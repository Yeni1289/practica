import os
import socket
import webbrowser
import threading
from django.core.management import execute_from_command_line

def get_local_ip():
    """Detecta automáticamente la IP local de tu Wi-Fi."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def open_browser(url):
    """Abre el navegador en la URL dada."""
    webbrowser.open_new(url)

if __name__ == "__main__":
    local_ip = get_local_ip()
    port = "8000"

    # Abre el navegador local (puedes cambiarlo a tu IP si prefieres)
    url = "http://localhost:8000/"
    if os.environ.get('RUN_MAIN') == 'true':
     threading.Timer(1, open_browser, args=[url]).start()


    # Escucha en todas las interfaces (localhost + Wi-Fi)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practica.settings")
    execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])
