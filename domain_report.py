#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
                         DOMAIN INTELLIGENCE
===============================================================================

DESCRIPTION
-----------

Domain Intelligence est un outil Python de reconnaissance passive
(OSINT - Open Source Intelligence), d'analyse technique et de veille
défensive sur les domaines Internet.

Il permet de collecter, centraliser, analyser et historiser des informations
publiquement accessibles concernant un domaine et ses sous-domaines.

L'objectif est de fournir une vision globale de la surface d'exposition
observable d'un domaine, de cartographier les éléments de son infrastructure
et de détecter les changements constatés entre plusieurs analyses.

Domain Intelligence privilégie une approche passive reposant sur des sources
publiques, des services tiers et des observations techniques limitées.

-------------------------------------------------------------------------------
FONCTIONNALITÉS PRINCIPALES
-------------------------------------------------------------------------------

1. INFORMATIONS SUR LE DOMAINE
   - Collecte des informations WHOIS.
   - Collecte des informations RDAP.
   - Identification des informations d'enregistrement disponibles.
   - Observation des serveurs de noms.
   - Collecte des dates et informations de registre lorsqu'elles sont
     communiquées par les sources.
   - Centralisation des informations dans le rapport JSON.

2. ANALYSE DNS
   - Enregistrements A : adresses IPv4.
   - Enregistrements AAAA : adresses IPv6.
   - Enregistrements MX : serveurs de messagerie.
   - Enregistrements NS : serveurs DNS autoritaires déclarés.
   - Enregistrements TXT : informations textuelles et politiques DNS.
   - Enregistrements CNAME : alias DNS.
   - Enregistrements SOA : informations de zone DNS.
   - Enregistrements CAA : autorités de certification autorisées.
   - Enregistrements DS : informations de délégation DNSSEC.
   - Enregistrements DNSKEY : clés DNS publiées.
   - Observation des éléments liés à DNSSEC.

   Les données collectées représentent les enregistrements observés
   au moment de l'analyse. La présence de DS ou DNSKEY ne constitue
   pas une validation cryptographique complète de DNSSEC.

3. DÉCOUVERTE PASSIVE DE SOUS-DOMAINES
   Sources prises en charge :
   - crt.sh (Certificate Transparency).
   - HackerTarget.
   - VirusTotal.
   - SecurityTrails.
   - urlscan.io.

   Fonctionnalités :
   - Interrogation des sources activées.
   - Normalisation des noms de domaine.
   - Filtrage des résultats hors périmètre.
   - Suppression des doublons.
   - Conservation de la provenance des découvertes.
   - Limitation du nombre de résultats traités.
   - Gestion des erreurs et indisponibilités des sources.

   Les sous-domaines découverts sont des éléments observés dans des sources
   publiques. Leur découverte ne prouve ni leur disponibilité actuelle,
   ni leur appartenance ou leur contrôle par l'utilisateur.

4. ANALYSE DES HÔTES
   - Résolution DNS des noms d'hôtes découverts.
   - Collecte des adresses IPv4 et IPv6 disponibles.
   - Limitation du nombre d'hôtes traités.
   - Observation des certificats TLS.
   - Collecte des informations de certificats accessibles.
   - Vérification HTTP du domaine et des hôtes concernés.
   - Collecte des codes de statut HTTP.
   - Observation des en-têtes HTTP.
   - Observation des redirections sans les suivre automatiquement.
   - Gestion des erreurs de connexion et des délais d'attente.

   Les observations TLS et HTTP sont des vérifications techniques limitées.
   Elles ne constituent pas un audit de sécurité ni un test d'intrusion.

5. CARTOGRAPHIE INTERACTIVE
   - Représentation du domaine principal.
   - Visualisation des hôtes et sous-domaines.
   - Association des hôtes avec leurs adresses IP observées.
   - Création de relations entre les différents éléments.
   - Génération d'une cartographie HTML interactive avec PyVis.

6. HISTORIQUE ET DÉTECTION DES CHANGEMENTS
   - Création d'un instantané à chaque analyse.
   - Conservation du dernier état connu.
   - Conservation de l'état précédent.
   - Historisation des événements.
   - Détection des nouveaux sous-domaines observés.
   - Identification des sous-domaines non retrouvés.
   - Comparaison des données DNS.
   - Suivi des changements concernant les hôtes.
   - Suivi des observations TLS.
   - Suivi des observations HTTP.
   - Génération d'une chronologie HTML.

   Un sous-domaine non retrouvé lors d'une analyse ultérieure n'est pas
   nécessairement supprimé : il peut être temporairement indisponible,
   absent des sources consultées ou non retourné par celles-ci.

7. RAPPORTS ET EXPORTS
   - Rapport JSON contenant les données collectées.
   - Rapport HTML avec sections consultables.
   - Rapport PDF structuré.
   - Explications des principaux résultats dans le rapport PDF.
   - Cartographie interactive HTML.
   - Timeline HTML des événements.
   - Historisation locale des analyses.

-------------------------------------------------------------------------------
STRUCTURE DES RAPPORTS
-------------------------------------------------------------------------------

Chaque analyse dispose de son propre répertoire, organisé par domaine,
date et heure d'exécution.

Exemple :

   results/
       example.com/
           05_11_2026/
               11-30-25-123456/
                   rapport.json
                   rapport.pdf
                   rapport.html
                   cartographie.html
                   historique.html

           history/
               latest.json
               previous.json

               snapshots/
                   snapshot_*.json

               events/
                   events.jsonl

DESCRIPTION DES FICHIERS :

   rapport.json
       Contient les données structurées collectées pendant l'analyse.

   rapport.pdf
       Présente les résultats dans un rapport lisible, avec des explications
       destinées à faciliter leur interprétation.

   rapport.html
       Fournit une consultation des résultats dans un navigateur.

   cartographie.html
       Présente les relations observées entre domaine, hôtes et adresses IP.

   historique.html
       Présente les événements et changements enregistrés.

   latest.json
       Contient le dernier état connu du domaine.

   previous.json
       Contient l'état précédent disponible.

   snapshots/
       Conserve les instantanés successifs des analyses.

   events/
       Conserve les événements de comparaison au format JSONL.

-------------------------------------------------------------------------------
TECHNOLOGIES ET DÉPENDANCES
-------------------------------------------------------------------------------

Langage :
   Python 3.10+

Bibliothèques principales :
   - requests
   - python-whois
   - dnspython
   - reportlab
   - python-dotenv
   - pyvis

Modules standards utilisés :
   - argparse
   - concurrent.futures
   - datetime
   - hashlib
   - html
   - json
   - logging
   - os
   - re
   - socket
   - ssl
   - sys
   - time
   - pathlib
   - typing
   - urllib.parse

-------------------------------------------------------------------------------
CONFIGURATION
-------------------------------------------------------------------------------

Les paramètres sont chargés depuis le fichier .env.

VARIABLES DISPONIBLES :

   VIRUSTOTAL_API_KEY
       Clé API permettant d'interroger VirusTotal.

   SECURITYTRAILS_API_KEY
       Clé API permettant d'interroger SecurityTrails.

   REQUEST_TIMEOUT
       Durée maximale d'attente des requêtes réseau.

   MAX_SUBDOMAINS
       Nombre maximal de sous-domaines traités.

   MAX_HOSTS_TO_PROBE
       Nombre maximal d'hôtes soumis aux observations techniques.

   MAX_WORKERS
       Nombre maximal de traitements concurrents.

   OUTPUT_ROOT
       Répertoire racine de stockage des résultats.

   ENABLE_CRTSH
       Active ou désactive la source crt.sh.

   ENABLE_HACKERTARGET
       Active ou désactive la source HackerTarget.

   ENABLE_VIRUSTOTAL
       Active ou désactive la source VirusTotal.

   ENABLE_SECURITYTRAILS
       Active ou désactive la source SecurityTrails.

   ENABLE_URLSCAN
       Active ou désactive la source urlscan.io.

   ENABLE_TLS
       Active ou désactive les observations TLS.

   ENABLE_HTTP
       Active ou désactive les observations HTTP.

Les clés API doivent être conservées dans le fichier .env et ne doivent
jamais être intégrées directement dans le code source ou publiées
dans un dépôt public.

-------------------------------------------------------------------------------
UTILISATION
-------------------------------------------------------------------------------

Installation des dépendances :

   pip install -r requirements.txt

