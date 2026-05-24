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

## Commandes de test

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
- Via nginx : http://192.168.180.80:8080
- Direct : http://192.168.180.80:8081