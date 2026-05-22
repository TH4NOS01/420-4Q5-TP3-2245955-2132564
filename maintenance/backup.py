import os
import subprocess
from datetime import datetime
WP_DATA = "/app/wp_data"
DB_DATA = "/app/db_data"

BACKUP_DIR = "/app/backups"

BACKUP_HOST = os.environ.get("BACKUP_HOST")
BACKUP_USER = os.environ.get("BACKUP_USER")
BACKUP_PATH = os.environ.get("BACKUP_PATH")


os.makedirs(BACKUP_DIR, exist_ok=True)
maintenant = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nom_archive = f"backup_{maintenant}.tar.gz"
chemin_archive = f"{BACKUP_DIR}/{nom_archive}"

print(f"Création de l'archive {nom_archive}")
subprocess.run(["tar", "-czf", chemin_archive, WP_DATA,DB_DATA])


taille = os.path.getsize(chemin_archive)
print(f"Archive créée : {nom_archive}")
print(f"Taille : {taille / 1024**2:.2f} MB")


print(f"Envoi vers VM2 ({BACKUP_HOST})")
subprocess.run(["rsync", "-avz","-e", "ssh -o StrictHostKeyChecking=no",
                chemin_archive,f"{BACKUP_USER}@{BACKUP_HOST}:{BACKUP_PATH}"                 
])
print("Envoie terminé")


print("Rotation des sauvegardes")
maintenant = datetime.now()

for fichier in os.listdir(BACKUP_DIR):
    chemin_fichier = f"{BACKUP_DIR}/{fichier}"
    age = maintenant - datetime.fromtimestamp(
        os.path.getmtime(chemin_fichier)
    )
    if age.days > 7:
        os.remove(chemin_fichier)
        print(f" le fichier suivant : {fichier} est Supprimé ")


