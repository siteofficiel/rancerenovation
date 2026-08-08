# 🖼️ RANCE RENOVATION — Guide : photos en ligne sans ré-uploader le site

## 🎯 Le principe

Le site en ligne **lit automatiquement** un petit fichier `photos/photos.json`
placé à côté de lui sur votre hébergeur. Ce fichier liste vos photos par galerie.

→ Pour ajouter des photos : vous déposez **uniquement les nouveaux fichiers**
dans le dossier `photos/` de votre hébergeur (FTP, cPanel, OVH, FileZilla…).
**Le site lui-même n'est jamais ré-uploadé.** Les visiteurs voient les
nouvelles photos dès le rechargement de la page.

✅ Fonctionne avec **n'importe quel hébergeur** (rien à installer, pas d'API).

---

## 🚀 Première mise en place (une seule fois)

1. **Mettez votre site en ligne** (les fichiers `index.html`, `nos-prestations.html`, etc.)
2. **Créez un dossier `photos/`** à côté des pages, sur l'hébergeur :
   ```
   / (racine de votre site)
   ├── index.html
   ├── nos-prestations.html
   ├── ... (vos pages)
   └── photos/          ← à créer
   ```
3. C'est tout ! Le site fonctionne avec ou sans le dossier (s'il est vide,
   rien ne change).

---

## 📸 Ajouter des photos (à chaque fois)

### Étape 1 — Ouvrir le panneau admin
- Ouvrez `nos-prestations.html` (en local sur votre PC)
- Appuyez sur **`Ctrl` + `Maj` + `A`** → mot de passe : **`rance2024`**

### Étape 2 — Ajouter vos photos
- Glissez-déposez vos photos dans la galerie voulue (Maçonnerie, Isolation…)
- Elles sont compressées automatiquement

### Étape 3 — Générer le pack photos
- Cliquez sur **« 📦 Générer le pack photos »**
- Votre navigateur télécharge :
  - `photos.json` (la liste des photos)
  - les fichiers images (`nom.jpg`)

### Étape 4 — Envoyer sur l'hébergeur
- Ouvrez votre **FTP / gestionnaire de fichiers** (FileZilla, cPanel, OVH…)
- Déposez les fichiers téléchargés dans le dossier **`photos/`** de votre site :
  ```
  photos/
  ├── photos.json
  └── (vos nouvelles images)
  ```
- ⚠️ Si vous mettez les images dans des sous-dossiers, gardez la même
  structure que dans `photos.json` (ex : `photos/s0/...`).

### ✅ Résultat
Les visiteurs de votre site en ligne voient les nouvelles photos
**immédiatement** (le site recharge automatiquement la liste toutes les
5 minutes, ou à chaque visite).

---

## ❓ Questions fréquentes

### Le site affiche les photos avec 5 min de retard ?
Le site met en cache la liste 5 minutes pour être rapide. Un simple
rechargement de page (F5) après ce délai affiche les nouveautés.

### Je veux supprimer une photo en ligne ?
- Supprimez le fichier image dans le dossier `photos/` de l'hébergeur
- Mettez à jour `photos.json` (générez le pack sans cette photo) et déposez-le

### Je n'ai pas de dossier photos/ sur mon hébergeur ?
Créez-le avec le gestionnaire de fichiers de votre hébergeur (bouton
« Nouveau dossier »). C'est le seul prérequis.

### Et le bouton « 💾 Télécharger le site à jour » ?
Il reste utile si vous voulez une version **tout-en-un** (photos intégrées
directement dans le fichier) — par exemple pour garder une copie locale
complète. Mais pour le site en ligne, le pack photos suffit.

---

## 🗂️ Structure recommandée de l'hébergeur

```
/ (racine)
├── index.html              ← vos pages (jamais ré-uploadées pour les photos)
├── nos-prestations.html
├── ...
└── photos/
    ├── photos.json         ← régénéré à chaque ajout
    └── (vos images)
```

---

# 📝 Guide complémentaire : les ARTICLES (page Actualités)

Les publications Facebook peuvent être **adaptées en articles** pour le site,
avec une belle mise en page (carte avec image, date, texte).

## Comment ça marche

1. Ouvrez `nos-prestations.html` en local → `Ctrl+Maj+A` → `rance2024`
2. Dans le panneau, section **« 📝 Articles »** :
   - **Titre** de la publication (ex : « Nouveau chantier à Dinan »)
   - **Date** (format calendrier)
   - **Texte** de la publication (copiez-le depuis Facebook)
   - **Photo** (optionnelle — l'image du post Facebook)
3. Cliquez **« ➕ Ajouter l'article »** → il apparaît dans la liste
4. Cliquez **« 📦 Générer le pack articles »** → votre navigateur télécharge :
   - `articles.json`
   - les images des articles
5. Sur votre hébergeur : déposez ces fichiers dans le dossier **`articles/`**
   (à côté du site, comme le dossier `photos/`)

## ✅ Résultat

La page **Actualités** affiche automatiquement vos articles en belles cartes :
image (16:9), date formatée en français, titre, texte — et le lien vers
Facebook. Les visiteurs voient les nouveaux articles dès le rechargement.

## 🗂️ Structure de l'hébergeur

```
/ (racine)
├── index.html
├── ...
├── photos/
│   ├── photos.json
│   └── (images)
└── articles/
    ├── articles.json
    └── (images des articles)
```

## ❓ Supprimer un article ?
Dans le panneau admin, section Articles → bouton × sur l'article → régénérez
le pack → remplacez `articles.json` (+ images) sur l'hébergeur.

---

# 🤖 Mise à jour AUTOMATIQUE depuis Facebook (script)

Un script est inclus : **`maj-facebook.py`**

## Ce qu'il fait
- Ouvre la page Facebook publique de RANCE RENOVATION (sans connexion)
- Récupère les **photos des derniers posts**
- Met à jour automatiquement `articles/articles.json` + les images
- Prépare les fichiers à déposer sur l'hébergement

## Comment l'utiliser
```
python3 maj-facebook.py
```
Puis déposez les fichiers indiqués dans le dossier `articles/` de l'hébergeur.

## ⚠️ Limite technique (importante)
Facebook **ne permet pas** de lire les textes des publications sans compte
connecté ni clé API. Le script récupère donc les **photos** des posts et les
associe à des articles types. Pour les textes exacts de vos publications,
utilisez le panneau admin (section « 📝 Articles ») — le pack se dépose de
la même façon dans `articles/`.