Vérification de la configuration :

   python domain_intelligence.py --check-config

Analyse d'un domaine :

   python domain_intelligence.py example.com

Analyse avec cartographie interactive :

   python domain_intelligence.py example.com --map

Analyse sans observations HTTP et TLS :

   python domain_intelligence.py example.com --no-active-web

Personnalisation du répertoire de sortie :

   python domain_intelligence.py example.com --out ./mes_analyses

Désactivation du rapport PDF :

   python domain_intelligence.py example.com --no-pdf

Désactivation du rapport HTML :

   python domain_intelligence.py example.com --no-html

Activation des journaux détaillés :

   python domain_intelligence.py example.com --verbose

Le paramètre --no-active-web désactive les observations TLS et HTTP.
Les collectes WHOIS, RDAP, DNS et les interrogations des sources passives
restent possibles. La résolution DNS des hôtes peut également être effectuée.

-------------------------------------------------------------------------------
PÉRIMÈTRE ET LIMITES TECHNIQUES
-------------------------------------------------------------------------------

Domain Intelligence est conçu pour la reconnaissance passive,
l'observation technique et la veille défensive.

L'outil ne réalise pas :
   - De brute force de sous-domaines.
   - De scan de ports.
   - D'exploitation de vulnérabilités.
   - De test d'intrusion.
   - De tentative d'accès non autorisé.
   - De contournement de mécanismes de sécurité.

Les résultats dépendent des sources publiques et des services tiers
interrogés. Ils peuvent être incomplets, anciens, limités par des quotas
ou temporairement indisponibles.

Les observations DNS, HTTP et TLS représentent un état ponctuel et peuvent
varier selon le moment de l'analyse, la résolution DNS, la localisation
réseau et les conditions d'accès.

La découverte d'un sous-domaine ne constitue pas une preuve de propriété
ou de contrôle du domaine.

La présence d'enregistrements DS ou DNSKEY ne constitue pas une validation
cryptographique complète de DNSSEC.

L'absence d'un résultat ne signifie pas nécessairement que la ressource
n'existe pas.

Les certificats TLS non validés par le contexte de confiance utilisé peuvent
ne pas être collectés comme certificats valides.

-------------------------------------------------------------------------------
UTILISATION RESPONSABLE ET SÉCURITÉ
-------------------------------------------------------------------------------

L'utilisateur doit disposer des autorisations nécessaires pour examiner
les domaines et infrastructures concernés.

Il est de sa responsabilité de :
   - Respecter le périmètre autorisé.
   - Respecter les conditions d'utilisation des fournisseurs.
   - Respecter les quotas et limitations des API.
   - Protéger les clés API et les fichiers de configuration.
   - Protéger les rapports pouvant contenir des informations sensibles.
   - Respecter les lois et réglementations applicables.
   - Vérifier les licences des bibliothèques et services tiers utilisés.

Les rapports doivent être stockés dans un emplacement adapté à leur niveau
de sensibilité et ne doivent pas être distribués sans précaution.

L'auteur du logiciel ne garantit ni l'exhaustivité, ni la disponibilité,
ni l'exactitude absolue des données collectées.

-------------------------------------------------------------------------------
INFORMATIONS DU PROJET
-------------------------------------------------------------------------------

Nom             : Domain Intelligence
Catégorie       : OSINT / Passive Domain Intelligence
Langage         : Python
Version Python  : 3.10+
Type            : Reconnaissance passive et veille technique
Sorties         : JSON / HTML / PDF
Cartographie    : PyVis
Historisation   : Snapshots JSON / Events JSONL
Sources         : crt.sh / HackerTarget / VirusTotal /
                  SecurityTrails / urlscan.io

Auteur          : Gabriel T
Organisation    : KAPELGY
Version         : 1.1.0
Date            : 2026-11-05

-------------------------------------------------------------------------------
ÉVOLUTION DU PROJET
-------------------------------------------------------------------------------

Domain Intelligence a vocation à évoluer vers une solution structurée
de veille et d'analyse de surface d'exposition.

Les évolutions envisageables comprennent notamment :
   - Interface graphique dédiée.
   - Tableau de bord centralisé.
   - Gestion de plusieurs domaines.
   - Comparaison avancée des historiques.
   - Alertes sur les changements détectés.
   - Gestion des utilisateurs et des accès.
   - Packaging et installation simplifiée.
   - Gestion des licences.
   - Tests automatisés et validation continue.
   - Documentation utilisateur et technique.

Toute distribution commerciale devra être précédée de tests approfondis,
d'une vérification des licences et conditions d'utilisation des services
tiers, ainsi que d'une revue des aspects juridiques et de sécurité.

-------------------------------------------------------------------------------
LICENCE
-------------------------------------------------------------------------------

Licence à définir par le propriétaire du projet.
Toute redistribution, modification ou exploitation commerciale doit
respecter la licence choisie ainsi que les licences et conditions
d'utilisation des bibliothèques et services tiers.

