# config.py

from dotenv import load_dotenv
import os

# Cargar las variables desde el archivo .env
load_dotenv()

# Configuración extraída del archivo .env
API_KEY = os.getenv("API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
CITY_NAME = os.getenv("CITY_NAME")

