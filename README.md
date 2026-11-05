# Domain Intelligence 

Outil Python de **veille passive sur un domaine (Passive Domain Intelligence / OSINT)**. Il rassemble des informations publiquement accessibles sur un domaine, découvre des noms d'hôtes associés à partir de sources passives, observe certains enregistrements DNS et caractéristiques TLS/HTTP, puis génère plusieurs rapports exploitables.

> **Important :** cet outil fournit des observations techniques, pas une preuve de propriété ou de contrôle d'un domaine. Les résultats peuvent être incomplets, obsolètes ou dépendre des limites des sources tierces.

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Fonctionnement général](#fonctionnement-général)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Rapports générés](#rapports-générés)
- [Historique et suivi des changements](#historique-et-suivi-des-changements)
- [Sources de données](#sources-de-données)
- [Structure du projet](#structure-du-projet)
- [Interprétation des résultats](#interprétation-des-résultats)
- [Dépannage](#dépannage)
- [Sécurité et usage responsable](#sécurité-et-usage-responsable)
- [Limites connues](#limites-connues)
- [Améliorations possibles](#améliorations-possibles)
- [Licence](#licence)

## Fonctionnalités

### 1. Collecte d'informations sur le domaine

- Normalisation du nom de domaine fourni.
- Consultation WHOIS lorsque le serveur et le registre le permettent.
- Consultation des données RDAP via le service public `rdap.org`.
- Collecte de plusieurs familles d'enregistrements DNS :
  - `A` et `AAAA`
  - `NS`
  - `MX`
  - `TXT`
  - `CNAME`
  - `SOA`
  - `CAA`
  - `DS` et `DNSKEY`
  - `SRV`
- Observation de la présence d'informations DNSSEC (`DS` / `DNSKEY`), sans validation cryptographique complète.
- Observation des certificats TLS présentés par les hôtes accessibles.
- Requête HTTP de base et collecte d'informations telles que le code de statut, les redirections et certains en-têtes.

### 2. Découverte passive de sous-domaines

Le programme interroge des sources publiques ou des services tiers pour identifier des noms d'hôtes associés au domaine racine.

Les résultats sont normalisés, filtrés pour rester dans le périmètre du domaine et dédupliqués.

Sources configurables :

- Certificate Transparency via `crt.sh`
- HackerTarget
- VirusTotal
- SecurityTrails
- urlscan.io

La disponibilité de chaque source dépend de son service, de ses quotas, de ses conditions d'accès et de sa configuration.

### 3. Cartographie et visualisation

Le projet génère une carte interactive permettant d'explorer les relations entre :

- Le domaine principal
- Les sous-domaines découverts
- Les adresses IP
- Les adresses IPv6

La cartographie utilise la bibliothèque PyVis et peut être consultée depuis un navigateur.

### 4. Génération de rapports

Plusieurs formats d'export sont disponibles :

| Format | Description |
|---|---|
| JSON | Données structurées pour traitement automatisé |
| HTML | Rapport consultable dans un navigateur |
| HTML interactif | Cartographie des hôtes et des adresses IP |
| HTML Timeline | Chronologie des changements observés |
| PDF | Rapport synthétique partageable et imprimable |

### 5. Historique des changements

À chaque exécution, le programme conserve un instantané et compare certaines observations à l'exécution précédente.

Il peut notamment signaler :

- L'apparition de nouveaux sous-domaines.
- La disparition de noms précédemment observés.
- Les modifications d'enregistrements DNS.
- Les changements d'informations TLS.
- Les modifications des observations HTTP.

Une absence dans une collecte ne prouve toutefois pas qu'un service a été supprimé : la source peut être indisponible, avoir changé ses résultats ou limiter les réponses.

---

## Fonctionnement général

Le traitement suit les étapes suivantes :

1. Normalisation du domaine fourni.
2. Collecte des informations WHOIS et RDAP.
3. Collecte des enregistrements DNS.
4. Découverte passive de sous-domaines auprès des sources activées.
5. Filtrage des résultats pour respecter le périmètre du domaine.
6. Résolution DNS des hôtes découverts.
7. Observation TLS et HTTP.
8. Sauvegarde de l'instantané.
9. Comparaison avec l'historique précédent.
10. Génération des rapports JSON, HTML, carte interactive, chronologie et PDF.

Le programme ne cherche pas à exploiter les hôtes. Il ne réalise pas de brute force de sous-domaines, de scan de ports ou de test d'intrusion.

---

## Prérequis

- Python 3.10 ou supérieur recommandé.
- Une connexion Internet.
- Les dépendances Python listées dans `requirements.txt`.
- Facultatif : une clé API VirusTotal.
- Facultatif : une clé API SecurityTrails.

---

## Installation

### 1. Récupérer le projet

Placez les fichiers du projet dans un répertoire local, puis ouvrez un terminal dans ce répertoire.

### 2. Créer un environnement virtuel

**Windows PowerShell :**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS :**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Dépendances utilisées

Exemple de contenu de `requirements.txt` :

```text
requests>=2.32.0
python-whois>=0.9.5
dnspython>=2.7.0
reportlab>=4.2.5
python-dotenv>=1.0.1
pyvis>=0.3.2
```

### 5. Préparer la configuration

Copiez le fichier modèle :

**Windows :**

```powershell
Copy-Item .env.example .env
```

**Linux / macOS :**

```bash
cp .env.example .env
```

Modifiez ensuite le fichier `.env` selon les sources que vous souhaitez activer.

---

## Configuration

Le programme charge les paramètres depuis un fichier `.env` situé dans le répertoire du projet.

Exemple de configuration :

```dotenv
VIRUSTOTAL_API_KEY=
SECURITYTRAILS_API_KEY=

REQUEST_TIMEOUT=15
MAX_SUBDOMAINS=5000
LOG_LEVEL=INFO

ENABLE_CRTSH=true
ENABLE_HACKERTARGET=false
ENABLE_URLSCAN=false
ENABLE_VIRUSTOTAL=true
ENABLE_SECURITYTRAILS=true
```

### Description des variables

| Variable | Description |
|---|---|
| `VIRUSTOTAL_API_KEY` | Clé API VirusTotal |
| `SECURITYTRAILS_API_KEY` | Clé API SecurityTrails |
| `REQUEST_TIMEOUT` | Délai maximal d'attente des requêtes, en secondes |
| `MAX_SUBDOMAINS` | Nombre maximal de sous-domaines conservés ou traités |
| `LOG_LEVEL` | Niveau de journalisation |
| `ENABLE_CRTSH` | Active ou désactive crt.sh |
| `ENABLE_HACKERTARGET` | Active ou désactive HackerTarget |
| `ENABLE_URLSCAN` | Active ou désactive urlscan.io |
| `ENABLE_VIRUSTOTAL` | Active ou désactive VirusTotal |
| `ENABLE_SECURITYTRAILS` | Active ou désactive SecurityTrails |

### Gestion des clés API

Les clés API sont facultatives selon les sources activées.

Bonnes pratiques :

- Ne publiez jamais votre fichier `.env`.
- N'intégrez pas de clé API directement dans le code source.
- Si une clé a été exposée, révoquez-la et générez-en une nouvelle.
- Vérifiez les quotas et les conditions d'utilisation des services.

---

## Utilisation

### Lancer une analyse

Depuis le répertoire du projet :

```bash
python domain_report.py example.com
```

Remplacez `example.com` par le domaine que vous souhaitez examiner et que vous êtes autorisé à analyser.

### Saisie interactive

Si aucun domaine n'est fourni :

```bash
python domain_report.py
```

Le programme peut demander le domaine directement dans le terminal.

### Définir le répertoire de sortie

L'option `--out` permet de choisir où enregistrer les rapports :

```bash
python domain_report.py example.com --out ./rapports
```

### Exemple sous Windows

```powershell
.venv\Scripts\Activate.ps1
python domain_report.py example.com --out .\rapports
```

### Exemple sous Linux / macOS

```bash
source .venv/bin/activate
python domain_report.py example.com --out ./rapports
```

---

## Rapports générés

Le programme produit plusieurs fichiers à partir des données collectées.

### Rapport JSON

Contient les données structurées de l'analyse :

- Domaine principal.
- Informations WHOIS et RDAP.
- Enregistrements DNS.
- Sous-domaines découverts.
- Adresses IP.
- Informations TLS.
- Informations HTTP.
- Sources ayant fourni les observations.

Ce format est adapté à l'intégration avec d'autres outils ou à l'analyse automatisée.

### Rapport HTML

Rapport lisible dans un navigateur présentant les principales informations collectées.

### Carte interactive

La carte permet d'explorer les relations entre les domaines, les sous-domaines et les adresses IP.

Elle est générée avec PyVis.

### Timeline

La chronologie présente les événements enregistrés au fil des analyses :

- Nouveaux sous-domaines.
- Sous-domaines non retrouvés.
- Changements DNS.
- Changements TLS.
- Changements HTTP.

### Rapport PDF

Le PDF fournit une synthèse exploitable pour l'archivage ou le partage.

---

## Historique et suivi des changements

L'historique est conservé localement dans le répertoire `history/`.

Organisation :

```text
history/
├── snapshots/
│   └── example.com.json
└── events/
    └── example.com.jsonl
```

### Snapshots

Le dossier `snapshots/` contient le dernier état collecté pour chaque domaine.

Chaque nouveau lancement met à jour l'instantané correspondant.

### Events

Le dossier `events/` contient les événements successifs au format JSON Lines.

Chaque ligne représente un événement distinct.

### Première exécution

La première exécution sert de référence initiale.

Elle ne permet pas de déduire des changements antérieurs à la date de cette collecte.

### Exécutions suivantes

Les comparaisons peuvent concerner :

- Les noms d'hôtes découverts.
- Les données DNS collectées.
- Les observations TLS.
- Les observations HTTP.

### Précautions

- Une donnée absente peut être due à une panne, un quota ou un délai d'attente.
- Une différence de réponse peut être temporaire.
- L'historique n'est pas une archive DNS exhaustive.
- L'historique est local à l'installation : sauvegardez `history/` pour le conserver.
- Évitez de lancer plusieurs analyses simultanées du même domaine dans le même répertoire d'historique.

---

## Sources de données

| Source | Type d'information | Remarques |
|---|---|---|
| WHOIS | Informations d'enregistrement | Données parfois masquées ou indisponibles |
| RDAP | Informations structurées d'enregistrement | Dépend du registre et du service RDAP |
| DNS | Enregistrements publiés dans le DNS | Dépend du résolveur et du moment |
| crt.sh | Certificats Certificate Transparency | Les certificats peuvent être anciens |
| HackerTarget | Découverte passive de sous-domaines | Dépend des limites du service |
| VirusTotal | Informations passives sur le domaine | Clé API et quotas éventuels |
| SecurityTrails | Informations DNS et sous-domaines | Clé API et quotas éventuels |
| urlscan.io | Observations issues d'analyses web | Dépend des scans disponibles |

Les fournisseurs peuvent modifier leurs API, leurs formats de réponse, leurs quotas ou leurs conditions d'accès.

Une erreur sur une source n'implique pas nécessairement l'échec de l'ensemble de l'analyse.

---

## Structure du projet

Structure indicative :

```text
domain-intelligence/
│
├── domain_report.py
├── requirements.txt
├── .env.example
├── .env
├── README.md
│
├── rapports/
│   ├── ... fichiers JSON ...
│   ├── ... fichiers HTML ...
│   ├── ... fichiers PDF ...
│   └── ... carte et timeline ...
│
└── history/
    ├── snapshots/
    └── events/
```

| Élément | Rôle |
|---|---|
| `domain_report.py` | Script principal : collecte, comparaison et exports |
| `requirements.txt` | Dépendances Python |
| `.env.example` | Modèle de configuration |
| `.env` | Configuration locale et clés API |
| `README.md` | Documentation du projet |
| `rapports/` | Rapports générés |
| `history/` | Instantanés et événements historiques |

---

## Interprétation des résultats

### Sous-domaines découverts

Un nom retourné par une source passive indique qu'il a été observé dans cette source.

Cela ne signifie pas nécessairement que :

- Le nom est encore actif.
- Le service répond actuellement.
- Le domaine racine possède ou contrôle le service.
- Le service est vulnérable.
- Le nom est utilisé en production.

Le programme applique un contrôle de suffixe pour éviter de retenir des domaines hors périmètre. Ce filtrage ne constitue pas une preuve de propriété.

### Adresses IP

Une adresse IP associée à un hôte est une observation DNS au moment de la collecte.

Les adresses peuvent changer, être partagées par plusieurs clients ou correspondre à une infrastructure CDN, proxy ou hébergeur.

### TLS

Les informations TLS décrivent le certificat présenté lors de la connexion testée.

Un certificat peut couvrir plusieurs noms, être renouvelé ou ne pas être récupérable si la connexion échoue ou si la validation TLS est refusée par le client.

### HTTP

Le code HTTP, les redirections et les en-têtes décrivent une requête donnée à un instant donné.

Ils peuvent varier selon :

- La région géographique.
- L'adresse IP.
- Le User-Agent.
- Les protections anti-robot.
- La configuration du serveur.

### DNSSEC

La présence d'enregistrements `DS` ou `DNSKEY` est une observation utile, mais ne vaut pas validation DNSSEC.

Le projet ne doit pas être utilisé comme validateur cryptographique de chaîne DNSSEC.

---

## Dépannage

### Erreur `ModuleNotFoundError`

Vérifiez que l'environnement virtuel est activé, puis réinstallez les dépendances :

```bash
pip install -r requirements.txt
```

### Erreur de résolution DNS

Vérifiez :

- La connexion Internet.
- Le résolveur configuré sur la machine.
- La disponibilité du domaine.
- Les éventuels filtres réseau.

Certaines réponses DNS peuvent être limitées par le réseau.

### Délai d'attente dépassé

Augmentez éventuellement `REQUEST_TIMEOUT` dans `.env`.

Une valeur trop élevée peut allonger considérablement l'analyse si plusieurs hôtes ne répondent pas.

### Une source ne renvoie aucun résultat

Vérifiez :

- Que la source est activée dans `.env`.
- Que la clé API est correcte, si nécessaire.
- Que le quota n'est pas dépassé.
- Que le service tiers est accessible.
- Que le domaine possède des données indexées par cette source.

L'absence de résultat ne signifie pas qu'aucun sous-domaine n'existe.

### La carte ou le PDF ne se génère pas

Vérifiez l'installation de PyVis et ReportLab :

```bash
pip install pyvis reportlab
```

Consultez également le message d'erreur dans le terminal et vérifiez les droits d'écriture dans le répertoire de sortie.

### Résultats différents entre deux exécutions

C'est attendu : les données DNS, les certificats, les services web et les index des fournisseurs évoluent.

Les sources passives peuvent également mettre à jour ou retirer leurs données.

---

## Sécurité et usage responsable

Cet outil est destiné à la **reconnaissance passive et à la veille défensive** sur des domaines que vous possédez, administrez ou êtes explicitement autorisé à examiner.

Avant toute utilisation :

1. Définissez clairement le périmètre autorisé.
2. Respectez les conditions d'utilisation des sources consultées.
3. Protégez les clés API et les rapports produits.
4. Traitez les informations collectées comme potentiellement sensibles.
5. Ne considérez pas une observation comme une preuve de vulnérabilité ou de propriété.
6. Obtenez une autorisation explicite avant toute activité complémentaire plus intrusive.

Le projet décrit ici ne réalise pas :

- D'exploitation de vulnérabilités.
- De brute force de sous-domaines.
- De scan de ports.
- De test d'intrusion.
- De tentative d'accès non autorisé.

Les requêtes DNS, TLS et HTTP restent néanmoins des interactions réseau : utilisez-les de manière proportionnée et dans le respect des règles applicables.

---

## Limites connues

- La couverture dépend des sources publiques et des fournisseurs activés.
- Les résultats peuvent être incomplets, anciens ou temporairement indisponibles.
- Les quotas et API tierces peuvent limiter la collecte.
- Le nombre d'hôtes traités est plafonné par `MAX_SUBDOMAINS`.
- Le suivi historique ne couvre que les catégories comparées par le script.
- La découverte passive ne prouve ni la propriété ni le contrôle d'un hôte.
- La présence de `DS` ou `DNSKEY` n'est pas une validation DNSSEC complète.
- Les données WHOIS/RDAP peuvent être masquées ou incomplètes.
- Les résultats HTTP/TLS peuvent varier selon l'environnement réseau.
- Les formats et points d'accès des fournisseurs peuvent évoluer et nécessiter une adaptation du code.

---

## Améliorations possibles

Quelques évolutions envisageables :

- Cache local et limitation de débit par fournisseur.
- Nouvelles sources passives et gestion plus robuste de leurs API.
- Export CSV.
- Suivi des TTL DNS et historique DNS plus détaillé.
- Comparaison enrichie des certificats et dates d'expiration.
- Validation DNSSEC complète via une bibliothèque dédiée.
- Tableau de bord centralisé pour plusieurs domaines.
- Tests automatisés et intégration continue.
- Configuration de listes d'exclusion et de périmètres autorisés.
- Meilleure gestion des redirections HTTP et des erreurs réseau.

---

## Licence

Aucune licence spécifique n'est définie dans ce dépôt à ce stade.

Ajoutez un fichier `LICENSE` avant toute redistribution si vous souhaitez choisir et expliciter les conditions de réutilisation.

---

**Projet :** Domain Intelligence 
**Langage :** Python  
**Usage visé :** veille passive, inventaire de surface d'exposition et OSINT défensif.
