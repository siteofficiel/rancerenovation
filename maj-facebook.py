# -*- coding: utf-8 -*-
"""
📡 MAJ-FACEBOOK.PY — Récupère les publications Facebook de RANCE RENOVATION
et met à jour les articles du site automatiquement.

Usage :
    python3 maj-facebook.py

Ce script :
  1. Ouvre la page Facebook publique (sans connexion)
  2. Récupère les photos des derniers posts
  3. Met à jour articles.json + les images dans le dossier articles/
  4. Affiche ce qu'il faut déposer sur l'hébergeur

⚠️ Limite technique : Facebook ne permet pas de lire les TEXTS des posts
sans compte connecté. Le script récupère donc les PHOTOS des derniers posts
et les associe à des articles types (titres métiers). Pour les textes
exacts, utilisez le panneau admin (bouton « 📝 Articles »).
"""
import json, os, re, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
ARTICLES_DIR = os.path.join(BASE, 'articles')
ARTICLES_JSON = os.path.join(ARTICLES_DIR, 'articles.json')

PAGE_URL = 'https://www.facebook.com/people/Rance-R%C3%A9novation/61568768357167/'
PAGE_DESC = ("Professionnel certifié RGE. RANCE RENOVATION est spécialisée dans la "
             "rénovation générale de votre habitat : maçonnerie, isolation, plâtrerie, "
             "menuiseries et revêtements de sols, aménagement de salle de bain et cuisine.")
PHONE = '07 71 45 46 19'

# Titres types utilisés quand le texte exact du post n'est pas accessible
TITLES = [
    "Nouveaux travaux en cours de réalisation",
    "Chantier du moment : rénovation en cours",
    "Découvrez nos dernières réalisations",
    "Un nouveau chantier vient de démarrer",
    "Retour en images sur nos chantiers",
    "L'équipe RANCE RENOVATION à l'œuvre",
]

def main():
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    print("📡 Récupération de la page Facebook…")

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(
            user_agent=("Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
                        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"),
            locale="fr-FR",
            viewport={'width': 390, 'height': 844},
            device_scale_factor=2,
        )
        pg = ctx.new_page()
        pg.goto(PAGE_URL, wait_until='domcontentloaded', timeout=45000)
        pg.wait_for_timeout(6000)

        # Faire défiler pour charger les photos
        for _ in range(5):
            pg.evaluate("window.scrollBy(0, 1000)")
            pg.wait_for_timeout(1000)

        # Capturer les photos des posts (images t39.30808-6)
        loc = pg.locator('img[src*="scontent"][src*="t39.30808-6"]')
        count = loc.count()
        print(f"   {count} photos trouvées")

        new_images = []
        stamp = datetime.date.today().strftime('%Y%m%d')
        for i in range(min(8, count)):
            out = os.path.join(ARTICLES_DIR, f'auto-{stamp}-{i+1:02d}.jpg')
            try:
                loc.nth(i).screenshot(path=out)
                size = os.path.getsize(out)
                if size > 6000:
                    new_images.append(f'auto-{stamp}-{i+1:02d}.jpg')
                    print(f"   ✅ {os.path.basename(out)} ({size//1024} Ko)")
            except Exception:
                pass
        b.close()

    if not new_images:
        print("❌ Aucune nouvelle photo récupérée (page inaccessible ?).")
        return

    # Charger les articles existants
    articles = []
    if os.path.exists(ARTICLES_JSON):
        try:
            articles = json.load(open(ARTICLES_JSON, encoding='utf-8')).get('articles', [])
        except Exception:
            articles = []

    # Ajouter les nouveaux articles (photos non déjà utilisées)
    used = {a.get('image', '').split('/')[-1] for a in articles}
    today = datetime.date.today()
    added = 0
    for idx, img in enumerate(new_images):
        if img in used:
            continue
        articles.append({
            "id": f"auto-{stamp}-{idx+1}",
            "title": TITLES[idx % len(TITLES)],
            "date": today.isoformat(),
            "text": f"{PAGE_DESC} Une question sur nos travaux ? Contactez-nous au {PHONE}.",
            "image": f"articles/{img}"
        })
        used.add(img)
        added += 1

    # Garder les 12 derniers articles
    articles = articles[-12:]

    data = {
        "version": 1,
        "generated": datetime.datetime.now().isoformat(),
        "articles": articles
    }
    json.dump(data, open(ARTICLES_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"\n✅ {added} nouvel(aux) article(s) ajouté(s) — {len(articles)} articles au total")
    print(f"📄 Fichier mis à jour : {ARTICLES_JSON}")
    print("\n➡️ Déposez sur votre hébergeur, dans le dossier articles/ :")
    print("   - articles.json")
    for img in new_images:
        print(f"   - {img}")

if __name__ == '__main__':
    main()
