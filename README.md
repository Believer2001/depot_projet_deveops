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

   

Étape 1 : Partie 1 - Infrastructure Légère avec Docker Swarm

    Fonctionnalités implémentées:

        Provisionnement automatisé : 

        Initialisation du Cluster 

        Déploiement et Contraintes 

        Mise à l'échelle (Scaling) et Rolling Update :


        Résilience (Drain Mode)

Étape 2 : Partie 2 - Migration vers Kubernetes & Approche GitOps (Argo CD)

    Fonctionnalités implémentées :

        Démarrage du Cluster

        Manifestes Kubernetes purs 

        Intégration d'Argo CD (GitOps) :

            

Étape 3 : Partie 3 - Monitoring et Observabilité (Prometheus & Grafana)

    Fonctionnalités à implémenter :

        Installation de la pile de monitoring :

        Collecte des métriques :

        Création du Tableau de Bord (Dashboard Grafana) :

 