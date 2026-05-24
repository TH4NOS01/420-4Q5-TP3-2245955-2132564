# TP3 - Infrastructure Docker et Automatisation de sauvegarde

## Memebres de l'équipe
- Baraka Nshimiye - DA : 2245955
- Thomas Perrier - DA : 2132564

## Dépôt GitHub
https://github.com/TH4NOS01/420-4Q5-TP3-2245955-2132564.git

## Adresses IP
- VM1 (Production) : 192.168.180.80
- VM2 (Sauvegarde) : 192.168.180.85

## Déploiement

```bash
git clone https://github.com/TH4NOS01/420-4Q5-TP3-2245955-2132564.git
cd 420-4Q5-TP3-2245955-2132564
cp .env.example .env
# Remplir les variables dans .env
sudo docker compose -f docker-compose.yaml up --build -d
```

## Variables d'environnement
Copier `.env.example` vers `.env` et remplir les valeurs.

## Configuration requise avant le déploiement

### Sur VM2
```bash
# Créer l'utilisateur backupuser
sudo useradd -m backupuser
sudo passwd backupuser

# Créer le dossier de sauvegarde
sudo mkdir -p /srv/backups/tp3
sudo chown backupuser:backupuser /srv/backups/tp3
```

### Sur VM1 - Clé SSH pour le conteneur maintenance
```bash
# Générer la clé SSH
sudo mkdir -p /root/.ssh/maintenance
sudo ssh-keygen -t ed25519 -C "maintenance" -f /root/.ssh/maintenance/id_ed25519 -N ""

# Afficher la clé publique à copier sur VM2
sudo cat /root/.ssh/maintenance/id_ed25519.pub
```

### Sur VM2 - Autoriser la clé SSH
```bash
sudo mkdir -p /home/backupuser/.ssh
sudo nano /home/backupuser/.ssh/authorized_keys
# Coller la clé publique de VM1

sudo chown -R backupuser:backupuser /home/backupuser/.ssh
sudo chmod 700 /home/backupuser/.ssh
sudo chmod 600 /home/backupuser/.ssh/authorized_keys
```

### État des conteneurs
```bash
sudo docker compose -f docker-compose.yaml ps
```

### Logs du conteneur maintenance
```bash
sudo docker compose -f docker-compose.yaml logs maintenance
```

### Vérifier les sauvegardes sur VM2
```bash
ssh -i /root/.ssh/maintenance/id_ed25519 backupuser@192.168.180.85 "ls -la /srv/backups/tp3/"
```

### Accéder au site
- Via reverse proxy : http://192.168.180.80:8080
- Accès direct WordPress : http://192.168.180.80:8081