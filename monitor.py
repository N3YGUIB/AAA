#!/usr/bin/env python3

import psutil
import socket
import os
import time
import distro
import pprint
from jinja2 import Template


def get_system_info():
    # ---------------------------------INFO SYSTEM------------------------------------------
    system_name = socket.gethostname()                  # Nom de la machine
    os_name = distro.name()                             # Récupère le nom de la distribution
    os_version = distro.version()                       # Récupère la version de la distribution

    # -----------------------------------INFO UPTIME-------------------------------------------
    
    uptime_seconds = time.time() - psutil.boot_time()       # Temps depuis le démarrage
    days = uptime_seconds // (24 * 3600)                    # Nombre de jours
    hours = (uptime_seconds % (24 * 3600)) // 3600          # Nombre d'heures restantes
    minutes = (uptime_seconds % 3600) // 60                 # Nombre de minutes restantes
    seconds = uptime_seconds % 60                           # Nombre de secondes restantes

    uptime = f"{int(days)} jours, {int(hours)} heures, {int(minutes)} minutes, {int(seconds)} secondes"

    # -----------------------------------INFO USER-------------------------------------------

    users = psutil.users()

    if users:
        user_count = len(users)
    else:
        user_count = 1 
                        
    # -----------------------------------INFO IP-------------------------------------------

    def get_local_ip():
        interfaces = psutil.net_if_addrs()
        for iface_addrs in interfaces.values():
            for addr in iface_addrs:
                if addr.family == socket.AF_INET and addr.address != "127.0.0.1":
                    return addr.address
        
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip if ip else "127.0.0.1"
    
    ip_address = get_local_ip()

    # -----------------------------------INFO CPU-------------------------------------------

    cpu_cores = psutil.cpu_count(logical=False)                         # Nombre de coeurs
    cpu_frequency = round(psutil.cpu_freq().current / 1000, 2)          # Fréquence 
    cpu_usage = round(psutil.cpu_percent(interval=1), 2)                # Pourcentage d'utilisation

    # --------------------------------- INFO MEMOIRE-------------------------------------------
    memory = psutil.virtual_memory()
    total_ram = round(memory.total / (1024 ** 3), 2)  # RAM totale
    used_ram = round(memory.used / (1024 ** 3), 2)    # RAM utilisé
    ram_usage = round(memory.percent, 2)              # Pourcentage de RAM utilisé

    # Récupérer les 3 processus les plus gourmands

    def get_top_processes(delay=1, limit=3):
        processes = []

        # Initialisation CPU
        for p in psutil.process_iter(['pid', 'name']):
            p.cpu_percent(None)

        time.sleep(delay)

        # Mesure réelle
        for p in psutil.process_iter(['pid', 'name', 'memory_percent']):
            cpu = p.cpu_percent(None)

            if cpu > 0:
                processes.append({
                    "pid": p.info['pid'],
                    "name": p.info['name'],
                    "cpu": cpu,
                    "memory": p.info['memory_percent'],
                })

        top_cpu = sorted(processes, key=lambda p: p['cpu'], reverse=True)[:limit]
        top_mem = sorted(processes, key=lambda p: p['memory'], reverse=True)[:limit]

        return top_cpu, top_mem


    top_cpu, top_mem = get_top_processes()

    top_processes_cpu = [
        f"{p['name']}: {round(p['cpu'], 2)}% CPU"
        for p in top_cpu
    ]

    top_processes_memory = [
        f"{p['name']}: {round(p['memory'], 2)}% RAM"
        for p in top_mem
    ]

    # Analyse des fichiers
    folder_path = os.path.expanduser("~")
    extensions = ['.txt','.py','.pdf','.jpg','.html','.css']
    file_counts = {ext: 0 for ext in extensions}

    for root, _, files in os.walk(folder_path):
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    file_counts[ext] += 1

    # Calcul des pourcentages
    total_files = sum(file_counts.values())
    file_percentages = {
        ext: (count / total_files) * 100 if total_files > 0 else 0 for ext, count in file_counts.items()
        }

    
    
    # Rassembler toute les information dans un dictionnaire
    return {
        'system_name': system_name,
        'os_name': os_name,
        'os_version': os_version,
        'uptime': uptime,
        'user_count': user_count,
        'ip_address': ip_address,
        'cpu_cores': cpu_cores,
        'cpu_frequency': cpu_frequency,
        'cpu_usage': cpu_usage,
        'total_ram': total_ram,
        'used_ram': used_ram,
        'ram_usage': ram_usage,
        'txt_count': file_counts['.txt'],
        'py_count': file_counts['.py'],
        'pdf_count': file_counts['.pdf'],
        'jpg_count': file_counts['.jpg'],
        'html_count': file_counts['.html'],
        'css_count': file_counts['.css'],
        'txt_percentage': round(file_percentages['.txt'], 2),
        'py_percentage': round(file_percentages['.py'], 2),
        'pdf_percentage': round(file_percentages['.pdf'], 2),
        'jpg_percentage': round(file_percentages['.jpg'], 2),
        'html_percentage': round(file_percentages['.html'], 2),
        'css_percentage': round(file_percentages['.css'], 2),
        'top_process_1': top_processes_cpu[0] if top_processes_cpu else "N/A",
        'top_process_2': top_processes_cpu[1] if len(top_processes_cpu) > 1 else "N/A",
        'top_process_3': top_processes_cpu[2] if len(top_processes_cpu) > 2 else "N/A",
        'top_process_memory_1': top_processes_memory[0] if top_processes_memory else "N/A",
        'top_process_memory_2': top_processes_memory[1] if len(top_processes_memory) > 1 else "N/A",
        'top_process_memory_3': top_processes_memory[2] if len(top_processes_memory) > 2 else "N/A",
        'current_time': time.strftime("%Y-%m-%d %H:%M:%S")
    }

