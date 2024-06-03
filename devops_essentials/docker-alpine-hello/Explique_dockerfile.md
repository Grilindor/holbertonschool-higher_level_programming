## Docker
- Est une plateforme open source qui automatise le déploiement d'applications dans des conteneurs logiciels. Pour bien comprendre Docker, voici les concepts de base expliqués simplement :

## Qu'est-ce qu'un conteneur ?
- Un conteneur est une unité standard de logiciel qui emballe le code et toutes ses dépendances pour que l'application fonctionne rapidement et de manière fiable d'un environnement informatique à un autre. Il est plus léger qu'une machine virtuelle (VM) car il partage le noyau du système d'exploitation avec d'autres conteneurs, mais reste isolé au niveau des processus et du réseau.

## Pourquoi utiliser Docker ?
- Portabilité : Les conteneurs Docker peuvent s'exécuter sur n'importe quel environnement, que ce soit sur un ordinateur portable, un serveur ou dans le cloud.
- Isolation : Chaque application fonctionne dans son propre conteneur, sans interférer avec les autres.
- Efficacité : Les conteneurs sont plus légers et démarrent plus rapidement que les machines virtuelles.
- Facilité de gestion : Docker simplifie la configuration, le déploiement et la gestion des applications.
## Concepts de base
- Images Docker : Une image est un modèle de lecture seule utilisé pour créer des conteneurs. Elle contient tout ce dont votre application a besoin pour fonctionner, y compris le code, les bibliothèques, les variables d'environnement et les fichiers de configuration.

- Conteneurs Docker : Un conteneur est une instance d'une image. Vous pouvez créer, démarrer, arrêter, déplacer ou supprimer un conteneur à l'aide de la CLI (Command Line Interface) de Docker.

- Dockerfile : Un fichier texte qui contient une série d'instructions pour assembler une image Docker. Il définit comment créer une image à partir d'un environnement de base, installer les dépendances nécessaires, copier les fichiers, et définir les commandes à exécuter.

- Docker Hub : Un registre en ligne public où les utilisateurs peuvent créer, tester, stocker et distribuer des conteneurs Docker. Il propose des images prêtes à l'emploi pour de nombreux logiciels.

## Comment utiliser Docker ?
- Voici un guide rapide pour débuter avec Docker :

## 1.Installer Docker :

- Téléchargez et installez Docker Desktop depuis le site officiel (disponible pour Windows, Mac et Linux).
## 2.Créer une Dockerfile :

- Dans le répertoire de votre projet, créez un fichier nommé Dockerfile.

- Ajoutez les instructions nécessaires pour assembler votre image. Par exemple, pour une application Node.js :

```
# Utilise une image de base officielle de Node.js
FROM node:14

# Crée un répertoire de travail pour l'application
WORKDIR /app

# Copie les fichiers package.json et package-lock.json
COPY package*.json ./

# Installe les dépendances
RUN npm install

# Copie le reste des fichiers de l'application
COPY . .

# Expose le port sur lequel l'application écoute
EXPOSE 3000

# Définit la commande à exécuter lorsque le conteneur démarre
CMD ["node", "app.js"]
```
## 3.Construire l'image :

- Ouvrez un terminal et placez-vous dans le répertoire où se trouve votre Dockerfile.
- Exécutez la commande : docker build -t nom-de-votre-image .

## 4.Exécuter le conteneur :
Pour créer et démarrer un conteneur à partir de l'image, utilisez la commande :
```
bash

docker run -d -p 3000:3000 nom-de-votre-image
```
- Cette commande démarre le conteneur en mode détaché (-d) et mappe le port 3000 du conteneur au port 3000 de votre machine

## Commandes utiles de Docker

- Lister les images : docker images
- Lister les conteneurs en cours d'exécution : docker ps
- Arrêter un conteneur : docker stop ID_du_conteneur
- Supprimer un conteneur : docker rm ID_du_conteneur
- Supprimer une image : docker rmi nom-de-l'image