"""

#===============================================================================
#                         IMPORT DES LIBRAIRIES
#===============================================================================

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
import json
import logging
import os
import re
import socket
import ssl
import sys
import time

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


# ============================================================
# IMPORTS OPTIONNELS
# ============================================================

load_dotenv()

try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

try:
    import dns.resolver
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
        PageBreak,
    )
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

try:
    from pyvis.network import Network
    PYVIS_AVAILABLE = True
except ImportError:
    PYVIS_AVAILABLE = False



# ============================================================
# CONFIGURATION
# ============================================================
APP_NAME = "Domain Intelligence"
APP_VERSION = "1.1.0"
USER_AGENT = f"DomainIntelligence/{APP_VERSION}"
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "15"))
MAX_SUBDOMAINS = int(os.getenv("MAX_SUBDOMAINS", "2000"))
MAX_HOSTS_TO_PROBE = int(os.getenv("MAX_HOSTS_TO_PROBE", "50"))
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "6"))
# Scan TCP volontairement limité aux ports courants et non intrusifs.
ACTIVE_TCP_PORTS = (21, 22, 25, 53, 80, 110, 143, 443, 8080, 8443)
OUTPUT_ROOT = Path(os.getenv("OUTPUT_ROOT", "results"))
ENABLE_CRTSH = os.getenv("ENABLE_CRTSH", "true").lower() == "true"
ENABLE_HACKERTARGET = os.getenv(
    "ENABLE_HACKERTARGET", "false"
).lower() == "true"

ENABLE_VIRUSTOTAL = os.getenv(
    "ENABLE_VIRUSTOTAL", "true"
).lower() == "true"

ENABLE_SECURITYTRAILS = os.getenv(
    "ENABLE_SECURITYTRAILS", "true"
).lower() == "true"

ENABLE_URLSCAN = os.getenv(
    "ENABLE_URLSCAN", "false"
).lower() == "true"

ENABLE_TLS = os.getenv("ENABLE_TLS", "true").lower() == "true"
ENABLE_HTTP = os.getenv("ENABLE_HTTP", "true").lower() == "true"
ENABLE_CONTACT_INTELLIGENCE = (
    os.getenv("ENABLE_CONTACT_INTELLIGENCE", "true").lower() == "true"
)
# ============================================================
# LOGGING
# ============================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(APP_NAME)

# --------------------------------------------------
# DEFINITIONS DES FONCTIONS
# --------------------------------------------------

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_filename(value: str) -> str:
    return re.sub(
        r"[^a-zA-Z0-9._-]+",
        "_",
        value
    ).strip("._") or "domain"


def json_safe(value: Any) -> Any:

    if value is None:
        return None

    if isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")

    if isinstance(value, (list, tuple, set)):
        return [json_safe(x) for x in value]

    if isinstance(value, dict):
        return {
            str(k): json_safe(v)
            for k, v in value.items()
        }

    if hasattr(value, "isoformat"):
        try:
            return value.isoformat()
        except Exception:
            pass

    return str(value)


def normalize_domain(raw: str) -> str:

    raw = raw.strip()

    if "://" in raw:
        parsed = urlparse(raw)
        raw = parsed.hostname or ""

    raw = raw.split("/")[0]
    raw = raw.split(":")[0]
    raw = raw.rstrip(".").lower()

    if not raw or "." not in raw or len(raw) > 253:
        raise ValueError("Nom de domaine invalide.")

    try:
        raw = raw.encode("idna").decode("ascii")
    except UnicodeError as exc:
        raise ValueError("Nom de domaine internationalisé invalide.") from exc

    label_pattern = re.compile(
        r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$"
    )

    if any(not label_pattern.fullmatch(x) for x in raw.split(".")):
        raise ValueError("Format DNS incorrect.")

    return raw


def in_scope(hostname: str, domain: str) -> bool:

    hostname = hostname.lower().strip(".")

    return (
        hostname == domain
        or hostname.endswith("." + domain)
    )


def write_json(data: Any, path: Path) -> None:

    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(
            json_safe(data),
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def stable_hash(value: Any) -> str:

    serialized = json.dumps(
        json_safe(value),
        sort_keys=True,
        ensure_ascii=False,
    )

    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


# ============================================================
# ORGANISATION DES DOSSIERS
# ============================================================

def create_output_directory(
    domain: str,
    root: Path = OUTPUT_ROOT,
) -> Path:

    now = datetime.now().astimezone()

    domain_dir = root / safe_filename(domain)

    date_dir = now.strftime("%d_%m_%Y")

    time_dir = now.strftime("%H-%M-%S-%f")

    output_dir = domain_dir / date_dir / time_dir

    output_dir.mkdir(parents=True, exist_ok=True)

    (domain_dir / "history" / "snapshots").mkdir(
        parents=True,
        exist_ok=True,
    )

    (domain_dir / "history" / "events").mkdir(
        parents=True,
        exist_ok=True,
    )

    return output_dir


# ============================================================
# COLLECTEUR PRINCIPAL
# ============================================================

class DomainCollector:

    def __init__(self, domain: str):

        self.domain = domain

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": USER_AGENT,
        })

        self.errors = []

        self.report = {
            "application": APP_NAME,
            "version": APP_VERSION,
            "domain": domain,
            "scan_date": datetime.now().astimezone().isoformat(),

            "whois": {},
            "rdap": {},
            "dns": {},

            "discovered": [],
            "sources": {},

            "hosts": [],
            "tls": [],
            "http": [],
            "port_scan": [],

            "errors": [],

            "scope": {
                "root_domain": domain,
                "mode": "passive",
                "port_scanning": False,
                "bruteforce": False,
                "exploitation": False,
                "http_redirect_following": False,
            },
        }

    # --------------------------------------------------------
    # REQUÊTES HTTP
    # --------------------------------------------------------

    def request(self, url, **kwargs):

        kwargs.setdefault(
            "timeout",
            REQUEST_TIMEOUT
        )

        kwargs.setdefault(
            "allow_redirects",
            False
        )

        response = self.session.get(
            url,
            **kwargs
        )

        response.raise_for_status()

        return response

    def add_error(self, component, error):

        item = {
            "component": component,
            "error": str(error)[:500],
            "date": utc_now(),
        }

        self.errors.append(item)

        logger.warning(
            "%s : %s",
            component,
            error,
        )

    # --------------------------------------------------------
    # WHOIS
    # --------------------------------------------------------

    def collect_whois(self):

        if not WHOIS_AVAILABLE:
            self.add_error(
                "WHOIS",
                "python-whois non installé",
            )
            return

        try:

            result = whois.whois(self.domain)

            self.report["whois"] = json_safe(
                dict(result)
            )

        except Exception as exc:

            self.add_error("WHOIS", exc)

    # --------------------------------------------------------
    # RDAP
    # --------------------------------------------------------

    def collect_rdap(self):

        urls = [
            f"https://rdap.org/domain/{self.domain}",
        ]

        for url in urls:

            try:

                response = self.request(
                    url,
                    headers={
                        "Accept": "application/rdap+json"
                    },
                )

                self.report["rdap"] = response.json()

                return

            except Exception as exc:

                last_error = exc

        self.add_error("RDAP", last_error)

    # --------------------------------------------------------
    # DNS
    # --------------------------------------------------------

    def collect_dns(self):

        if not DNS_AVAILABLE:
            self.add_error(
                "DNS",
                "dnspython non installé",
            )
            return

        resolver = dns.resolver.Resolver()

        resolver.lifetime = REQUEST_TIMEOUT

        record_types = [
            "A",
            "AAAA",
            "MX",
            "NS",
            "TXT",
            "CNAME",
            "SOA",
            "CAA",
            "DS",
            "DNSKEY",
        ]

        result = {}

        for record_type in record_types:

            try:

                answer = resolver.resolve(
                    self.domain,
                    record_type,
                    raise_on_no_answer=False,
                )

                if answer.rrset is None:
                    result[record_type] = []
                else:
                    result[record_type] = [
                        record.to_text()
                        for record in answer
                    ]

            except Exception:
                result[record_type] = []

        result["_dnssec_note"] = (
            "La présence de DS/DNSKEY est observée. "
            "Aucune validation cryptographique DNSSEC n'est effectuée."
        )

        self.report["dns"] = result

    # --------------------------------------------------------
    # SOURCES OSINT
    # --------------------------------------------------------

    def source_crtsh(self):

        response = self.request(
            "https://crt.sh/",
            params={
                "q": f"%.{self.domain}",
                "output": "json",
            },
        )

        data = response.json()

        found = set()

        for item in data if isinstance(data, list) else []:

            names = str(
                item.get("name_value", "")
            ).splitlines()

            for name in names:

                name = name.strip().lower().lstrip("*.")

                if in_scope(name, self.domain):
                    found.add(name)

        return sorted(found)

    def source_hackertarget(self):

        response = self.request(
            "https://api.hackertarget.com/hostsearch/",
            params={"q": self.domain},
        )

        found = set()

        for line in response.text.splitlines():

            hostname = line.split(",", 1)[0].strip().lower()

            if in_scope(hostname, self.domain):
                found.add(hostname)

        return sorted(found)

    def source_virustotal(self):

        api_key = os.getenv("VIRUSTOTAL_API_KEY", "").strip()

        if not api_key:
            raise RuntimeError("Clé VirusTotal absente.")

        headers = {
            "x-apikey": api_key,
        }

        url = (
            "https://www.virustotal.com/api/v3/domains/"
            f"{self.domain}/subdomains"
        )

        found = set()

        for _ in range(10):

            response = self.request(
                url,
                headers=headers,
                params={"limit": 40},
            )

            payload = response.json()

            for item in payload.get("data", []):

                hostname = item.get("id", "").lower()

                if in_scope(hostname, self.domain):
                    found.add(hostname)

            next_url = payload.get(
                "links", {}
            ).get("next")

            if not next_url:
                break

            parsed = urlparse(next_url)

            if (
                parsed.scheme != "https"
                or parsed.hostname != "www.virustotal.com"
            ):
                break

            url = next_url

        return sorted(found)

    def source_securitytrails(self):

        api_key = os.getenv(
            "SECURITYTRAILS_API_KEY",
            "",
        ).strip()

        if not api_key:
            raise RuntimeError("Clé SecurityTrails absente.")

        response = self.request(
            (
                "https://api.securitytrails.com/v1/domain/"
                f"{self.domain}/subdomains"
            ),
            headers={
                "APIKEY": api_key,
            },
        )

        found = set()

        for subdomain in response.json().get("subdomains", []):

            hostname = (
                f"{subdomain}.{self.domain}"
            ).lower()

            if in_scope(hostname, self.domain):
                found.add(hostname)

        return sorted(found)

    def source_urlscan(self):

        response = self.request(
            "https://urlscan.io/api/v1/search/",
            params={
                "q": f"domain:{self.domain}",
                "size": 100,
            },
        )

        found = set()

        for item in response.json().get("results", []):

            page = item.get("page", {})

            candidates = [
                page.get("domain"),
                page.get("url"),
            ]

            for candidate in candidates:

                if not candidate:
                    continue

                host = urlparse(
                    candidate if "://" in candidate
                    else "//" + candidate
                ).hostname

                if host and in_scope(
                    host.lower(),
                    self.domain,
                ):
                    found.add(host.lower())

        return sorted(found)

    def discover_subdomains(self):

        sources = {
            "crt.sh": (
                self.source_crtsh,
                ENABLE_CRTSH,
            ),
            "HackerTarget": (
                self.source_hackertarget,
                ENABLE_HACKERTARGET,
            ),
            "VirusTotal": (
                self.source_virustotal,
                ENABLE_VIRUSTOTAL,
            ),
            "SecurityTrails": (
                self.source_securitytrails,
                ENABLE_SECURITYTRAILS,
            ),
            "urlscan.io": (
                self.source_urlscan,
                ENABLE_URLSCAN,
            ),
        }

        provenance = {}

        for source_name, (function, enabled) in sources.items():

            if not enabled:

                self.report["sources"][source_name] = {
                    "enabled": False,
                    "status": "disabled",
                    "count": 0,
                }

                continue

            try:

                results = function()

                self.report["sources"][source_name] = {
                    "enabled": True,
                    "status": "success",
                    "count": len(results),
                }

                for hostname in results:

                    provenance.setdefault(
                        hostname,
                        set(),
                    ).add(source_name)

            except Exception as exc:

                self.report["sources"][source_name] = {
                    "enabled": True,
                    "status": "error",
                    "count": 0,
                    "error": str(exc)[:300],
                }

                self.add_error(
                    f"OSINT:{source_name}",
                    exc,
                )

        discovered = sorted(provenance)

        discovered = discovered[:MAX_SUBDOMAINS]

        self.report["discovered"] = [
            {
                "hostname": hostname,
                "sources": sorted(provenance[hostname]),
            }
            for hostname in discovered
        ]

    # --------------------------------------------------------
    # RÉSOLUTION DNS DES HÔTES
    # --------------------------------------------------------

    def resolve_host(self, hostname):

        result = {
            "hostname": hostname,
            "A": [],
            "AAAA": [],
            "CNAME": [],
            "resolved": False,
        }

        if not DNS_AVAILABLE:
            result["error"] = "dnspython non installé"
            return result

        resolver = dns.resolver.Resolver()

        resolver.lifetime = REQUEST_TIMEOUT

        for record_type in ("A", "AAAA", "CNAME"):

            try:

                answer = resolver.resolve(
                    hostname,
                    record_type,
                    raise_on_no_answer=False,
                )

                if answer.rrset:

                    result[record_type] = [
                        item.to_text()
                        for item in answer
                    ]

            except Exception:
                pass

        result["resolved"] = bool(
            result["A"]
            or result["AAAA"]
            or result["CNAME"]
        )

        return result

    def collect_hosts(self):

        hostnames = [self.domain]

        hostnames.extend(
            item["hostname"]
            for item in self.report["discovered"]
        )

        hostnames = list(dict.fromkeys(hostnames))

        hostnames = hostnames[:MAX_HOSTS_TO_PROBE]

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=MAX_WORKERS
        ) as executor:

            futures = {
                executor.submit(self.resolve_host, hostname): hostname
                for hostname in hostnames
            }

            for future in concurrent.futures.as_completed(futures):

                try:
                    self.report["hosts"].append(
                        future.result()
                    )

                except Exception as exc:
                    self.add_error("Résolution DNS", exc)

        self.report["hosts"].sort(
            key=lambda item: item["hostname"]
        )

    # --------------------------------------------------------
    # TLS
    # --------------------------------------------------------

    def collect_tls_one(self, hostname):

        result = {
            "hostname": hostname,
        }

        context = ssl.create_default_context()

        try:

            with socket.create_connection(
                (hostname, 443),
                timeout=REQUEST_TIMEOUT,
            ) as sock:

                with context.wrap_socket(
                    sock,
                    server_hostname=hostname,
                ) as tls_socket:

                    certificate = tls_socket.getpeercert()

                    result.update({
                        "subject": certificate.get("subject"),
                        "issuer": certificate.get("issuer"),
                        "not_before": certificate.get("notBefore"),
                        "not_after": certificate.get("notAfter"),
                        "san": certificate.get("subjectAltName", []),
                        "serial_number": certificate.get("serialNumber"),
                        "tls_version": tls_socket.version(),
                    })

        except Exception as exc:

            result["error"] = (
                f"{type(exc).__name__}: {str(exc)[:300]}"
            )

        return json_safe(result)

    def collect_tls(self):

        if not ENABLE_TLS:
            return

        hosts = [
            item["hostname"]
            for item in self.report["hosts"]
            if item.get("resolved")
        ]

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=MAX_WORKERS
        ) as executor:

            self.report["tls"] = list(
                executor.map(
                    self.collect_tls_one,
                    hosts,
                )
            )

    # --------------------------------------------------------
    # HTTP / HTTPS
    # --------------------------------------------------------

    def collect_http_one(self, hostname):

        last_error = None

        for scheme in ("https", "http"):

            url = f"{scheme}://{hostname}/"

            try:

                response = self.session.get(
                    url,
                    timeout=REQUEST_TIMEOUT,
                    allow_redirects=False,
                    stream=True,
                )

                result = {
                    "url": url,
                    "status_code": response.status_code,
                    "server": response.headers.get("Server"),
                    "content_type": response.headers.get("Content-Type"),
                    "headers": dict(response.headers),
                    "redirect_location": response.headers.get("Location"),
                }

                content = b""

                try:

                    for chunk in response.iter_content(
                        chunk_size=4096
                    ):

                        content += chunk

                        if len(content) >= 65536:
                            break

                finally:
                    response.close()

                if "html" in str(
                    result["content_type"]
                ).lower():

                    match = re.search(
                        rb"<title[^>]*>(.*?)</title>",
                        content,
                        re.IGNORECASE | re.DOTALL,
                    )

                    if match:

                        result["title"] = match.group(
                            1
                        ).decode(
                            "utf-8",
                            errors="replace",
                        ).strip()[:300]

                return json_safe(result)

            except requests.RequestException as exc:

                last_error = (
                    f"{type(exc).__name__}: {str(exc)[:250]}"
                )

        return {
            "hostname": hostname,
            "error": last_error,
        }

    def collect_http(self):

        if not ENABLE_HTTP:
            return

        hosts = [
            item["hostname"]
            for item in self.report["hosts"]
            if item.get("resolved")
        ]

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=MAX_WORKERS
        ) as executor:

            self.report["http"] = list(
                executor.map(
                    self.collect_http_one,
                    hosts,
                )
            )

    # --------------------------------------------------------
    # RECONNAISSANCE ACTIVE : SCAN TCP LIMITÉ
    # --------------------------------------------------------

    def scan_tcp_host(self, host):
        """Teste une courte liste de ports TCP sur les IP résolues du domaine."""
        findings = {
            "hostname": host.get("hostname"),
            "addresses": [],
            "open_ports": [],
        }
        addresses = list(dict.fromkeys(host.get("A", []) + host.get("AAAA", [])))
        findings["addresses"] = addresses

        for address in addresses:
            for port in ACTIVE_TCP_PORTS:
                try:
                    with socket.create_connection(
                        (address, port), timeout=min(REQUEST_TIMEOUT, 2)
                    ):
                        findings["open_ports"].append({
                            "address": address,
                            "port": port,
                            "service": {
                                21: "ftp", 22: "ssh", 25: "smtp",
                                53: "dns", 80: "http", 110: "pop3",
                                143: "imap", 443: "https",
                                8080: "http-alt", 8443: "https-alt",
                            }.get(port, "unknown"),
                        })
                except (OSError, socket.timeout):
                    continue

        return findings

    def collect_port_scan(self):
        """Scan TCP borné aux hôtes du périmètre déjà découverts et résolus."""
        hosts = [item for item in self.report["hosts"] if item.get("resolved")]
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            self.report["port_scan"] = list(executor.map(self.scan_tcp_host, hosts))

    # --------------------------------------------------------
    # EXÉCUTION
    # --------------------------------------------------------

    def run(self, active=False, active_web=True):

        start = time.monotonic()

        logger.info("Début de l'analyse : %s", self.domain)

        self.collect_whois()
        self.collect_rdap()
        self.collect_contacts()
        self.collect_dns()

        self.discover_subdomains()

        if active:
            self.report["scope"].update({
                "mode": "active",
                "port_scanning": True,
                "active_web_checks": bool(active_web),
            })
            self.collect_hosts()
            if active_web:
                self.collect_tls()
                self.collect_http()
            self.collect_port_scan()
        else:
            self.report["scope"].update({
                "mode": "passive",
                "port_scanning": False,
                "active_web_checks": False,
            })

        self.report["finished_at_utc"] = utc_now()

        self.report["duration_seconds"] = round(
            time.monotonic() - start,
            2,
        )

        self.report["errors"] = self.errors

        return self.report

    def close(self):
        self.session.close()


# ============================================================
# HISTORIQUE ET COMPARAISON
# ============================================================

def save_history(report, root, output_dir):

    domain_dir = root / safe_filename(report["domain"])

    history_dir = domain_dir / "history"

    snapshots_dir = history_dir / "snapshots"

    events_dir = history_dir / "events"

    snapshots_dir.mkdir(parents=True, exist_ok=True)

    events_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().astimezone().strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    snapshot = snapshots_dir / f"{stamp}.json"

    write_json(report, snapshot)

    latest = history_dir / "latest.json"

    previous = history_dir / "previous.json"

    events_file = events_dir / "events.jsonl"

    events = []

    if previous.exists():

        try:

            old = json.loads(
                previous.read_text(encoding="utf-8")
            )

            old_hosts = {
                item.get("hostname")
                for item in old.get("discovered", [])
                if isinstance(item, dict)
            }

            new_hosts = {
                item.get("hostname")
                for item in report.get("discovered", [])
                if isinstance(item, dict)
            }

            for hostname in sorted(new_hosts - old_hosts):

                events.append({
                    "type": "subdomain_added",
                    "hostname": hostname,
                    "date": utc_now(),
                })

            for hostname in sorted(old_hosts - new_hosts):

                events.append({
                    "type": "subdomain_not_seen",
                    "hostname": hostname,
                    "date": utc_now(),
                    "note": (
                        "Non retrouvé pendant cette analyse. "
                        "La suppression n'est pas confirmée."
                    ),
                })

            for category in (
                "dns",
                "hosts",
                "tls",
                "http",
            ):

                if stable_hash(old.get(category)) != stable_hash(
                    report.get(category)
                ):

                    events.append({
                        "type": "category_changed",
                        "category": category,
                        "date": utc_now(),
                    })

        except Exception as exc:

            logger.warning(
                "Comparaison historique impossible : %s",
                exc,
            )

    with events_file.open(
        "a",
        encoding="utf-8",
    ) as file:

        for event in events:

            file.write(
                json.dumps(
                    event,
                    ensure_ascii=False,
                ) + "\n"
            )

    write_json(report, latest)

    write_json(report, previous)


# ============================================================
# EXPLICATIONS POUR LES RAPPORTS
# ============================================================

EXPLANATIONS = {
    "registrar": "Bureau d'enregistrement du domaine.",
    "creation_date": "Date de création déclarée.",
    "expiration_date": "Date d'expiration déclarée.",
    "updated_date": "Dernière modification connue.",
    "name_servers": "Serveurs DNS déclarés pour gérer le domaine.",
    "status": "Statut administratif ou technique publié.",
    "emails": "Adresses électroniques éventuellement publiées.",
    "org": "Organisation déclarée dans les données d'enregistrement.",
    "country": "Pays déclaré dans les données d'enregistrement.",
    "A": "Adresse IPv4 associée au nom.",
    "AAAA": "Adresse IPv6 associée au nom.",
    "MX": "Serveur de réception des courriels.",
    "NS": "Serveur DNS faisant autorité.",
    "TXT": "Donnée textuelle pouvant contenir SPF ou des vérifications de services.",
    "CNAME": "Alias DNS pointant vers un autre nom.",
    "SOA": "Paramètres principaux de gestion de la zone.",
    "CAA": "Autorités de certification autorisées à émettre des certificats.",
    "DS": "Empreinte reliant une zone à la chaîne de confiance DNSSEC.",
    "DNSKEY": "Clé publique publiée pour DNSSEC.",
    "hostname": "Nom d'hôte observé.",
    "resolved": "Indique si une réponse DNS exploitable a été obtenue.",
    "sources": "Sources passives ayant rapporté ce nom.",
    "subject": "Identité déclarée dans le certificat TLS.",
    "issuer": "Autorité ayant signé le certificat.",
    "not_before": "Début de validité déclaré du certificat.",
    "not_after": "Fin de validité déclarée du certificat.",
    "san": "Autres noms de domaine couverts par le certificat.",
    "serial_number": "Numéro de série du certificat.",
    "tls_version": "Version du protocole TLS négociée.",
    "url": "Adresse web interrogée.",
    "status_code": "Code HTTP retourné par le serveur.",
    "server": "Valeur de l'en-tête Server, si elle est publiée.",
    "content_type": "Type de contenu retourné.",
    "title": "Titre HTML de la page, lorsqu'il est disponible.",
    "headers": "En-têtes HTTP observés.",
    "error": "Erreur de collecte. Elle ne prouve pas l'absence du service.",
}


def explain(key):
    return EXPLANATIONS.get(
        str(key),
        "Valeur technique observée pendant l'analyse.",
    )


def readable(value):

    if value is None:
        return "Non renseigné"

    if isinstance(value, bool):
        return "Oui" if value else "Non"

    if isinstance(value, (dict, list, tuple)):
        return json.dumps(
            value,
            ensure_ascii=False,
            indent=2,
            default=json_safe,
        )

    return str(value)


# ============================================================
# EXPORT PDF
# ============================================================

def export_pdf(report, output_path):

    if not REPORTLAB_AVAILABLE:
        raise RuntimeError(
            "Installez reportlab pour produire le PDF."
        )

    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="MainTitle",
            parent=styles["Title"],
            fontSize=23,
            leading=29,
            alignment=1,
            textColor=colors.HexColor("#203A54"),
        )
    )

    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading2"],
            fontSize=13,
            textColor=colors.HexColor("#203A54"),
            spaceBefore=12,
            spaceAfter=7,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SmallText",
            parent=styles["BodyText"],
            fontSize=7.5,
            leading=10,
        )
    )

    styles.add(
        ParagraphStyle(
            name="Explanation",
            parent=styles["BodyText"],
            fontSize=8.5,
            leading=12,
            textColor=colors.HexColor("#4D5965"),
            spaceAfter=7,
        )
    )

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=14 * mm,
        leftMargin=14 * mm,
        topMargin=16 * mm,
        bottomMargin=17 * mm,
        title=f"Rapport OSINT - {report['domain']}",
        author=APP_NAME,
    )

    story = []

    def paragraph(text, style):
        return Paragraph(
            html.escape(str(text)).replace("\n", "<br/>"),
            style,
        )

    def heading(title, explanation=None):

        story.append(
            paragraph(title, styles["Section"])
        )

        if explanation:
            story.append(
                paragraph(
                    explanation,
                    styles["Explanation"],
                )
            )

    def data_table(data, section):

        if not isinstance(data, dict) or not data:

            story.append(
                paragraph(
                    "Aucune donnée exploitable obtenue.",
                    styles["BodyText"],
                )
            )

            return

        rows = [[
            paragraph("Champ", styles["SmallText"]),
            paragraph("Valeur observée", styles["SmallText"]),
            paragraph("Explication", styles["SmallText"]),
        ]]

        for key, value in data.items():

            rows.append([
                paragraph(key, styles["SmallText"]),
                paragraph(
                    readable(value)[:10000],
                    styles["SmallText"],
                ),
                paragraph(
                    explain(key),
                    styles["SmallText"],
                ),
            ])

        table = Table(
            rows,
            colWidths=[
                32 * mm,
                77 * mm,
                66 * mm,
            ],
            repeatRows=1,
        )

        table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#24364B"),
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.3,
                    colors.lightgrey,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#F2F5F8"),
                    ],
                ),
            ])
        )

        story.append(table)

        story.append(Spacer(1, 5))

    # COUVERTURE

    story.extend([
        Spacer(1, 40 * mm),
        paragraph(APP_NAME, styles["MainTitle"]),
        paragraph(
            "Rapport de reconnaissance "
            + str(report.get("scope", {}).get("mode", "passive"))
            + " et OSINT",
            styles["Heading2"],
        ),
        Spacer(1, 15 * mm),
        paragraph(
            f"Domaine : {report['domain']}",
            styles["BodyText"],
        ),
        paragraph(
            f"Date : {report['scan_date']}",
            styles["BodyText"],
        ),
        Spacer(1, 10 * mm),
        paragraph(
            "Ce document décrit des informations publiquement "
            "observables à la date de l'analyse. Il ne constitue "
            "ni un audit d'intrusion ni une preuve de propriété.",
            styles["Explanation"],
        ),
        PageBreak(),
    ])

    # RÉSUMÉ

    heading(
        "1. Résumé exécutif",
        "Synthèse des observations collectées.",
    )

    summary = {
        "Domaine": report["domain"],
        "Sous-domaines découverts": len(report["discovered"]),
        "Hôtes examinés": len(report["hosts"]),
        "Résultats TLS": len(report["tls"]),
        "Observations HTTP": len(report["http"]),
        "Erreurs de collecte": len(report["errors"]),
        "Durée en secondes": report.get("duration_seconds"),
    }

    data_table(summary, "summary")

    # WHOIS

    heading(
        "2. Informations WHOIS",
        "Données publiques d'enregistrement. "
        "Certaines informations peuvent être masquées.",
    )

    data_table(report.get("whois", {}), "whois")

    # RDAP

    heading(
        "3. Informations RDAP",
        "Données structurées concernant l'enregistrement du domaine.",
    )

    rdap = report.get("rdap", {})

    selected = {
        key: rdap.get(key)
        for key in (
            "handle",
            "ldhName",
            "status",
            "events",
            "entities",
            "nameservers",
            "links",
        )
        if key in rdap
    }

    data_table(selected or rdap, "rdap")

    # DNS

    heading(
        "4. Configuration DNS",
        "Les enregistrements décrivent la configuration DNS publiée. "
        "La présence de DS/DNSKEY ne signifie pas que DNSSEC a été validé.",
    )

    for record_type, records in report.get("dns", {}).items():

        if str(record_type).startswith("_"):
            story.append(
                paragraph(records, styles["Explanation"])
            )
            continue

        story.append(
            paragraph(
                f"Enregistrement {record_type}",
                styles["Heading3"],
            )
        )

        story.append(
            paragraph(
                explain(record_type),
                styles["Explanation"],
            )
        )

        story.append(
            paragraph(
                readable(records),
                styles["SmallText"],
            )
        )

    # SOUS-DOMAINES

    heading(
        "5. Sous-domaines découverts",
        "Une découverte passive ne garantit pas que le sous-domaine "
        "est encore actif ou accessible.",
    )

    discovered = report.get("discovered", [])

    if discovered:

        rows = [[
            paragraph("Nom d'hôte", styles["SmallText"]),
            paragraph("Sources", styles["SmallText"]),
        ]]

        for item in discovered:

            rows.append([
                paragraph(
                    item.get("hostname", ""),
                    styles["SmallText"],
                ),
                paragraph(
                    ", ".join(item.get("sources", [])),
                    styles["SmallText"],
                ),
            ])

        table = Table(
            rows,
            colWidths=[90 * mm, 85 * mm],
            repeatRows=1,
        )

        table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#24364B"),
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.3,
                    colors.lightgrey,
                ),
            ])
        )

        story.append(table)

    else:

        story.append(
            paragraph(
                "Aucun sous-domaine découvert.",
                styles["BodyText"],
            )
        )

    # SOURCES

    heading(
        "6. Sources OSINT",
        "Les sources peuvent être limitées par leurs quotas, "
        "leurs données ou leur disponibilité.",
    )

    data_table(report.get("sources", {}), "sources")

    # HÔTES

    heading(
        "7. Résolution des hôtes",
        "Une résolution réussie signifie qu'une réponse DNS a été obtenue "
        "au moment du test.",
    )

    for host in report.get("hosts", []):
        data_table(host, "hosts")

    # TLS

    heading(
        "8. Certificats TLS",
        "Les certificats sont observés lors d'une connexion TLS. "
        "Un échec de connexion ne prouve pas l'absence de certificat.",
    )

    for item in report.get("tls", []):
        data_table(item, "tls")

    # HTTP

    heading(
        "9. Observations HTTP et HTTPS",
        "Les requêtes portent sur la racine des hôtes résolus. "
        "Les redirections ne sont pas suivies.",
    )

    status_explanations = {
        200: "Réponse réussie.",
        301: "Redirection permanente.",
        302: "Redirection temporaire.",
        400: "Requête incorrecte.",
        401: "Authentification requise.",
        403: "Accès refusé.",
        404: "Ressource non trouvée.",
        429: "Limitation du nombre de requêtes.",
        500: "Erreur interne du serveur.",
        502: "Réponse incorrecte d'un serveur intermédiaire.",
        503: "Service temporairement indisponible.",
    }

    for item in report.get("http", []):

        data_table(item, "http")

        code = item.get("status_code")

        if code is not None:

            try:
                explanation = status_explanations.get(
                    int(code),
                    "Code HTTP renvoyé par le serveur.",
                )

                story.append(
                    paragraph(
                        f"Code {code} : {explanation}",
                        styles["Explanation"],
                    )
                )

            except (ValueError, TypeError):
                pass

    # SCAN TCP ACTIF

    if report.get("port_scan"):
        heading(
            "10. Ports TCP observés",
            "Tests de connexion TCP limités à une liste de ports courants. "
            "Un port fermé ou filtré peut ne pas répondre.",
        )
        for item in report.get("port_scan", []):
            data_table(item, "port_scan")

    # ERREURS

    heading(
        "11. Erreurs et limites de collecte",
        "Une erreur indique une collecte incomplète. "
        "Elle ne prouve pas l'absence d'une ressource.",
    )

    for error in report.get("errors", []):

        story.append(
            paragraph(
                readable(error),
                styles["SmallText"],
            )
        )

    if not report.get("errors"):

        story.append(
            paragraph(
                "Aucune erreur enregistrée.",
                styles["BodyText"],
            )
        )

    # MÉTHODOLOGIE

    heading("11. Méthodologie et limites")

    limitations = [
        "Les données passives dépendent des bases interrogées.",
        "Les sous-domaines peuvent être historiques ou inactifs.",
        "Les données DNS peuvent évoluer après l'analyse.",
        "La présence de DS/DNSKEY ne valide pas DNSSEC.",
        "Les observations TLS ne constituent pas un audit complet.",
        "Les codes HTTP ne prouvent pas une vulnérabilité.",
        "Aucun scan de ports, brute-force ou exploitation n'est réalisé.",
        "Les observations ne prouvent pas la propriété d'une ressource.",
    ]

    for limitation in limitations:

        story.append(
            paragraph(
                "• " + limitation,
                styles["Explanation"],
            )
        )

    heading(
        "12. Conclusion",
        "Ce rapport constitue un inventaire d'observations techniques "
        "à un instant donné. Les anomalies potentielles doivent être "
        "vérifiées avant toute qualification de risque.",
    )

    def footer(canvas, document):

        canvas.saveState()

        canvas.setFont("Helvetica", 7)

        canvas.setFillColor(colors.grey)

        canvas.drawString(
            14 * mm,
            9 * mm,
            f"{APP_NAME} {APP_VERSION}",
        )

        canvas.drawRightString(
            A4[0] - 14 * mm,
            9 * mm,
            f"Page {document.page}",
        )

        canvas.restoreState()

    doc.build(
        story,
        onFirstPage=footer,
        onLaterPages=footer,
    )
    # CONTACT INTELLIGENCE

    heading(
        "4. Contacts professionnels",
        "Coordonnées professionnelles publiquement disponibles "
        "dans les données WHOIS et RDAP."
    )

    contacts = report.get("contacts", {})

    data_table(
        {
            "Statut": contacts.get("status"),
            "Nombre de contacts": contacts.get("count", 0),
            "Contacts": contacts.get("data", []),
        },
        "contacts",
    )

# ============================================================
# RAPPORT HTML
# ============================================================

def export_html(report, output_path):

    sections = [
        "whois",
        "rdap",
        "dns",
        "discovered",
        "sources",
        "hosts",
        "tls",
        "http",
        "port_scan",
        "errors",
    ]

    content = []

    for section in sections:

        payload = json.dumps(
            report.get(section, {}),
            ensure_ascii=False,
            indent=2,
        )

        content.append(
            f"""
            <details open>
                <summary>{html.escape(section.upper())}</summary>
                <pre>{html.escape(payload)}</pre>
            </details>
            """
        )

    page = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Domain Intelligence - {html.escape(report['domain'])}</title>

    <style>

    body {{
        font-family: Arial, sans-serif;
        background: #f4f6f9;
        color: #253447;
        max-width: 1200px;
        margin: auto;
        padding: 30px;
    }}

    h1 {{
        color: #183a5a;
    }}

    details {{
        background: white;
        border: 1px solid #d9e0e8;
        border-radius: 8px;
        padding: 15px;
        margin: 12px 0;
    }}

    summary {{
        cursor: pointer;
        font-weight: bold;
    }}

    pre {{
        white-space: pre-wrap;
        overflow-wrap: anywhere;
        background: #f3f5f7;
        padding: 15px;
        border-radius: 5px;
    }}

    </style>
    </head>

    <body>

    <h1>Domain Intelligence V4</h1>

    <p>
        <b>Domaine :</b> {html.escape(report['domain'])}<br>
        <b>Date :</b> {html.escape(report['scan_date'])}
    </p>

    <p>
        Rapport de reconnaissance passive et d'observations OSINT.
    </p>

    {''.join(content)}

    </body>
    </html>
    """

    output_path.write_text(
        page,
        encoding="utf-8",
    )


    # --------------------------------------------------------
    # CONTACT INTELLIGENCE
    # --------------------------------------------------------

    def collect_contacts(self):

        if not ENABLE_CONTACT_INTELLIGENCE:
            self.report["contacts"] = {
                "enabled": False,
                "status": "disabled",
                "data": [],
            }
            return

        contacts = []

        generic_prefixes = {
            "abuse",
            "security",
            "admin",
            "administrator",
            "hostmaster",
            "webmaster",
            "postmaster",
            "support",
            "contact",
            "info",
            "noc",
            "technical",
            "privacy",
        }

        def is_generic_email(email):

            if not isinstance(email, str):
                return False

            email = email.strip().lower()

            if "@" not in email:
                return False

            local_part = email.split("@", 1)[0]

            return (
                local_part in generic_prefixes
                or any(
                    local_part.startswith(prefix + "+")
                    for prefix in generic_prefixes
                )
            )

        def extract_vcard(entity):

            result = {
                "organization": None,
                "role": None,
                "emails": [],
                "phones": [],
                "addresses": [],
            }

            vcard = entity.get("vcardArray")

            if not isinstance(vcard, list) or len(vcard) < 2:
                return result

            for field in vcard[1]:

                if not isinstance(field, list) or len(field) < 4:
                    continue

                field_name = str(field[0]).lower()
                value = field[3]

                if field_name == "org":

                    if isinstance(value, list):
                        result["organization"] = " ".join(
                            str(x) for x in value
                        )
                    else:
                        result["organization"] = str(value)

                elif field_name == "kind":

                    result["role"] = str(value)

                elif field_name == "email":

                    if is_generic_email(value):
                        result["emails"].append(value.lower())

                elif field_name == "tel":

                    # Ne conserver que les numéros professionnels
                    # explicitement identifiés comme tels.
                    params = field[1] if isinstance(field[1], dict) else {}

                    if params.get("type") in (
                        "work",
                        ["work"],
                    ):
                        result["phones"].append(str(value))

                elif field_name == "adr":

                    # Éviter de collecter les adresses personnelles.
                    params = field[1] if isinstance(field[1], dict) else {}

                    if params.get("type") in (
                        "work",
                        ["work"],
                    ):
                        result["addresses"].append(
                            json_safe(value)
                        )

            return result

        def process_entities(entities, parent_roles=None):

            if not isinstance(entities, list):
                return

            for entity in entities:

                if not isinstance(entity, dict):
                    continue

                roles = entity.get("roles", [])

                if not isinstance(roles, list):
                    roles = []

                for role in roles:

                    role = str(role).lower()

                    if role not in (
                        "registrant",
                        "administrative",
                        "technical",
                        "abuse",
                        "registrar",
                        "billing",
                        "legal",
                    ):
                        continue

                    details = extract_vcard(entity)

                    entry = {
                        "role": role,
                        "organization": details["organization"],
                        "emails": sorted(set(details["emails"])),
                        "phones": sorted(set(details["phones"])),
                        "addresses": details["addresses"],
                        "source": "RDAP",
                    }

                    if entry not in contacts:
                        contacts.append(entry)

                process_entities(entity.get("entities", []), roles)

        try:

            rdap = self.report.get("rdap", {})

            if isinstance(rdap, dict):

                process_entities(rdap.get("entities", []))

            # Complément WHOIS : uniquement les adresses génériques.
            whois_data = self.report.get("whois", {})

            if isinstance(whois_data, dict):

                emails = whois_data.get("emails", [])

                if isinstance(emails, str):
                    emails = [emails]

                if isinstance(emails, list):

                    generic_emails = sorted({
                        email.strip().lower()
                        for email in emails
                        if is_generic_email(email)
                    })

                    if generic_emails:

                        contacts.append({
                            "role": "public_contact",
                            "organization": whois_data.get("org"),
                            "emails": generic_emails,
                            "phones": [],
                            "addresses": [],
                            "source": "WHOIS",
                        })

            self.report["contacts"] = {
                "enabled": True,
                "status": "success",
                "count": len(contacts),
                "data": contacts,
                "note": (
                    "Contacts professionnels publiquement disponibles. "
                    "Les coordonnées personnelles nominatives ne sont "
                    "pas collectées."
                ),
            }

            logger.info(
                "Contacts professionnels identifiés : %s",
                len(contacts),
            )

        except Exception as exc:

            self.add_error("CONTACT INTELLIGENCE", exc)

            self.report["contacts"] = {
                "enabled": True,
                "status": "error",
                "count": 0,
                "data": [],
            }

        sections = [
            "whois",
            "rdap",
            "contacts",
            "dns",
            "discovered",
            "sources",
            "hosts",
            "tls",
            "http",
            "errors",
        ]
    # --------------------------------------------------------
    # CONTACT INTELLIGENCE
    # --------------------------------------------------------

    def collect_contacts(self):

        if not ENABLE_CONTACT_INTELLIGENCE:
            self.report["contacts"] = {
                "enabled": False,
                "status": "disabled",
                "data": [],
            }
            return

        contacts = []

        generic_prefixes = {
            "abuse",
            "security",
            "admin",
            "administrator",
            "hostmaster",
            "webmaster",
            "postmaster",
            "support",
            "contact",
            "info",
            "noc",
            "technical",
            "privacy",
        }

        def is_generic_email(email):

            if not isinstance(email, str):
                return False

            email = email.strip().lower()

            if "@" not in email:
                return False

            local_part = email.split("@", 1)[0]

            return (
                local_part in generic_prefixes
                or any(
                    local_part.startswith(prefix + "+")
                    for prefix in generic_prefixes
                )
            )

        def extract_vcard(entity):

            result = {
                "organization": None,
                "role": None,
                "emails": [],
                "phones": [],
                "addresses": [],
            }

            vcard = entity.get("vcardArray")

            if not isinstance(vcard, list) or len(vcard) < 2:
                return result

            for field in vcard[1]:

                if not isinstance(field, list) or len(field) < 4:
                    continue

                field_name = str(field[0]).lower()
                value = field[3]

                if field_name == "org":

                    if isinstance(value, list):
                        result["organization"] = " ".join(
                            str(x) for x in value
                        )
                    else:
                        result["organization"] = str(value)

                elif field_name == "kind":

                    result["role"] = str(value)

                elif field_name == "email":

                    if is_generic_email(value):
                        result["emails"].append(value.lower())

                elif field_name == "tel":

                    # Ne conserver que les numéros professionnels
                    # explicitement identifiés comme tels.
                    params = field[1] if isinstance(field[1], dict) else {}

                    if params.get("type") in (
                        "work",
                        ["work"],
                    ):
                        result["phones"].append(str(value))

                elif field_name == "adr":

                    # Éviter de collecter les adresses personnelles.
                    params = field[1] if isinstance(field[1], dict) else {}

                    if params.get("type") in (
                        "work",
                        ["work"],
                    ):
                        result["addresses"].append(
                            json_safe(value)
                        )

            return result

        def process_entities(entities, parent_roles=None):

            if not isinstance(entities, list):
                return

            for entity in entities:

                if not isinstance(entity, dict):
                    continue

                roles = entity.get("roles", [])

                if not isinstance(roles, list):
                    roles = []

                for role in roles:

                    role = str(role).lower()

                    if role not in (
                        "registrant",
                        "administrative",
                        "technical",
                        "abuse",
                        "registrar",
                        "billing",
                        "legal",
                    ):
                        continue

                    details = extract_vcard(entity)

                    entry = {
                        "role": role,
                        "organization": details["organization"],
                        "emails": sorted(set(details["emails"])),
                        "phones": sorted(set(details["phones"])),
                        "addresses": details["addresses"],
                        "source": "RDAP",
                    }

                    if entry not in contacts:
                        contacts.append(entry)

                process_entities(entity.get("entities", []), roles)

        try:

            rdap = self.report.get("rdap", {})

            if isinstance(rdap, dict):

                process_entities(rdap.get("entities", []))

            # Complément WHOIS : uniquement les adresses génériques.
            whois_data = self.report.get("whois", {})

            if isinstance(whois_data, dict):

                emails = whois_data.get("emails", [])

                if isinstance(emails, str):
                    emails = [emails]

                if isinstance(emails, list):

                    generic_emails = sorted({
                        email.strip().lower()
                        for email in emails
                        if is_generic_email(email)
                    })

                    if generic_emails:

                        contacts.append({
                            "role": "public_contact",
                            "organization": whois_data.get("org"),
                            "emails": generic_emails,
                            "phones": [],
                            "addresses": [],
                            "source": "WHOIS",
                        })

            self.report["contacts"] = {
                "enabled": True,
                "status": "success",
                "count": len(contacts),
                "data": contacts,
                "note": (
                    "Contacts professionnels publiquement disponibles. "
                    "Les coordonnées personnelles nominatives ne sont "
                    "pas collectées."
                ),
            }

            logger.info(
                "Contacts professionnels identifiés : %s",
                len(contacts),
            )

        except Exception as exc:

            self.add_error("CONTACT INTELLIGENCE", exc)

            self.report["contacts"] = {
                "enabled": True,
                "status": "error",
                "count": 0,
                "data": [],
            }

