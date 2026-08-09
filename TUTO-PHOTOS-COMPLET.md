# 📸 TUTORIEL COMPLET — Mettre en ligne vos photos (de A à Z)

> **Objectif** : pouvoir ajouter des photos à votre site depuis n'importe où
> (PC, téléphone, tablette) et les voir en ligne **sans jamais toucher aux
> fichiers du site** après la première configuration.

---

## 📋 SOMMAIRE

- [PARTIE 1 — Créer votre clé ImgBB (une seule fois, 5 min)](#partie-1)
- [PARTIE 2 — Enregistrer la clé dans le panneau admin (5 min)](#partie-2)
- [PARTIE 3 — Mettre le site configuré en ligne (10 min)](#partie-3)
- [PARTIE 4 — Ajouter et publier une photo (30 secondes, à chaque fois)](#partie-4)
- [PARTIE 5 — Ajouter un article sur Facebook → sur le site](#partie-5)
- [PARTIE 6 — Dépannage](#partie-6)

---

<a name="partie-1"></a>
## 🗝️ PARTIE 1 — Créer votre clé ImgBB (UNE SEULE FOIS)

ImgBB est un service **gratuit** qui héberge vos photos en ligne.
La clé API permet à votre panneau admin d'envoyer les photos dessus.

### Étape 1.1 — Créer le compte
1. Ouvrez **https://imgbb.com** sur votre navigateur (PC ou téléphone)
2. Cliquez sur **« Sign up »** (S'inscrire) en haut à droite
3. Remplissez le formulaire (email, mot de passe) et validez
4. Vérifiez votre email (cliquez sur le lien reçu)

### Étape 1.2 — Générer la clé API
1. Connectez-vous sur imgbb.com
2. Cliquez sur votre **avatar** (photo de profil, en haut à droite)
3. Dans le menu, cliquez sur **« API »**
   (ou allez directement sur : **https://api.imgbb.com**)
4. Cliquez sur le bouton **« Generate API key »**
5. Votre clé s'affiche : une chaîne d'environ **30 caractères** du type :
   `a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`
6. **Copiez-la** et gardez-la précieusement (dans un bloc-notes)

> ⚠️ La clé est comme un mot de passe : ne la partagez pas.

✅ **PARTIE 1 terminée** — vous avez votre clé.

---

<a name="partie-2"></a>
## ⚙️ PARTIE 2 — Enregistrer la clé dans le panneau admin

### Étape 2.1 — Ouvrir le panneau admin

**Sur ordinateur :**
1. Ouvrez le fichier `nos-prestations.html` (ou le site en ligne)
2. Appuyez sur **Ctrl + Maj + A** en même temps
3. Le panneau s'ouvre

**Sur téléphone :**
1. Ouvrez votre site en ligne
2. Appuyez sur le menu **☰** (en haut)
3. Allez dans **« Mentions légales »**
4. Descendez **tout en bas** de la page
5. Appuyez sur le petit **⚙ Admin**
6. Le panneau s'ouvre

### Étape 2.2 — Se connecter
1. Mot de passe : **`rance2024`**
2. Cliquez **« Se connecter »**

### Étape 2.3 — Enregistrer la clé
1. Dans le panneau, cherchez la section **« ☁️ Publication automatique en ligne »**
2. Collez votre clé ImgBB dans le champ **« Clé API ImgBB »**
3. Cliquez sur **« 🔑 Enregistrer ma clé »**
4. Le message s'affiche : **« ✅ Clé valide et enregistrée ! »**

### Étape 2.4 — Télécharger le site configuré (IMPORTANT)
1. Cliquez sur **« 💾 Télécharger le site configuré »**
2. Le navigateur télécharge un fichier HTML (par ex. `nos-prestations.html`)
3. **C'est CE fichier qu'il faudra mettre en ligne** (voir Partie 3)

✅ **PARTIE 2 terminée** — votre site sait maintenant publier.

---

<a name="partie-3"></a>
## 🚀 PARTIE 3 — Mettre le site configuré en ligne (UNE SEULE FOIS)

> ⚠️ Cette partie se fait **une seule fois** après avoir enregistré la clé.
> Ensuite, vous n'aurez plus JAMAIS à remettre le site en ligne.

### Option A — Hébergeur LWS (FileZilla)

1. Ouvrez **FileZilla** (gratuit sur filezilla-project.org)
2. Connectez-vous avec vos identifiants FTP LWS
3. À gauche (votre PC) : ouvrez le dossier où est le fichier téléchargé
4. À droite (le serveur) : ouvrez le dossier racine du site (souvent `www/`)
5. **Glissez le fichier `nos-prestations.html`** de gauche vers la droite
6. FileZilla demande « Écraser ? » → **Oui**
7. C'est fait !

### Option B — GitHub Pages

1. Allez sur votre dépôt GitHub (github.com → votre dépôt)
2. Cliquez sur le fichier `nos-prestations.html` existant
3. Cliquez sur l'icône **✏️ (crayon)** pour modifier
4. **Supprimez tout le contenu** (Ctrl+A puis Suppr)
5. Allez dans l'onglet **« Edit file »** → **« Upload files »** impossible ici...
   → Plus simple : revenez en arrière, cliquez **« Add file » → « Upload files »**
   → Glissez le **nouveau** `nos-prestations.html` par-dessus (GitHub remplace)
6. **Commit changes**
7. Attendez 1-2 minutes

### Étape 3.1 — Vérifier
1. Ouvrez votre site en ligne
2. Page **Nos prestations** → panneau admin
3. Le message s'affiche : **« ✅ Clé enregistrée »** (la clé est dans le site)

✅ **PARTIE 3 terminée** — plus jamais besoin de remettre le site en ligne !

---

<a name="partie-4"></a>
## 📷 PARTIE 4 — Ajouter et publier une photo (30 secondes, à chaque fois)

### Étape 4.1 — Ouvrir le panneau admin
- PC : **Ctrl + Maj + A** sur la page Prestations
- Téléphone : **☰ Menu → Mentions légales → ⚙ Admin en bas**

### Étape 4.2 — Ajouter la photo
Dans la galerie de votre choix (Maçonnerie, Isolation, Menuiseries, Sols, Peinture) :

**Depuis un téléphone :**
- Cliquez sur **« 📷 Prendre une photo »** → la caméra s'ouvre → prenez la photo
- Ou cliquez sur la **zone en pointillés** → choisissez dans vos photos

**Depuis un ordinateur :**
- **Glissez-déposez** vos photos dans la zone en pointillés
- Ou cliquez pour parcourir vos fichiers

La photo apparaît avec le badge **« NOUVEAU »**.

### Étape 4.3 — Publier
1. Cliquez sur **« 📤 Publier mes photos »**
2. Patientez quelques secondes (envoi sur ImgBB)
3. Le badge passe à **« EN LIGNE ✓ »**
4. Le message s'affiche : **« ✅ photo(s) publiée(s) ! »**

### Étape 4.4 — Vérifier en ligne
1. Ouvrez votre site (ou rechargez avec F5)
2. Allez dans la galerie → **la photo est là !** 🎉

> ⏱️ Si la photo n'apparaît pas tout de suite, attendez **2-5 minutes**
> (cache du site) puis rechargez.

✅ **PARTIE 4 terminée** — c'est tout ! À chaque nouvelle photo, répétez
simplement la Partie 4.

---

<a name="partie-5"></a>
## 📰 PARTIE 5 — Ajouter un article (publication Facebook → site)

Pour transformer une publication Facebook en article sur le site :

1. Ouvrez le panneau admin (voir Partie 4.1)
2. Section **« 📝 Articles »** (si présente sur votre version)
3. Remplissez : **Titre**, **Date**, **Texte** (copiez depuis Facebook), **Photo**
4. Cliquez **« ➕ Ajouter l'article »**
5. Cliquez **« 📦 Générer le pack articles »**
6. Déposez `articles.json` + les images dans le dossier `articles/` de l'hébergeur
   (comme avant, via FTP ou GitHub)

> ℹ️ Si la section Articles n'existe pas sur votre version, les articles
> se gèrent avec le pack `articles/` directement.

---

<a name="partie-6"></a>
## 🆘 PARTIE 6 — Dépannage

### ❌ « Clé invalide » à l'enregistrement
- Vérifiez que vous avez **copié toute la clé** (30 caractères, sans espaces)
- Régénérez une clé sur imgbb.com → API → Generate key
- Réessayez

### ❌ « Impossible de contacter ImgBB »
- Vérifiez votre **connexion Internet**
- Réessayez dans 1 minute

### ❌ « Aucune nouvelle photo à publier »
- Vous n'avez pas ajouté de photo AVANT de cliquer sur Publier
- Ajoutez d'abord des photos (Partie 4.2)

### ❌ La photo publiée n'apparaît pas sur le site en ligne
1. Avez-vous mis le **site configuré** en ligne (Partie 3) ?
   → Sans cela, le site ne sait pas où chercher les photos
2. Attendez **2-5 minutes** (cache)
3. Rechargez avec **Ctrl+F5** (vidage du cache)

### ❌ Je perds ma clé
- Retournez sur imgbb.com → API → la clé est affichée (ou régénérez-la)
- Répétez la Partie 2 (nouvelle clé + nouveau site configuré à remettre en ligne)

### ❌ Je veux supprimer une photo publiée
1. Dans le panneau admin, cliquez sur le **×** rouge de la photo
2. La photo est retirée de la galerie
3. Pour la retirer du site en ligne : supprimez-la de votre compte ImgBB
   (imgbb.com → vos images → corbeille)

---

## 🎉 RÉSUMÉ EN UNE LIGNE

> **Une fois la clé enregistrée et le site configuré mis en ligne :
> téléphone → ⚙ Admin → 📷 photo → 📤 Publier → c'est en ligne !**

| Tâche | Fait |
|---|---|
| Créer le compte ImgBB + clé API | Une seule fois |
| Enregistrer la clé dans le panneau | Une seule fois |
| Mettre le site configuré en ligne | Une seule fois |
| Ajouter + publier une photo | **À chaque fois (30 s)** |
