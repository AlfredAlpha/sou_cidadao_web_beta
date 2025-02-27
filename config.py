import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'sou_cidadao')
    SECRET_KEY = os.getenv('SECRET_KEY', 'sua-chave-secreta-aqui')
    UPLOAD_FOLDER = 'static/uploads'
    EMAIL_SERVER = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')