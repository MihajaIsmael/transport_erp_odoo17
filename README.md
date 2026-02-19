# 🚚 Transport ERP – Odoo 17

Projet **ERP de gestion du transport terrestre** basé sur **Odoo 17**, conçu dans un cadre **académique**. Ce projet vise à démontrer la mise en place d’un module métier personnalisé dans Odoo, intégrant des notions d’architecture modulaire, de SOA, de BI et ouvrant la voie à des usages Data Mining et IA.

---

## 🎯 Objectifs du projet

- Mettre en œuvre un **ERP Transport** sur Odoo 17
- Concevoir un **module personnalisé** (`gestion_transport`)
- Utiliser **Docker** pour simplifier l’installation et l’exécution
- Appliquer les bonnes pratiques de développement Odoo
- Servir de **support pédagogique / démonstration académique**

---

## 🧱 Architecture du projet

```
transport_erp_odoo17/
├── addons/
│   └── gestion_transport/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       ├── views/
│       ├── security/
│       └── data/
├── docker-compose.yml
├── .gitignore
└── README.md
```

### 📦 Module `gestion_transport`

Le module `gestion_transport` contient la logique métier liée au transport terrestre, notamment :
- gestion des entités métier (transport, véhicules, chauffeurs, etc.)
- vues et menus Odoo (XML)
- règles de sécurité (droits d’accès)

---

## ⚙️ Prérequis

- Docker
- Docker Compose
- Git

> Aucune installation locale d’Odoo ou de PostgreSQL n’est requise grâce à Docker.

---

## 🚀 Installation et démarrage

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/MihajaIsmael/transport_erp_odoo17.git
cd transport_erp_odoo17
```

### 2️⃣ Lancer l’environnement Docker

```bash
docker compose up -d
```

### 3️⃣ Accéder à Odoo

- URL : http://localhost:8069
- Créer une base de données
- Activer le **mode développeur**
- Installer le module **Gestion Transport**

---

## 🧪 Environnement de développement

- **Odoo** : 17.x
- **Langage** : Python
- **Base de données** : PostgreSQL
- **Orchestration** : Docker / Docker Compose

---

## 📊 Axes d’évolution prévus

- Planning et affectation des véhicules
- Gestion des chauffeurs et itinéraires
- Génération de rapports (PDF, statistiques)
- Intégration BI / tableaux de bord
- Exposition de services (SOA / API)
- Exploitation des données (Data Mining, IA)

---

## 📚 Contexte académique

Ce projet est réalisé dans un **cadre académique** et a pour but de :
- illustrer le développement de modules Odoo
- démontrer une architecture ERP orientée métier
- servir de base à une soutenance ou démonstration technique

---

## 👤 Auteurs

**Kevin Heritsihoarana ANDRIANARIVONY**
**Andry Nantenaina RAKOTOZANANY**
**Liana Miotisoa RANARIMANANA**
**Ismael A. RAVALOMANDA** 
Projet académique – Odoo 17

---

## 📄 Licence

Projet à usage pédagogique et académique.
