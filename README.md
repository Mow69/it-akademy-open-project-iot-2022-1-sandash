[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6640314&assignment_repo_type=AssignmentRepo)
<a href="https://aimeos.org/">
    <img src="https://res.cloudinary.com/it-akademy/image/upload/f_auto,q_auto,h_60/logo_2x_feoygs.png" alt="IT-Akademy logo" title="IT-Akademy" align="right" height="60" />
</a>

# Open Project IoT

![Project](https://img.shields.io/badge/Projet_type-IoT-blue.svg)
![Project](https://img.shields.io/badge/Projet_mode-Hackathon/sprint-orange.svg)
![Session](https://img.shields.io/badge/Session-DFS18-brightgreen.svg)
![Session](https://img.shields.io/badge/Session-DFS19-brightgreen.svg)
![Session](https://img.shields.io/badge/Session-DFS21-brightgreen.svg)
![Session](https://img.shields.io/badge/Session-DFS23-brightgreen.svg)

## Pitch

Presentation rapide du concept de votre projet

<b><i>Sandash</i></b> est un dashboard modulaire et personnalisable. 

Constitué de 9 blocs d'espace à afficher, il permet de mettre en avant les informations les plus importantes pour vous sans réchigner sur les détails. 

Dans cette version MVP (minimum viable product), vous trouverez tous les modules les plus chers à une entreprise afin qu'elle informe les employés en toute transparence. 

---

<b>Les modules actuellement configurés sont : </b>

1. <b>L'horloge</b> : affiche l'heure et la date du jour dans 3 villes aux fuseaux horaires différents successivement (Londres, New York, Tokyo). Ne proposez plus des calls Skype à heures décalées à vos collaborateurs ou clients.


2. <b>Le trombinoscope</b> : présente la photo de chaque employé et son métier, afin de favoriser la cohésion dans l'entreprise.


3. <b>La météo</b> : donne les températures minimale et maximale sur 3 jours. Soyez prévoyant avant d'inviter vos clients à déjeuner en terrasse.


4. <b>Le compteur</b> : suit en temps réel le nombre d'employé actuellement sur site. Ne vous faites plus avoir à amener les croissants quand il n'y a personne, ou au contraire...


5. <b>L'humidité et la température intérieure</b> : avec nos détecteurs précis, apprenez à vous créer davantage de confort au bureau.


6. <b>Le planning</b> : ayez sous les yeux les prochaines réunions pour ne plus les manquer. Nous avons agrémenté ce module avec le nom à fêter du jour, mais surtout l'anniversaire d'une célébrité ce jour-là. Ne soyez plus étonné qu'on vous souhaite votre jour dans les couloirs.

---

<u>Maquette de Sandash</u>
![alt maquette](./images/maquette.png?raw=true "Maquette")

## Stack

Liste des technologies et outils employés dans votre projet
- <b>Technologies :</b>
    - Serveur distant
        - MariaDB
        - PHP 8
        - Symfony 6
        - Python 3
        - pip 3 
        - Flask (https://flask.palletsprojects.com/en/2.0.x/)
        - Dash (https://dash.plotly.com/)
        - dash-iconify (https://docs.iconify.design/icon-components/)
        - dash-bootstrap-components (https://dash-bootstrap-components.opensource.faculty.ai/)
        - requests (https://docs.python-requests.org/en/latest/)

    - Serveur local sur le Raspberry Pi 4
        - SQLite
        

---

- <b>Matériel utilisé :</b>
    - 1 Raspberry Pi 3 sous Raspian pour servir de serveur distant
    - 1 une Freebox mini 4K pour servir de routeur
    - 1 Kit complet Raspberry Pi 4 Modèle B 4G RAM+64G SD avec boitier écran tactile  
    - 1 Kit électronique Freenove RFID Starter Kit pour le badgeage des employé entrant et sortant, ainsi que pour la détection de l'humidité intérieure
    - Un écran LCD HDMI (non tactile)
    - Un clavier sans fil Rii K12
    - Piles, cables jumper, multiprises
    - 1 multiprise 220V + USB  

## Fonctionnement

Les informations récupérées par le Raspberri Pi 4 via le détecteur d'humité et le lecteur de carte RFID sont stockées dans une BDD SQLite. 

Par exemple, le Raspberri Pi 4 peut vérifier ensuite via le protocole MQTT si le tag RFID de l'employé entrant ou sortant est connu dans la BDD du serveur distant. Auquel cas, il met à jour le nombre d'employés présents sur le dashboard.

<u>Schéma sur le fonctionnement de Sandash</u>
![alt mqtt-schema](./images/mqtt-schema.png?raw=true "MQTT protocol schema")

## Team

Liste des membres de l'équipe projet

DFS19A :
- Gaëlle Payet 
- Olivier Sonrel

DFS21A :
- François De Saporta
- Mouaz Saadaoui

DFS23C :
- Pablo Routhier
- Mélodie Strzempek

## Demo

Lien vers une vidéo de démonstration du produit fini
