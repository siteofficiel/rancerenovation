# -*- coding: utf-8 -*-
"""
Génère la page Actualités du site : toutes les publications Facebook de
RANCE RENOVATION, présentées en « petits articles » dans l'ordre
chronologique (la plus récente en premier), avec le texte écrit réel
de chaque publication, sa date et sa photo / vidéo.

Sources (sans compte Facebook) :
  - page Reels  : liste des vidéos (image de couverture, ordre, vues)
  - page Photos : album de photos (avant / après)
  - page d'un reel : le titre de la publication (= son texte écrit)
  - HTML d'un reel : la date exacte (creation_time)

Les images sont téléchargées en local (WebP) pour que le site reste
parfaitement autonome, même si Facebook change ses liens.
"""
import re, json, os, datetime, urllib.request

ROOT = '/home/user/rance-site'
IMG_DIR = f'{ROOT}/assets/actus'
CACHE = f'{IMG_DIR}/dates.json'
FB_PAGE = 'https://www.facebook.com/people/Rance-R%C3%A9novation/61568768357167/'
FB_REELS = 'https://www.facebook.com/profile.php?id=61568768357167&sk=reels_tab'
FB_PHOTOS = 'https://www.facebook.com/profile.php?id=61568768357167&sk=photos'
JINA = 'https://r.jina.ai/'

MOIS_FR = ['janvier','février','mars','avril','mai','juin',
           'juillet','août','septembre','octobre','novembre','décembre']

# ------------------------------------------------------------------
# Outils réseau
# ------------------------------------------------------------------
def fetch(url, timeout=60, as_html=False):
    req = urllib.request.Request(JINA + url, headers={
        'User-Agent': 'Mozilla/5.0',
        **({'x-respond-with': 'html'} if as_html else {}),
    })
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', errors='ignore')

def fetch_bytes(url, timeout=45):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=timeout).read()

