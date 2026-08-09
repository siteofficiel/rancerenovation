# 🌐 GUIDE — Mise en ligne du site chez LWS

Votre site est prêt : 9 fichiers HTML autonomes (chaque page contient ses
images). Il ne reste qu'à les déposer chez votre hébergeur LWS.

---

## Étape 1 — Se connecter à l'espace client LWS

1. Allez sur **https://www.lws.fr** et cliquez sur **« Espace client »** (en haut à droite).
2. Connectez-vous avec votre identifiant client et votre mot de passe.

## Étape 2 — Ouvrir le gestionnaire de fichiers

1. Dans le menu de gauche, cliquez sur **« Hébergement »** puis sur votre **nom de domaine** (rancerenovation.fr).
2. Cliquez sur **« Gestion des fichiers »** ou **« FTP »** selon ce qui est affiché.
3. Ouvrez le dossier **`www`** (ou **`htdocs`**) : c'est là que va votre site.

## Étape 3 — Déposer les fichiers

1. Décompressez le fichier `upload-lws.zip` sur votre ordinateur.
2. Dans le dossier décompressé, **sélectionnez les 9 fichiers `*.html`** ainsi que les favicons (`favicon.png`, `favicon.ico`, `favicon-16.png`, `favicon-32.png`, `favicon-48.png`, `apple-touch-icon.png`).
3. **Glissez-les** dans le gestionnaire de fichiers LWS (ou utilisez le bouton « Téléverser »).
4. Si LWS vous demande de remplacer des fichiers existants : **« Oui, remplacer »**.

> ⚠️ Important : remplacez TOUS les fichiers, pas seulement les nouveaux,
> pour être sûr d'avoir la dernière version.

## Étape 4 — Vérifier

1. Ouvrez **https://rancerenovation.fr** dans votre navigateur.
2. Videz le cache si besoin : **Ctrl + F5** (Windows) ou **Cmd + Maj + R** (Mac).
3. Cliquez sur **Actualités** : vous devez voir les publications Facebook
   présentées en petits articles, avec le texte de chaque publication.

## Mettre à jour le site plus tard

Quand on vous donne une nouvelle version du site (nouveaux fichiers),
refaites les étapes 2 et 3 : déposez les nouveaux fichiers en remplaçant
les anciens, puis **Ctrl + F5** pour vider le cache.

---

### Pour les photos en ligne (sans repasser par l'hébergeur)

Le panneau admin (Ctrl + Maj + A sur le site) permet d'ajouter des photos
qui sont publiées **automatiquement** via Firebase — voir `GUIDE-FIREBASE.md`
et `TUTO-AJOUTER-PHOTOS.html` dans ce dossier.
