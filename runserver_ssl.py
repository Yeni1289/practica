import os
import webbrowser
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practica.settings')

# Abre el navegador automáticamente en HTTPS
webbrowser.open('https://192.168.10.159:8000')

# Ejecuta el servidor SSL
call_command('runsslserver', '0.0.0.0:8000')
