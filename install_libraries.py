import subprocess
import sys

# Si no tienes las librerías necesarias, puedes descargarlas automáticamente incializando este módulo
# NECESITAS CONEXIÓN A INTERNET PARA HACER ESTO.

print("\n🚀 Instalando dependencias de Star Wars Missions Planner...\n")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
print("\n✅ ¡Instalación completa! Ejecuta: python main_controller.py\n")