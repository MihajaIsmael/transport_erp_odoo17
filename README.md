# 🚚 ERP Transport Terrestre – Odoo 17

## ERP Transport Terrestre + SOA + BI + Data Mining + IA

Projet **académique** visant la conception et la mise en œuvre d’un **système ERP orienté services** pour la gestion du transport terrestre. Le projet s’appuie sur **Odoo 17** comme cœur transactionnel et intègre des dimensions **Business Intelligence, Data Mining et Intelligence Artificielle** pour l’aide à la décision.

---

## 👥 Équipe du projet (Groupe 3)

* **ANDRIANARIVONY Heritsihoarana Kevin**
* **RAKOTOZANANY Andry Nantenaina**
* **RANARIMANANA Liana Miotisoa**
* **RAVALOMANDA Andrianarimihaja Ismael**

---

## 1️⃣ Introduction et contexte

### 1.1 Présentation du domaine

Le **transport terrestre** joue un rôle central dans :

* la mobilité des passagers
* la logistique des marchandises
* le développement économique

Cependant, de nombreuses entreprises du secteur font face à :

* une mauvaise gestion des réservations
* un suivi insuffisant des véhicules
* une absence d’analyse décisionnelle
* un manque d’automatisation des processus

### 1.2 Problématique

**Comment concevoir un système intégré permettant :**

* la gestion opérationnelle du transport
* l’analyse décisionnelle basée sur les données
* l’automatisation du reporting
* l’amélioration continue des performances

### 1.3 Objectifs du projet

#### 🎯 Objectif général

Concevoir un **ERP de transport terrestre orienté services**, intégrant des capacités de **BI, Data Mining et IA**.

#### 🎯 Objectifs spécifiques

* Mettre en place un ERP transactionnel
* Assurer la qualité et la fiabilité des données
* Concevoir un Data Warehouse
* Développer des tableaux de bord décisionnels
* Intégrer une assistance basée sur l’IA

---

## 2️⃣ Analyse des besoins

### 2.1 Identification des acteurs

* Administrateur
* Agent de réservation
* Responsable transport
* Chauffeur
* Client
* Direction

### 2.2 Processus métier principaux

#### 🚗 Gestion de la flotte

* Enregistrement des véhicules
* Suivi de la maintenance
* Affectation des véhicules

#### 🛣️ Gestion des trajets

* Création des lignes
* Planification des horaires
* Affectation des chauffeurs

#### 👥 Gestion des clients

* Réservation de billets
* Gestion du transport de marchandises

#### 💰 Gestion financière

* Paiements
* Facturation
* Suivi des revenus

### 2.3 Besoins fonctionnels

Le système doit permettre :

* ✔ gestion des utilisateurs et des rôles
* ✔ gestion des véhicules
* ✔ gestion des chauffeurs
* ✔ gestion des trajets
* ✔ gestion des réservations
* ✔ gestion de la maintenance
* ✔ facturation
* ✔ génération de rapports

### 2.4 Besoins non fonctionnels

* Sécurité
* Performance
* Fiabilité
* Scalabilité
* Traçabilité

---

## 3️⃣ Architecture globale du système

### 3.1 Architecture multi‑couches

* **Couche présentation** : Interface utilisateur Odoo
* **Couche métier** : Services ERP
* **Couche données** : Base transactionnelle + Data Warehouse

### 3.2 Architecture SOA

Services exposés via **API REST** :

* Service réservation
* Service flotte
* Service maintenance
* Service facturation
* Service reporting

---

## 4️⃣ Conception ERP et règles de gestion

### 4.1 Modules ERP

#### Module Gestion des véhicules

**Fonctions** :

* Ajouter un véhicule
* Consulter l’historique de maintenance
* Suivre l’utilisation

**Règles de gestion** :

* Un véhicule doit être validé avant affectation
* Maintenance obligatoire selon le kilométrage

#### Module Gestion des chauffeurs

**Fonctions** :

* Gestion des informations
* Planning de travail
* Affectation aux véhicules

**Règles** :

* Permis valide obligatoire
* Un chauffeur ne peut conduire qu’un seul véhicule à la fois

#### Module Gestion des trajets

* Création des lignes
* Planification des horaires
* Affectation des ressources

#### Module Réservation

* Réservation de sièges
* Gestion du transport de marchandises
* Annulation des réservations

#### Module Facturation

* Génération des factures
* Paiement
* Historisation des transactions

### 4.2 Journalisation et traçabilité

* Historique des modifications
* Logs des actions utilisateurs
* Audit système

---

## 5️⃣ Gouvernance et qualité des données

* Normalisation des données
* Validation des champs obligatoires
* Détection des incohérences et doublons
* Séparation des données transactionnelles et analytiques

---

## 6️⃣ Business Intelligence

### 6.1 Data Warehouse

Modèle dimensionnel en **étoile** :

**Table de faits** :

* Faits_Transport

**Dimensions** :

* Temps
* Véhicule
* Chauffeur
* Trajet
* Client

### 6.2 Processus ETL

* Extraction depuis l’ERP
* Transformation et nettoyage des données
* Chargement du Data Warehouse

### 6.3 Tableaux de bord

* **Stratégique** : rentabilité globale, évolution du chiffre d’affaires
* **Tactique** : performance des lignes, coûts de maintenance
* **Opérationnel** : taux de remplissage, suivi quotidien des trajets

---

## 7️⃣ Data Mining

* Analyse exploratoire des données
* Analyse de la saisonnalité
* Segmentation et clustering des clients
* Détection d’anomalies
* Analyse des coûts de maintenance
* Étude des corrélations (saison / demande)

---

## 8️⃣ Reporting assisté par IA

* Génération automatique d’insights
* Narration décisionnelle automatique
* Recommandations : nouveaux trajets, maintenance préventive

---

## 9️⃣ Technologies utilisées

* **ERP** : Odoo 17
* **Base de données** : PostgreSQL
* **BI** : Power BI / Metabase
* **Data Mining & IA** : Python, Pandas, Scikit‑learn
* **SOA** : API REST
* **Conteneurisation** : Docker / Docker Compose

---

## 🔧 1️⃣0️⃣ Installation de l’application

### Prérequis

Avant de commencer, assurez-vous d’avoir installé :
- Docker
- Docker Compose
- Git

> L’utilisation de Docker permet d’éviter toute installation manuelle d’Odoo ou de PostgreSQL.

---

### Étape 1 : Clonage du projet

```bash
git clone https://github.com/MihajaIsmael/transport_erp_odoo17.git
cd transport_erp_odoo17
```

---

### Étape 2 : Lancement de l’environnement Odoo

```bash
docker compose up -d
```

Cette commande lance :
- le serveur **Odoo 17**
- la base de données **PostgreSQL**
- le module personnalisé `gestion_transport`

---

### Étape 3 : Accès à l’interface Odoo

- URL : http://localhost:8069
- Créer une nouvelle base de données
- Se connecter avec le compte administrateur

---

### Étape 4 : Installation du module Transport

1. Activer le **mode développeur** dans Odoo
2. Aller dans **Apps**
3. Cliquer sur **Mettre à jour la liste des applications**
4. Rechercher le module **Gestion Transport**
5. Installer le module

Une fois installé, les menus et fonctionnalités du module apparaissent dans l’interface Odoo.

---

## 📌 Contexte académique

Projet réalisé dans un cadre **universitaire**, servant de support à l’analyse, la conception et la démonstration d’un **ERP décisionnel orienté données**.

---

## 📄 Licence

Projet à usage pédagogique et académique uniquement.