# ============================================================
# CARTOGRAPHIE
# ============================================================

def export_map(report, output_path):

    if not PYVIS_AVAILABLE:
        logger.warning("PyVis non installé.")
        return False

    network = Network(
        height="750px",
        width="100%",
        directed=True,
        bgcolor="#ffffff",
    )

    domain = report["domain"]

    network.add_node(
        domain,
        label=domain,
        color="#1f4e79",
        size=30,
    )

    ip_nodes = set()

    for host in report["hosts"]:

        hostname = host["hostname"]

        network.add_node(
            hostname,
            label=hostname,
            color="#4f81bd",
        )

        network.add_edge(
            domain,
            hostname,
            label="hôte",
        )

        for ip in host.get("A", []) + host.get("AAAA", []):

            if ip not in ip_nodes:

                network.add_node(
                    ip,
                    label=ip,
                    color="#70ad47",
                    shape="box",
                )

                ip_nodes.add(ip)

            network.add_edge(
                hostname,
                ip,
                label="résolution DNS",
            )

    network.write_html(
        str(output_path),
        notebook=False,
    )

    return True


# ============================================================
# HISTORIQUE HTML
# ============================================================

def export_timeline(root, domain, output_path):

    events_path = (
        root
        / safe_filename(domain)
        / "history"
        / "events"
        / "events.jsonl"
    )

    rows = []

    if events_path.exists():

        for line in events_path.read_text(
            encoding="utf-8"
        ).splitlines():

            try:

                event = json.loads(line)

                rows.append(
                    "<tr><td>"
                    + html.escape(str(event.get("date", "")))
                    + "</td><td>"
                    + html.escape(str(event.get("type", "")))
                    + "</td><td><pre>"
                    + html.escape(json.dumps(event, ensure_ascii=False))
                    + "</pre></td></tr>"
                )

            except json.JSONDecodeError:
                continue

    page = """
    <!DOCTYPE html>
    <html lang="fr">
    <meta charset="UTF-8">
    <title>Historique</title>
    <style>
    body{font-family:Arial;margin:30px}
    table{border-collapse:collapse;width:100%}
    td,th{border:1px solid #ccc;padding:8px}
    pre{white-space:pre-wrap}
    </style>
    <h1>Historique - """ + html.escape(domain) + """</h1>
    <table>
    <tr><th>Date</th><th>Événement</th><th>Détails</th></tr>
    """ + "".join(rows) + """
    </table>
    </html>
    """

    output_path.write_text(
        page,
        encoding="utf-8",
    )


