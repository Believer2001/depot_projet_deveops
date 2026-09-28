# Conception et Déploiement d'une Application Conteneurisée Haute Disponibilité

### De l'orchestration légère (Docker Swarm) à l'écosystème Cloud-Native (Kubernetes, GitOps & Monitoring)

---

## 📋 1. Objectif du Projet
L'objectif de ce projet est de concevoir, déployer et administrer une application web conteneurisée à travers deux approches d'orchestration complémentaires :
* **Première étape (Swarm)** : Mise en place d'une infrastructure conteneurisée rapide et légère avec **Docker Swarm**.
* **Seconde étape (Kubernetes)** : Migration vers un environnement de production Cloud-Native automatisé via **Argo CD (GitOps)** et supervisé par **Prometheus & Grafana**.

---

## 🏗️ 2. Architecture Globale du Projet

![image](https://www.plantuml.com/plantuml/svg/ZLHHRjj64FtNAGOkqCW8X42kqxhzA4AHkp8HIZ98oa6X-cD5ZjY5g5rYkLHi53v0_dk9_FS6kbY7QzDY8zIe850GzytCU_DczaDjXR7DhXpKMwagOSGErYBR5aOtAlTrgGrynzsdXr0wnyG-b0W6CojKKMBlDC2DQ4gRuhtrIbce7IeB6JtG30PlO3GQGN3umiDvc8QBEGGi0N-nZDWoJjh3NgQAc8ZYbL9nzsvomlc2N_BB7dIkyrCKc_3tVD93SLtcQ4wp-Vm7lzy1N-yghKZJQKgFUtmy65XfYRGN-zTXolnq6JEOHek95p4uDk7cy5SAqp05dytJs8kS_cVLSDO3d57YAtx5tyEV0u2LJs8WqOt943xXMbGL3FTZ-1xs5-Vm5WATRT5iP8btBJh9ZAni3VcRK6sCgArfCjiOXE6jA8nGbW8zLSjrYUSkO2QKt61jiOQFLpMT-bfjP563PmeDVd0tUEoSPFFRC5xCvsn62i1p0ZgdICAtnxz0TFWoPJ7bd7jfo67un1MIpyBipaacP_ndzfEJgLgLPpUQY42ErA-lUonrLQ6Rg7TmVVZRufc30coSSmGtUYzhgPLoiAF6joyQkv2kmkriJCH8D7NTk44X7XuBVkJZ5oHrvPafKuLKU7TyxwY_X0yZ54Jal0CyVbFgWafzqcRxloj1hnJvO55XOshuVBHzz6lh--zgU2qQYn38ccPJhcKfxU4hzIamGYgOKRKUg-xv-5zUJbxtSa8ww9V5Dt6OCF2ZnJ8OjPxUCXX-RDPe55fiXsSgxQAgMs-PHsjvvPJIzsNE_R8XYmtqeeOpgUIM_hTXmINZ0Nzkq2fKXS6wJPoWsSiCQrBExYjTIqks0zvJBjL9NGLObVgX7OKsv4RdBNoAjSFkn-_s5_GwrcKfLG7BAXTKlekTKHkjDkr9OeajHT9uxT3-WOrJPiI6R7VmnoTHgsv5O4Ish5wLTaSjJ1vK1gsjKZLuj29caTVUZabtQIGGX37pK_PqH_xxRd2bJgUupKzBG_hbqowuIJsDFPAcWDxk_-RDei47L7cpA_y1)

Le projet se décompose en deux phases distinctes :
* **Phase 1 : Infrastructure Légère avec Docker Swarm** (Provisionnement Vagrant/Ansible, gestion du cluster, résilience et scaling).
* **Phase 2 : Écosystème Cloud-Native avec Kubernetes** (Déploiement de manifestes, automatisation GitOps, et observabilité).

---

##  3. Étapes de Réalisation

###  Étape 0 : Préparation de l'Application Cible
Développement et conteneurisation de l'application web 

---

### 🐳 Étape 1 : Phase 1 - Orchestration avec Docker Swarm
* **Provisionnement automatisé** des machines virtuelles via Vagrant et VMware   via un fichier `Vagrantfile`.

* **Initialisation du Cluster** (Manager & Worker) et mise en œuvre des contraintes de placement via `Ansible`

* **Gestion du cycle de vie** : Scaling, Rolling Updates, et tests de résilience (mode Drain).

### Étape 2 : Phase 2 - Migration vers Kubernetes & Approche GitOps (Argo CD)

* **Provisionnement automatisé**  des  machines virtuellles via Vagrant et Vmware via un  fichier `Vagrantfile`.

* **Démarrage et configuration du cluster Kubernetes** via `Ansible`


* **Intégration du dépôt Git avec Argo CD** pour assurer un déploiement continu et déclaratif.

### Étape 3 : Phase 3 - Observabilité et Monitoring (Prometheus & Grafana)


Installation des outils de supervision sur le cluster Kubernetes :
```bash

ansible-galaxy collection install community.kubernetes

```
* Déploiement de la pile de monitoring et configuration des sources de données pour suivre les performances en temps réel.

* Tableau de Bord Grafana :

### Conclusion
Ce projet a permis la mise en oeuvre de  deux grands paradigmes de l'orchestration de conteneurs : la simplicité et l'agilité de Docker Swarm pour des architectures rapides, combinées à la robustesse, l'automatisation GitOps (Argo CD) et l'observabilité avancée (Prometheus/Grafana) offertes par Kubernetes pour des environnements de production scalables.

 