# 🔥 GUIDE — Publier vos photos avec Firebase (SANS clé, SANS FTP)

> **Le nouveau système** : vos photos sont stockées sur **Firebase** (service
> gratuit de Google). Vous n'avez besoin que d'**UNE URL** — pas de clé API,
> pas de FTP, rien à déposer sur l'hébergeur après la première fois.

---

## 🎯 Pourquoi Firebase ?
- ✅ **Gratuit** (1 Go de stockage, 10 Go de transfert/mois — largement assez)
- ✅ **Fiable** (c'est Google)
- ✅ **Une seule URL à copier** (pas de clé compliquée)
- ✅ Fonctionne sur **n'importe quel hébergeur** (LWS, GitHub, OVH…)

---

## 📝 ÉTAPE 1 — Créer la base Firebase (5 minutes, UNE seule fois)

### 1.1 — Créer le projet
1. Ouvrez **https://console.firebase.google.com** sur votre téléphone ou PC
2. Connectez-vous avec votre **compte Google** (si vous n'en avez pas,
   créez-en un gratuitement sur google.com)
3. Cliquez sur **« Créer un projet »** (Create a project)
4. Nom du projet : `rance-photos` (ou autre)
5. Cliquez **« Continuer »** puis **« Créer le projet »**
6. Attendez quelques secondes → **« Continuer »**

### 1.2 — Activer la Realtime Database
1. Dans le menu de gauche, cherchez **« Build »** → **« Realtime Database »**
2. Cliquez **« Créer une base de données »** (Create database)
3. Région : **« europe-west1 (Belgique) »** (ou laissez celle proposée)
4. Mode de sécurité : choisissez **« Mode de test »** (Test mode)
   > 💡 Le mode test permet au site d'écrire/lire les photos sans mot de passe.
   > Parfait pour un petit site. (Après 30 jours, il suffira de re-confirmer
   > les règles dans la console — 1 clic.)
5. Cliquez **« Activer »** (Enable)

### 1.3 — Copier l'URL de la base
1. Sur la page **« Realtime Database »** (onglet **Données** / Data), regardez
   en haut : vous voyez l'**URL de la base** :
   ```
   https://rance-photos-default-rtdb.firebaseio.com
   ```
2. **Copiez cette URL** (elle finit par `-default-rtdb.firebaseio.com`)

> ✅ C'est TOUT. Cette URL est votre « clé » — et elle n'est pas secrète.

---

## ⚙️ ÉTAPE 2 — Entrer l'URL dans le panneau admin (2 minutes)

1. Ouvrez votre site → panneau admin :
   - PC : **Ctrl + Maj + A** sur la page Prestations
   - Téléphone : **☰ Menu → Mentions légales → ⚙ Admin en bas**
2. Mot de passe : `rance2024`
3. Section **« ☁️ Publication automatique en ligne »** :
   - Collez l'**URL de la base Firebase** dans le champ
   - Cliquez **« 🔧 Tester la connexion »**
   - Message : **« ✅ Connexion réussie ! »**
4. Cliquez **« 💾 Télécharger le site configuré »**
5. **Remplacez ce fichier sur votre hébergeur** (1 seule fois, comme d'habitude)

---

## 📸 ÉTAPE 3 — Publier des photos (à chaque fois, 30 secondes)

1. Panneau admin → ajoutez vos photos (📷 caméra ou glisser-déposer)
2. Cliquez **« 📤 Publier mes photos »**
3. Badge **« EN LIGNE ✓ »**
4. Rechargez votre site (F5) → **les photos sont là !** 🎉

---

## 🆘 Dépannage

### « Impossible de joindre Firebase : Réponse 404 »
→ L'URL est fausse ou la base n'existe pas. Vérifiez qu'elle ressemble à :
`https://VOTRE-PROJET-default-rtdb.firebaseio.com` (sans rien après).

### « Impossible de joindre Firebase : Failed to fetch »
→ Problème de connexion Internet, ou l'URL a un caractère en trop (espace,
slash final…). Corrigez et réessayez.

### Les photos ne s'affichent pas sur le site en ligne
1. Avez-vous mis le **« site configuré »** en ligne (Étape 2, point 4-5) ?
2. Attendez 2-5 minutes (cache) puis **Ctrl+F5**

### Mode test expiré après 30 jours
1. Console Firebase → Realtime Database → onglet **« Règles »** (Rules)
2. Remplacez par :
   ```json
   {
     "rules": {
       ".read": true,
       ".write": true
     }
   }
   ```
3. **Publier** (Publish)

---

## 🎉 RÉSUMÉ
> **Une fois la base créée et l'URL entrée : téléphone → ⚙ Admin → 📷 photo
> → 📤 Publier → c'est en ligne !** Sans clé, sans FTP, sans hébergeur.
