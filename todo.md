### TODO

# Page d'acceuil personnalisée :
- [ ] : Présente une vue d'ensemble du programme de workout, avec les objectifs, des statistiques rapides (calories brûlées, temps total d'entraînement, progression, etc.), et des encouragements personnalisés

## Pour toute les pages :
- [ ] : Faire une barre de navigation commune pour toutes les pages

# Stylesheets :
- [ ] : Ajouter un style pour les notifications de warning

# Démarrage Serveur :
- [ ] : récupérer la nouvelle clé de ngrok
- [ ] : l'envoyer en notif au tel

- [ ] : une fois les étapes ci-dessus faites -> scripter le lancement du serveur

# Authentification / Verification accès serveur :
- [ ] : enregistrer les appareils autorisés
- [ ] : vérifier les appareils autorisés
- [ ] : envoyer une notification si un appareil non autorisé se connecte

# Page records

- [ ] : table complete anciens records

# For the Python requirements :
Check the requirements.txt file to find every packages needed

# For the python environnement :
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
.\app_env\Scripts\activate
Set-ExecutionPolicy -ExecutionPolicy Restricted 

install with proxy:
pip install --proxy=http://PITC-Zscaler-Global-ZEN.proxy.corporate.ge.com:80 panel

# How to serve
panel serve app.py --address 127.0.0.1 --port 5006 --allow-websocket-origin=*

with dev :
panel serve app.py --address 127.0.0.1 --port 5006 --allow-websocket-origin=* --dev

panel serve home_page.py project_page.py database_page.py --address 127.0.0.1 --port 5006 --allow-websocket-origin=* --dev --index=home_page