def date_fr(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {MOIS_FR[d.month-1]} {d.year}"

# ------------------------------------------------------------------
# 1. Récupérer la liste des reels (page Reels, markdown)
# ------------------------------------------------------------------
def fetch_reels_list():
    """-> liste dicts: id, image_url, views, position (0 = plus récent)"""
    md = fetch(FB_REELS)
    reels = []
    for m in re.finditer(
        r'!\[Image \d+\]\((https://scontent[^)]+?)\)\s*(\d+)\]\(https://www\.facebook\.com/reel/(\d+)',
        md):
        reels.append({
            'id': m.group(3),
            'image_url': m.group(1).rstrip(')'),
            'views': int(m.group(2)),
            'position': len(reels),
        })
    return reels

# ------------------------------------------------------------------
# 2. Récupérer les photos de l'album (page Photos, markdown)
# ------------------------------------------------------------------
def fetch_album_photos():
    md = fetch(FB_PHOTOS)
    urls = []
    for u in re.findall(r'https://scontent[^)]+?\.jpg[^)]*', md):
        u = u.rstrip(')')
        if 'stp=dst-jpg_fb50' in u or u in urls:
            continue
        urls.append(u)
    return urls

# ------------------------------------------------------------------
# 3. Titre écrit + date exacte d'un reel (page individuelle)
# ------------------------------------------------------------------
def reel_info(rid, cache):
    """-> (titre, iso_date) — via cache si déjà connu."""
    if rid in cache and cache[rid].get('title') and cache[rid].get('date'):
        return cache[rid]['title'], cache[rid]['date']
    title, iso = None, None
    try:
        md = fetch(f'https://www.facebook.com/reel/{rid}/')
        m = re.search(r'^Title:\s*(.+?)\s*\| Rance Rénovation', md, re.M)
        if m:
            t = m.group(1).strip()
            if t and 'on Reels' not in t:
                title = t
    except Exception:
        pass
    try:
        html = fetch(f'https://www.facebook.com/reel/{rid}/', as_html=True)
        for m in re.finditer(r'"creation_time":(\d+)', html):
            ctx = html[max(0, m.start()-3000):m.end()+3000]
            if re.search(r'"id":"?' + rid + r'"?"?', ctx) or re.search(rid, ctx):
                iso = datetime.datetime.fromtimestamp(int(m.group(1)), datetime.UTC).date().isoformat()
                break
    except Exception:
        pass
    if title or iso:
        cache[rid] = {'title': title, 'date': iso}
        return title, iso
    return None, None

# ------------------------------------------------------------------
# 4. Télécharger les images en local (WebP)
# ------------------------------------------------------------------
def dl_webp(url, dest, w=720, h=960):
    """Télécharge et convertit en WebP (si le fichier n'existe pas déjà)."""
    if os.path.exists(dest):
        return True
    try:
        data = fetch_bytes(url)
    except Exception:
        return False
    try:
        from PIL import Image
        import io
        im = Image.open(io.BytesIO(data)).convert('RGB')
        if im.width > w * 2 or im.height > h * 2:
            im.thumbnail((w, h), Image.LANCZOS)
        im.save(dest, 'WEBP', quality=76, method=6)
    except Exception:
        return False
    return True

# ------------------------------------------------------------------
# 5. Données de secours (si Facebook est injoignable au moment du build)
# ------------------------------------------------------------------
FALLBACK = [
    {'kind': 'video', 'id': '2136507240601160', 'date': '2026-08-08',
     'title': 'Nouvelle vidéo',
     'text': 'Retrouvez notre toute dernière vidéo sur notre page Facebook.',
     'views': 208},
    {'kind': 'photos', 'id': 'album', 'date': '2026-07-28', 'approx': True,
     'title': 'Avant / Après',
     'text': 'Album photo de nos travaux : découvrez le résultat, avant et après le chantier.',
     'views': None},
    {'kind': 'video', 'id': '574974665342384', 'date': '2025-01-17',
     'title': "Démarrage d'une extension",
     'text': None, 'views': 68},
    {'kind': 'video', 'id': '494211920356152', 'date': '2025-01-05',
     'title': "Et voilà, les travaux sont terminés pour l'entreprise, les peintures seront réalisées par le client. À bientôt pour une nouvelle salle de bain 😉",
     'text': None, 'views': 136},
    {'kind': 'video', 'id': '27856206557358390', 'date': '2024-11-24',
     'title': "Terrasse en dalle grès cérame de 2 cm d'épaisseur",
     'text': None, 'views': 81},
    {'kind': 'video', 'id': '955188829975247', 'date': '2024-11-24',
     'title': "Réalisation d'une extension",
     'text': None, 'views': 95},
]

# ------------------------------------------------------------------
# 6. Assemblage des données
# ------------------------------------------------------------------
os.makedirs(IMG_DIR, exist_ok=True)
cache = {}
try:
    cache = json.load(open(CACHE, encoding='utf-8'))
except Exception:
    pass

posts, notes = [], []
try:
    reels = fetch_reels_list()
    album_urls = fetch_album_photos()
    notes.append(f"Facebook accessible : {len(reels)} vidéo(s), {len(album_urls)} photo(s) d'album.")
except Exception as e:
    reels, album_urls = [], []
    notes.append(f"Facebook injoignable ({e}) — utilisation des données de secours.")

for r in reels:
    title, iso = reel_info(r['id'], cache)
    posts.append({
        'kind': 'video',
        'id': r['id'],
        'date': iso or '2000-01-01',
        'title': title or 'Nouvelle vidéo',
        'text': None,
        'views': r['views'],
        'image_url': r['image_url'],
        'position': r['position'],
    })

if album_urls:
    posts.append({
        'kind': 'photos', 'id': 'album', 'date': '2026-07-28', 'approx': True,
        'title': 'Avant / Après',
        'text': 'Album photo de nos travaux : découvrez le résultat, avant et après le chantier.',
        'views': None, 'photo_urls': album_urls,
    })

# Si Facebook n'a rien donné : données de secours
if not posts:
    posts = [dict(p) for p in FALLBACK]

# Ordre chronologique : la plus récente d'abord (album « récent » placé
# avant 2025 ; à date égale, on garde l'ordre Facebook)
def sort_key(p):
    return (p['date'], p.get('position', 0))
posts.sort(key=sort_key, reverse=True)

# Télécharger les images locales
for p in posts:
    if p['kind'] == 'video':
        dest = f"{IMG_DIR}/reel_{p['id']}.webp"
        p['image'] = f"assets/actus/reel_{p['id']}.webp"
        if not os.path.exists(dest) and p.get('image_url'):
            if dl_webp(p['image_url'], dest):
                notes.append(f"Couverture vidéo {p['id']} téléchargée.")
            else:
                p['image'] = p['image_url']  # repli : image distante
    else:
        p['gallery'] = []
        for i, u in enumerate(p.get('photo_urls', []), start=1):
            dest = f"{IMG_DIR}/album_{i:02d}.webp"
            p['gallery'].append(f"assets/actus/album_{i:02d}.webp")
            if not os.path.exists(dest):
                u2 = re.sub(r'ctp=s\d+x\d+', 'ctp=s720x720', u)
                if dl_webp(u2, dest, w=720, h=720):
                    notes.append(f"Photo album {i} téléchargée.")
                else:
                    p['gallery'][-1] = u

# Sauvegarder le cache (titres + dates)
try:
    json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
except Exception:
    pass

# ------------------------------------------------------------------
# 7. Construire les petits articles
# ------------------------------------------------------------------
def build_article(p):
    kind = p['kind']
    badge = '<span class="fp-badge">📹 Vidéo</span>' if kind == 'video' else '<span class="fp-badge">📷 Photos</span>'
    img = p.get('image') or (p['gallery'][0] if p.get('gallery') else '')
    link = f'https://www.facebook.com/reel/{p["id"]}/' if kind == 'video' else FB_PAGE

    # Date
    if p.get('approx'):
        date_html = '<span class="fp-date">Publié récemment</span>'
    elif p['date'] and p['date'] != '2000-01-01':
        date_html = f'<span class="fp-date">📅 {date_fr(p["date"])}</span>'
    else:
        date_html = ''

    # Vues (uniquement pour les vidéos, si connu)
    views_html = f'<span class="fp-views">👁 {p["views"]} vues</span>' if (kind == 'video' and p.get('views')) else ''

    # Titre = texte écrit de la publication
    title = p.get('title') or 'Nouvelle publication'
    title_html = f'<h3 class="fp-title"><a href="{link}" target="_blank" rel="noopener">{title}</a></h3>'

    # Texte libre (complément, uniquement s'il existe réellement)
    text_html = ''
    if p.get('text'):
        text_html = f'<p class="fp-text">{p["text"]}</p>'

    # Miniatures de l'album
    gal_html = ''
    if kind == 'photos' and p.get('gallery'):
        items = '\n'.join(
            f'<a class="fp-thumb" href="{link}" target="_blank" rel="noopener" title="Voir sur Facebook"><img src="{u}" alt="Photo avant / après" loading="lazy"></a>'
            for u in p['gallery'])
        gal_html = f'<div class="fp-subgallery">{items}</div>'

    img_html = ''
    if img:
        img_html = (f'<a class="fp-img" href="{link}" target="_blank" rel="noopener">'
                    f'<img src="{img}" alt="Publication Facebook" loading="lazy">'
                    f'<span class="fp-play">▶</span></a>')

    return f'''      <article class="fp-card">
        {img_html}
        <div class="fp-body">
          <div class="fp-meta">
            {badge}
            {date_html}
            {views_html}
          </div>
          {title_html}
          {text_html}
          {gal_html}
          <a class="fp-link" href="{link}" target="_blank" rel="noopener">
            Voir sur Facebook
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7"/><path d="M7 7h10v10"/></svg>
          </a>
        </div>
      </article>'''

cards = '\n'.join(build_article(p) for p in posts)
known_ids = ','.join(f"'{p['id']}'" for p in posts if p['kind'] == 'video')
gen_date = datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')

page = f'''  <main class="site-content">
    <div class="container">

      <!-- En-tête -->
      <div class="actus-header">
        <h2>Nos actualités</h2>
        <p>Chaque publication de notre page Facebook, présentée comme un petit article — dans l'ordre, de la plus récente à la plus ancienne.</p>
      </div>

      <!-- Bandeau « nouvelle publication » (rempli par le script si besoin) -->
      <div class="fp-new-banner" id="fp-new-banner" hidden></div>

      <!-- Publications Facebook -->
      <div class="fp-grid" id="fp-grid">
{cards}
      </div>

      <p class="fp-note">Publications récupérées depuis notre page Facebook · dernière mise à jour : {gen_date}</p>

      <!-- Lien vers la page -->
      <div class="actus-fb-link">
        <a href="{FB_PAGE}" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.7c0-.9.3-1.6 1.6-1.6h1.7V3.2c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.4V13h2.7v8h3.4z"/></svg>
          Voir toute notre page Facebook
        </a>
      </div>

    </div>
  </main>

  <!-- Détection automatique des nouvelles publications -->
  <script>
  (function () {{
    'use strict';
    /* Au chargement, on vérifie discrètement si de nouvelles publications
       sont parues sur Facebook. Si oui, un bandeau l'indique. */
    var CONNUES = [{known_ids}];
    var banniere = document.getElementById('fp-new-banner');
    if (!banniere) return;

    function signaler(libelle, lien) {{
      banniere.hidden = false;
      banniere.innerHTML = '🆕 ' + libelle + ' — <a href="' + lien + '" target="_blank" rel="noopener">la voir sur Facebook</a>';
    }}

    function verifierReels() {{
      fetch('{JINA}{FB_REELS}', {{ cache: 'no-store' }})
        .then(function (r) {{ if (!r.ok) throw new Error('http ' + r.status); return r.text(); }})
        .then(function (t) {{
          var ids = t.match(/facebook\\.com\\/reel\\/(\\d+)/g) || [];
          for (var i = 0; i < ids.length; i++) {{
            var id = ids[i].replace(/[^0-9]/g, '');
            if (CONNUES.indexOf(id) === -1) {{
              signaler('Une nouvelle vidéo vient d\\'être publiée sur notre page Facebook',
                       'https://www.facebook.com/reel/' + id + '/');
              return;
            }}
          }}
        }})
        .catch(function () {{ /* silencieux */ }});
    }}

    verifierReels();
    setInterval(verifierReels, 10 * 60 * 1000); /* toutes les 10 minutes */
  }})();
  </script>
'''

# ------------------------------------------------------------------
# 8. Assembler la page complète (header + footer depuis nos-prestations)
# ------------------------------------------------------------------
tpl = open(f'{ROOT}/nos-prestations.html', encoding='utf-8').read()
header = tpl[:tpl.find('<!-- ==================== TITRE DE PAGE')]
footer = tpl[tpl.find('<!-- ==================== PIED DE PAGE'):]
header = header.replace(' class="current"', '')
header = header.replace('<li><a href="actualites.html">Actualités</a></li>',
                        '<li class="current"><a href="actualites.html">Actualités</a></li>')

title_block = '''  <!-- ==================== TITRE DE PAGE ==================== -->
  <div class="container">
    <div class="page-title">
      <h1>Actualités</h1>
      <div class="breadcrumbs">
        <a href="index.html"><span>Home</span></a>
        <span class="sep">&raquo;</span>
        <span>Actualités</span>
      </div>
    </div>
  </div>
'''

html = header + '\n' + title_block + '\n' + page + '\n' + footer
html = html.replace('<title>Nos prestations - RANCE RENOVATION</title>',
                    '<title>Actualités - RANCE RENOVATION</title>')
html = html.replace('<meta name="description" content="Les prestations de RANCE RENOVATION',
                    '<meta name="description" content="Les actualités de RANCE RENOVATION, entreprise de travaux du bâtiment à Dinan.">')
open(f'{ROOT}/actualites.html', 'w', encoding='utf-8').write(html)

print(f"✅ actualites.html généré — {len(posts)} publication(s) dans l'ordre")
for p in posts:
    print(f"   - {p['date']} | {p['kind']:6} | {p.get('title','')[:60]}")
print(f"   Taille: {os.path.getsize(f'{ROOT}/actualites.html')//1024} Ko")
for n in notes:
    print('   ℹ️', n)
