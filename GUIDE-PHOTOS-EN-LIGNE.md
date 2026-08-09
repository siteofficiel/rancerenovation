# 🖼️ RANCE RENOVATION — Guide : photos en ligne depuis le panneau admin

## 🎯 Le principe (simplifié)

Tout se fait depuis le **panneau admin** (dans le site en ligne) :
1. Vous ajoutez vos photos (caméra du téléphone ou galerie)
2. Vous cliquez **« 📤 Publier mes photos »**
3. Les photos sont envoyées sur **ImgBB** (hébergement d'images gratuit)
4. Elles apparaissent sur votre site (après avoir mis le site configuré en ligne UNE fois)

**Aucun FTP, aucun fichier à déposer** une fois la configuration faite.
**Ça marche sur n'importe quel hébergeur** (LWS, OVH, GitHub Pages…).

---

## ⚙️ Configuration initiale (UNE SEULE FOIS, ~5 min)

### Étape 1 — Créer une clé API ImgBB (gratuite)
1. Allez sur **https://imgbb.com** → créez un compte gratuit
2. Connectez-vous → cliquez sur votre avatar (en haut à droite) → **API**
   (ou directement : https://api.imgbb.com)
3. Cliquez sur **Generate API key** → copiez la clé affichée (environ 30 caractères)

### Étape 2 — Enregistrer la clé dans le panneau admin
1. Ouvrez votre site (en local ou en ligne) → page **Nos prestations**
2. **Ctrl+Maj+A** (ordinateur) ou **menu ☰ → Mentions légales → ⚙ Admin en bas** (téléphone)
3. Mot de passe : `rance2024`
4. Section **« ☁️ Publication automatique »** :
   - Collez votre clé ImgBB dans le champ
   - Cliquez **« 🔑 Créer mon espace »** → la clé est vérifiée et enregistrée

### Étape 3 — Mettre le site configuré en ligne (1 seule fois)
1. Cliquez **« 💾 Télécharger le site configuré »** → vous obtenez un fichier HTML avec la clé intégrée
2. **Remplacez ce fichier sur votre hébergeur** (comme vous le faites déjà)
3. C'est fini — plus jamais besoin de retoucher au site pour les photos !

---

## 📸 Publier une photo (à chaque fois, 30 secondes)

1. Ouvrez le panneau admin (voir Étape 2)
2. Dans une galerie (Maçonnerie, Isolation…), cliquez :
   - **« 📷 Prendre une photo »** (téléphone : la caméra s'ouvre)
   - ou sur la **zone pointillée** pour choisir une photo
3. La photo apparaît avec le badge **NOUVEAU**
4. Cliquez **« 📤 Publier mes photos »**
5. ✅ Badge **EN LIGNE ✓** → la photo est publiée !
6. Les visiteurs la voient (cache ≤ 5 min)

---

## 📱 Depuis le téléphone, n'importe où

- Ouvrez votre site → **☰ Menu → Mentions légales → tout en bas → ⚙ Admin**
- Prenez la photo du chantier avec la caméra
- Publiez — c'est en ligne !

---

## ❓ Questions

### C'est gratuit ?
Oui. ImgBB est gratuit (stockage illimité pour comptes gratuits).

### Que se passe-t-il si je perds ma clé ?
Retournez sur imgbb.com → API → vous pouvez régénérer une clé. Ensuite,
répétez l'Étape 2 (collez la nouvelle clé → Téléchargez le site configuré → remplacez).

### Et si je n'ai pas configuré la clé ?
Le panneau fonctionne quand même : vous pouvez préparer vos photos et
générer un « pack » à déposer sur l'hébergeur (ancienne méthode, toujours
disponible via le bouton « 📦 Générer le pack photos »).

### Les photos restent-elles en ligne ?
Oui, tant que votre compte ImgBB existe. Pour un usage professionnel
critique, vous pouvez passer à un plan payant ImgBB (ou un autre service) —
le principe reste identique.