## Conclusion
Docker est un outil puissant pour simplifier le développement, le déploiement et la gestion des applications. En isolant les applications dans des conteneurs, il garantit que le code fonctionne de manière cohérente dans différents environnements. En maîtrisant les concepts de base et les commandes essentielles, vous serez bien équipé pour commencer à utiliser Docker dans vos projets.

- Pour mieux comprendre Docker, un schéma visuel peut être très utile. Voici un schéma simple qui illustre les concepts clés de Docker :
```
                   +---------------------------+
                   |       Docker Hub          |
                   |                           |
                   | [ Images d'applications ] |
                   +---------------------------+
                                |
                                |
                                v
+-----------------------------+         +--------------------------------+
|                             |         |                                |
|     Docker Engine           |<------>|   Docker CLI (Command Line)    |
|                             |         |                                |
|                             |         +--------------------------------+
|                             |
|   +----------------------+  |
|   |  Image 1             |  |
|   +----------------------+  |
|   |  Image 2             |  |
|   +----------------------+  |
|   |  ...                 |  |
|   +----------------------+  |
|                             |
|   +----------------------+  |
|   |  Conteneur 1         |  |
|   |----------------------|  |
|   |  Instance de Image 1 |  |
|   +----------------------+  |
|                             |
|   +----------------------+  |
|   |  Conteneur 2         |  |
|   |----------------------|  |
|   |  Instance de Image 2 |  |
|   +----------------------+  |
|                             |
+-----------------------------+
```

## Explications du schéma

# 1. Docker Hub :

- 1.Rôle : C'est un registre en ligne où sont stockées les images Docker. Vous pouvez y trouver des images d'applications prêtes à l'emploi, télécharger des images, ou y déposer vos propres images pour les partager avec la communauté.
- 2.Fonctionnement : Vous pouvez tirer (pull) des images depuis Docker Hub ou pousser (push) vos images vers Docker Hub.

# 2.Docker Engine :

- 1.Rôle : C'est le cœur de Docker, responsable de la gestion des images et des conteneurs. Il s'occupe de l'exécution des commandes Docker, du téléchargement des images, et de la création et de la gestion des conteneurs.
- 2.Images : Ce sont les modèles de conteneurs. Une image est un paquet statique qui contient tout le nécessaire pour exécuter une application (code, dépendances, configurations, etc.).
- 3.Conteneurs : Ce sont les instances en cours d'exécution des images. Chaque conteneur est isolé et fonctionne indépendamment des autres conteneurs et de l'hôte.

# 3.Docker CLI (Command Line Interface) :

- 1.Rôle : C'est l'interface en ligne de commande que vous utilisez pour interagir avec Docker Engine. Vous pouvez exécuter des commandes pour créer, gérer et déployer des conteneurs.
- 2.Fonctionnement : À l'aide de commandes comme docker build, docker run, docker stop, vous contrôlez Docker Engine et manipulez les images et conteneurs

## Comment le tout fonctionne ensemble

# 1.Créer une Image :

- 1.Vous écrivez un Dockerfile qui contient les instructions pour construire une image.
- 2.Utilisez la commande docker build pour créer l'image à partir du Dockerfile.

# 2.Pousser et tirer des Images :
- 1.Utilisez docker push pour envoyer une image vers Docker Hub.
- 2.Utilisez docker pull pour télécharger une image depuis Docker Hub vers votre Docker Engine



# 3.Créer et exécuter des Conteneurs :

- 1.Utilisez docker run pour créer et démarrer un conteneur à partir d'une image.
- 2.Les conteneurs s'exécutent de manière isolée mais peuvent être configurés pour communiquer entre eux si nécessaire.

## Conclusion
Ce schéma montre comment les différentes composantes de Docker interagissent pour vous permettre de créer, partager et exécuter des applications dans des environnements isolés et portables. Cela simplifie considérablement le processus de développement et de déploiement, en garantissant que votre application fonctionne de la même manière, que ce soit en développement, en test ou en production