def print_system_info(info):
    # Vérif de l'affichage des données sur le terminal
    print(f"Système : {info['system_name']}")
    print(f"OS : {info['os_name']} {info['os_version']}")
    print(f"Uptime : {info['uptime']}")
    print(f"Utilisateurs connectés : {info['user_count']}")
    print(f"Adresse IP : {info['ip_address']}")
    print(f"CPU : {info['cpu_cores']} cœurs, {info['cpu_frequency']} GHz, {info['cpu_usage']}% utilisation")
    print(f"RAM : {info['used_ram']} Go sur {info['total_ram']} Go, {info['ram_usage']}% utilisée")
    print(f"Fichiers .txt : {info['txt_count']} ({info['txt_percentage']}%)")
    print(f"Fichiers .py : {info['py_count']} ({info['py_percentage']}%)")
    print(f"Fichiers .pdf : {info['pdf_count']} ({info['pdf_percentage']}%)")
    print(f"Fichiers .jpg : {info['jpg_count']} ({info['jpg_percentage']}%)")
    print(f"Heure de génération : {info['current_time']}")
    print(f"Top 3 des processus CPU :")
    print(f"  - {info['top_process_1']}")
    print(f"  - {info['top_process_2']}")
    print(f"  - {info['top_process_3']}")
    print(f"Top 3 des processus RAM :")
    print(f"  - {info['top_process_memory_1']}")
    print(f"  - {info['top_process_memory_2']}")
    print(f"  - {info['top_process_memory_3']}")

#---------------------------------MAIN------------------------------------------

if __name__ == "__main__":
    system_info = get_system_info()
    pprint.pprint(system_info)

# ---------------------------- GENERER LA PAGE HTML ------------------------------

with open("template.html", "r") as f:
    template_content = f.read()

template = Template(template_content)
index_html = template.render(**system_info)

with open("index.html", "w") as f:
    f.write(index_html)


print("Le fichier HTML a été générer avec succès.")
