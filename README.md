# 🏗️ RANCE RENOVATION — Site multi-fichiers (GitHub Pages)

**9 fichiers HTML, 1 page par fichier** — chaque fichier est autonome (images incluses). Aucun zip, aucune installation.

## 📄 Les fichiers

| Fichier | Page | Taille |
|---|---|---|
| `index.html` | Accueil (slider) | 1,1 Mo |
| `a-propos.html` | À propos | 0,3 Mo |
| `nos-prestations.html` | Prestations + **panneau admin** | 1,3 Mo |
| `nos-realisations.html` | Réalisations | 1,9 Mo |
| `actualites.html` | Actualités | 0,1 Mo |
| `contactez-nous.html` | Contact | 0,1 Mo |
| `politique-de-confidentialite.html` | Confidentialité | 0,1 Mo |
| `mentions-legales.html` | Mentions légales | 0,1 Mo |
| `plan-du-site.html` | Plan du site | 0,1 Mo |

## 🚀 Mise en ligne sur GitHub (10 minutes)

### Étape 1 — Compte GitHub
**https://github.com** → **Sign up** → gratuit.

### Étape 2 — Créer le dépôt
1. Bouton **+** (haut à droite) → **New repository**
2. Nom : `rance-renovation-site` → **Public** → **Create repository**

### Étape 3 — Envoyer LES 9 FICHIERS
1. Sur la page du dépôt : **« uploading an existing file »**
2. **Glissez les 9 fichiers `*.html` en même temps** dans la zone (sélectionnez-les tous dans le dossier, ou glissez le dossier complet — GitHub acceptera les fichiers)
   ⚠️ Glissez les **fichiers**, jamais le fichier zip !
3. **Commit changes** (vert)

### Étape 4 — Activer le site
1. **Settings** → **Pages**
2. Branch `main` → `/ (root)` → **Save**
3. Attendez 1-2 min

### ✅ En ligne !
```
https://VOTRE-PSEUDO.github.io/rance-renovation-site/
```

## 📸 Ajouter des photos (une fois en ligne)

1. Ouvrez **nos-prestations.html** (en local ou en ligne)
2. **`Ctrl` + `Maj` + `A`** → mot de passe : `rance2024`
3. Glissez vos photos → **💾 Télécharger le site à jour** → vous obtenez un nouveau `nos-prestations.html`
4. Sur GitHub : **Add file** → **Upload files** → glissez le nouveau fichier → **Commit changes**
5. En ligne en 1-2 minutes !

> 💡 Sur la page Actualités, le petit ⚙ Admin en bas renvoie directement vers `nos-prestations.html#admin` (panneau auto-ouvert).

## 🔧 Changer le mot de passe
- Dans `nos-prestations.html`, cherchez `rance2024` et remplacez-le.

## 💡 Tester en local avant GitHub
Double-cliquez sur `index.html` — tout fonctionne sans serveur (les liens entre pages sont normaux : `a-propos.html`, etc.).

## 📰 Page Actualités — flux Facebook

La page `actualites.html` affiche automatiquement les publications de la page
Facebook **Rance Rénovation** (via le plugin officiel Facebook).

- Publiez sur Facebook → la publication apparaît sur le site (quelques secondes)
- Aucune manipulation nécessaire après la mise en ligne
- Si le flux ne peut pas s'afficher (page privée, région, etc.), un message de
  secours propose un lien direct vers la page Facebook
- Pour changer la page affichée : dans `actualites.html`, modifiez le
  `data-href` du bloc `.fb-page` avec l'URL de votre page
