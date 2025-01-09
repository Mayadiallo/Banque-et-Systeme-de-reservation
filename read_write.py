import os
from datetime import datetime
import threading

FICHIER_CLIENT = "client.txt"
FICHIER_TRANSACTION = "transaction.txt"

def ecrire_client():
    with open("nom_fichier.txt", "a", encoding="utf-8") as fichier