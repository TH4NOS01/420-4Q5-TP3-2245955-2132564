import os
import subprocess
import datetime

WP_DATE = "/app/wp_data"
DB_DATA = "/app/db_data"

BACKUP_DIR = "/app/backups"

BACKUP_HOST = os.environ.get("BACKUP_HOST")
BACKUP_USER = os.environ.get("BACKUP_USER")
BACKUP_PATH = os.environ.get("BACKUP_PATH")


