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