# ============================================================
# CONFIGURATION ET CONTRÔLE
# ============================================================

def check_configuration():

    logger.info("Vérification des dépendances et de la configuration.")

    checks = {
        "python-whois": WHOIS_AVAILABLE,
        "dnspython": DNS_AVAILABLE,
        "reportlab": REPORTLAB_AVAILABLE,
        "pyvis": PYVIS_AVAILABLE,
    }

    for name, available in checks.items():

        logger.info(
            "%s : %s",
            name,
            "disponible" if available else "absent",
        )

    if not os.getenv("VIRUSTOTAL_API_KEY"):
        logger.info("VirusTotal : clé API non configurée.")

    if not os.getenv("SECURITYTRAILS_API_KEY"):
        logger.info("SecurityTrails : clé API non configurée.")


# ============================================================
# ARGUMENTS
# ============================================================

def build_parser():

    parser = argparse.ArgumentParser(
        description=(
            "Domain Intelligence V4 - "
            "Reconnaissance passive de domaines"
        )
    )

    parser.add_argument(
        "domain",
        nargs="?",
        help="Domaine à analyser",
    )

    parser.add_argument(
        "--out",
        default=str(OUTPUT_ROOT),
        help="Dossier de sortie",
    )

    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Désactive le PDF",
    )

    parser.add_argument(
        "--no-html",
        action="store_true",
        help="Désactive le HTML",
    )

    parser.add_argument(
        "--map",
        action="store_true",
        help="Génère la cartographie PyVis",
    )

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--passive",
        action="store_true",
        help="Reconnaissance passive uniquement (mode par défaut)",
    )
    mode_group.add_argument(
        "--active",
        action="store_true",
        help="Reconnaissance active : résolution des hôtes, TLS/HTTP et scan TCP limité",
    )

    parser.add_argument(
        "--no-active-web",
        action="store_true",
        help="En mode --active, désactive les observations TLS et HTTP (le scan TCP reste actif)",
    )

    parser.add_argument(
        "--check-config",
        action="store_true",
        help="Vérifie la configuration",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Active les logs détaillés",
    )

    return parser



