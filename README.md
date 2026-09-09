 ## Conception et  Déploiement d'une Application Conteneurisée Haute Disponibilité:
 ### Comparatif Docker Swarm vs Kubernetes (GitOps & Monitoring)


#### 1. objectif du projet

L'objectif global de ce projet est de comparer deux orchestrateurs de conteneurs : D
ocker Swarm (natif à Docker), reconnu pour sa légèreté et sa simplicité, et Kubernetes, réputé pour sa robustesse et son adaptabilité à l'écosystème Cloud-Native.  Pour mettre en oeuvre cette étude comparative, nous allons  procéder comme suit.

- La mise en oeuvre d'un  pipeline Devops  permettant d'automatiser provisionnement des serveurs et synchronisation continue des déploiements via Argo CD

- La mise en place d'un  système de monitoring   pour suivre la santé et les performance ses infrastruceure  grâce à Prometheus & Grafana.



#### 2. Architecture Globale du Projet

![image](https://www.plantuml.com/plantuml/svg/ZLHHRjj64FtNAGOkqCW8X42kqxhzA4AHkp8HIZ98oa6X-cD5ZjY5g5rYkLHi53v0_dk9_FS6kbY7QzDY8zIe850GzytCU_DczaDjXR7DhXpKMwagOSGErYBR5aOtAlTrgGrynzsdXr0wnyG-b0W6CojKKMBlDC2DQ4gRuhtrIbce7IeB6JtG30PlO3GQGN3umiDvc8QBEGGi0N-nZDWoJjh3NgQAc8ZYbL9nzsvomlc2N_BB7dIkyrCKc_3tVD93SLtcQ4wp-Vm7lzy1N-yghKZJQKgFUtmy65XfYRGN-zTXolnq6JEOHek95p4uDk7cy5SAqp05dytJs8kS_cVLSDO3d57YAtx5tyEV0u2LJs8WqOt943xXMbGL3FTZ-1xs5-Vm5WATRT5iP8btBJh9ZAni3VcRK6sCgArfCjiOXE6jA8nGbW8zLSjrYUSkO2QKt61jiOQFLpMT-bfjP563PmeDVd0tUEoSPFFRC5xCvsn62i1p0ZgdICAtnxz0TFWoPJ7bd7jfo67un1MIpyBipaacP_ndzfEJgLgLPpUQY42ErA-lUonrLQ6Rg7TmVVZRufc30coSSmGtUYzhgPLoiAF6joyQkv2kmkriJCH8D7NTk44X7XuBVkJZ5oHrvPafKuLKU7TyxwY_X0yZ54Jal0CyVbFgWafzqcRxloj1hnJvO55XOshuVBHzz6lh--zgU2qQYn38ccPJhcKfxU4hzIamGYgOKRKUg-xv-5zUJbxtSa8ww9V5Dt6OCF2ZnJ8OjPxUCXX-RDPe55fiXsSgxQAgMs-PHsjvvPJIzsNE_R8XYmtqeeOpgUIM_hTXmINZ0Nzkq2fKXS6wJPoWsSiCQrBExYjTIqks0zvJBjL9NGLObVgX7OKsv4RdBNoAjSFkn-_s5_GwrcKfLG7BAXTKlekTKHkjDkr9OeajHT9uxT3-WOrJPiI6R7VmnoTHgsv5O4Ish5wLTaSjJ1vK1gsjKZLuj29caTVUZabtQIGGX37pK_PqH_xxRd2bJgUupKzBG_hbqowuIJsDFPAcWDxk_-RDei47L7cpA_y1)

Le projet est divisé en deux environnements distincts :

- Environnement A (Docker Swarm) :

        Provisionnement automatisé de deux machines virtuelles Ubuntu via Vagrant / Ansible.

        Configuration d'un cluster Swarm (1 Manager, 1 Worker) avec des containtes de placement et gestion de la haute disponibilité (Drain mode).

- Environnement B (Kubernetes / Minikube) :

        Déploiement d'un cluster local ou distant.

        Gestion des manifestes Kubernetes (Deployments, Services, Ingress).

        Automatisation des déploiements via Argo CD (GitOps).

        Supervision globale via Prometheus et Grafana.


#### 3. Étapes Détaillées de Réalisation
Étape 0 : Préparation de l'Application Cible

    Mission : Développer ou packager une application web simple (ex: une page HTML/Python Flask ou Node.js) qui affiche un message d'accueil (Welcome BDCC V1), l'adresse IP du conteneur (pour voir l'équilibrage de charge) et un compteur.

    Livrables :

        Un dépôt Git structuré.

        Deux tags d'images Docker sur votre Docker Hub : votre-user/webapp:v1 et votre-user/webapp:v2.

Étape 1 : Partie 1 - Infrastructure Légère avec Docker Swarm

    Fonctionnalités à implémenter :

        Provisionnement automatisé : Utiliser Vagrant et un script Ansible pour lancer deux machines virtuelles Ubuntu Server, configurer le réseau local, et installer automatiquement Docker Engine.

        Initialisation du Cluster : Configurer la VM1 en tant que Manager et la VM2 en tant que Worker (docker swarm init et docker swarm join).

        Déploiement et Contraintes : Déployer le service webapp en appliquant des contraintes de placement (ex: forcer le service à tourner uniquement sur le worker avec une limite de mémoire de 1 Go, comme vu à l'étape 17 du TP).

        Mise à l'échelle (Scaling) et Rolling Update :

            Augmenter le nombre de réplicas à 5.

            Mettre à jour l'image vers la version v2 (webapp:v2) sans coupure de service, puis tester le retour en arrière (docker service rollback).

        Résilience (Drain Mode) : Passer le nœud worker en mode drain pour observer le déplacement automatique des conteneurs vers le manager (haute disponibilité).

Étape 2 : Partie 2 - Migration vers Kubernetes & Approche GitOps (Argo CD)

    Fonctionnalités à implémenter :

        Démarrage du Cluster : Lancer un cluster Kubernetes local (via Minikube ou Kind).

        Manifestes Kubernetes purs : Rédiger les fichiers YAML :

            deployment.yaml (pour gérer les réplicas de la webapp).

            service.yaml (de type NodePort ou LoadBalancer).

            ingress.yaml (pour l'accès externe).

        Intégration d'Argo CD (GitOps) :

            Installer Argo CD sur le cluster Kubernetes.

            Configurer une application Argo CD pointant vers votre dépôt Git (où se trouvent vos fichiers YAML).

            Test du flux GitOps : Modifier le nombre de réplicas ou passer à la version v2 directement dans le fichier YAML sur Git, commiter, et observer Argo CD synchroniser et appliquer automatiquement les changements sur le cluster en temps réel.

Étape 3 : Partie 3 - Monitoring et Observabilité (Prometheus & Grafana)

    Fonctionnalités à implémenter :

        Installation de la pile de monitoring : Utiliser Helm pour installer la kube-prometheus-stack sur le cluster Kubernetes.

        Collecte des métriques : Configurer Prometheus pour collecter l'utilisation du CPU, de la mémoire et le trafic réseau des pods de la webapp.

        Création du Tableau de Bord (Dashboard Grafana) :

            Accéder à l'interface de Grafana.

            Créer ou importer un dashboard personnalisé pour visualiser en direct les performances de l'application lors de tests de charge (générés par exemple avec l'outil ab ou wrk).

#### 4. Structure Recommandée du Projet (sur Git)

Organisez votre dépôt de cette manière pour qu'il soit propre et professionnel :
Plaintext

```Bash

/mon-projet-cloud
│
├── README.md                 
├── application/              
│   ├── app.py (ou server.js)
│   └── Dockerfile
│
├── part1-docker-swarm/       
│   ├── Vagrantfile
│   └── playbook.yml
│
├── part2-kubernetes/         
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
└── part3-monitoring/         
    └── values-override.yaml 
```


#### 5. Critères de Réussite / Démonstration pour la Soutenance

Pour valider le projet lors d'une présentation, vous devez être capable de montrer :

    L'automatisation Swarm : Les VM se lancent seules via Vagrant/Ansible, le cluster est actif et réagit au mode drain.

    Le fonctionnement d'Argo CD : Un changement de code ou de configuration dans Git se répercute visuellement et instantanément sur le cluster Kubernetes via l'interface d'Argo CD.

    Le Monitoring en action : Générer de la charge sur l'application web et voir les courbes de consommation CPU/RAM s'affoler en temps réel sur le dashboard Grafana.