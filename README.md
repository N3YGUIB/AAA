# Challenge  AAA -- Dashboard de Monitoring

## Description

Ce projet est un **dashboard de monitoring système** développé en Python.  
Il collecte des informations essentielles sur la machine et génère un **rapport HTML stylé** pour visualiser :

- Nom et OS de la machine
- Uptime (jours, heures, minutes, secondes)
- Utilisateurs connectés
- Adresse IP locale
- Informations CPU et RAM
- Top 3 des processus les plus gourmands en CPU et RAM
- Analyse des fichiers dans le dossier utilisateur (txt, py, pdf, jpg, html, css)

---

## Prérequis

- Python 3.7 ou supérieur  
- Modules Python :

```bash
pip install psutil jinja2 distro
```

---

## Installation

```bash
git clone https://github.com/N3YGUIB/AAA
cd AAA/
```

Commandes pour installer les dépendances:

```bash
pip install psutil jinja2 distro
```
---

## Utilisation

```bash
python monitor.py
```
Ouvrir index.html dans le navigateur

Après exécution, un fichier index.html sera généré à la racine du projet.
Ouvrez-le dans un navigateur pour visualiser le dashboard complet.

---

## Fonctionnalités

- Affichage des informations système (nom, OS, uptime, utilisateurs)
- Récupération de l’adresse IP locale
- Informations CPU : cœurs, fréquence, pourcentage d’utilisation
- Informations RAM : totale, utilisée, pourcentage
- Top 3 des processus CPU et RAM
- Analyse des fichiers utilisateur par extension (.txt, .py, .pdf, .jpg, .html, .css)

Génération d’un dashboard HTML avec mise en forme CSS

---

## Captures d'écran

  

## Difficultés rencontrées

- Les calculs précis de l’uptime en jours, heures, minutes et secondes
- Le Tri des processus selon l’utilisation CPU et RAM
- Collecter l'adresse IP
- Le Nombre d'utilisateur connecté

---

## Améliorations possible

- Ajouter un graphique dynamique pour l’utilisation CPU et RAM
- Afficher l'interface en temps réel
- Ajouter un export PDF du dashboard

---

## Auteur 

### Neyguib & Mohray