# ============================================================
# MAIN
# ============================================================

def main():

    parser = build_parser()

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.check_config:

        check_configuration()

        return 0

    if args.no_active_web and not args.active:
        parser.error("--no-active-web ne peut être utilisé qu'avec --active.")

    if not args.domain:

        parser.error(
            "Veuillez préciser un domaine à analyser."
        )

    try:

        domain = normalize_domain(args.domain)

    except ValueError as exc:

        logger.error("%s", exc)

        return 2

    root = Path(args.out).expanduser().resolve()

    output_dir = create_output_directory(
        domain,
        root,
    )

    collector = DomainCollector(domain)

    try:

        if args.active:
            logger.warning(
                "Reconnaissance active sur %s : utilisez cette option uniquement "
                "sur un domaine et des systèmes pour lesquels vous avez une autorisation.",
                domain,
            )

        report = collector.run(
            active=args.active,
            active_web=not args.no_active_web,
        )

        # JSON
        write_json(
            report,
            output_dir / "rapport.json",
        )

        # HTML
        if not args.no_html:

            export_html(
                report,
                output_dir / "rapport.html",
            )

        # PDF
        if not args.no_pdf:

            if REPORTLAB_AVAILABLE:

                export_pdf(
                    report,
                    output_dir / "rapport.pdf",
                )

            else:

                logger.warning(
                    "PDF non généré : reportlab absent."
                )

        # Cartographie
        if args.map:

            export_map(
                report,
                output_dir / "cartographie.html",
            )

        # Historique
        save_history(
            report,
            root,
            output_dir,
        )

        # Timeline
        export_timeline(
            root,
            domain,
            output_dir / "historique.html",
        )

        logger.info("Analyse terminée.")

        logger.info(
            "Domaine : %s",
            domain,
        )

        logger.info(
            "Sous-domaines : %s",
            len(report["discovered"]),
        )

        logger.info(
            "Hôtes : %s",
            len(report["hosts"]),
        )

        logger.info(
            "Erreurs : %s",
            len(report["errors"]),
        )

        logger.info(
            "Dossier de résultats : %s",
            output_dir,
        )

        return 0

    except KeyboardInterrupt:

        logger.warning(
            "Analyse interrompue par l'utilisateur."
        )

        return 130

    except Exception:

        logger.exception(
            "Erreur pendant l'analyse."
        )

        return 1

    finally:

        collector.close()


if __name__ == "__main__":

    raise SystemExit(main())
