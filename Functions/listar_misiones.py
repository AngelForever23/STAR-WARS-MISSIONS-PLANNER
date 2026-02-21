from Modules.musica_sonidos import sonido2
from Modules.utilidades import limpiar_terminal
import Modules.bando as bando

# Importación de los colores para los textos
from colorama import Fore, Back, Style, init
init(autoreset=True)

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame"

misiones_planificadas_alianza = [] # Aquí se almacenan los datos importantes de las misiones agendadas [{ID,nombre,día,recursos}]
misiones_planificadas_imperio = []

# Guardar una misión agendada de la alianza
def agregar_mision_alianza_para_agendar(id_mision, nombre_mision, dia_semana, recursos_usados_ids):
    mision_info = {
        "id": id_mision,
        "nombre": nombre_mision,
        "dia": dia_semana,
        "recursos": recursos_usados_ids
    }
    misiones_planificadas_alianza.append(mision_info)

# Guardar una misión agendada del imperio
def agregar_mision_imperio_para_agendar(id_mision, nombre_mision, dia_semana, recursos_usados_ids):
    mision_info = {
        "id": id_mision,
        "nombre": nombre_mision,
        "dia": dia_semana,
        "recursos": recursos_usados_ids
    }
    misiones_planificadas_imperio.append(mision_info)


def mostrar_misiones_agendadas():
    if bando.Alianza == True:
        if len(misiones_planificadas_alianza) < 1: # Verificamos en caso que no haigan misiones agendadas
            limpiar_terminal()
            print("========================================")
            print("| NO HAY MISIONES AGENDADAS TODAVÍA 📭 |")
            print("========================================")
            input("\nPresiona Enter ↩️  Para regresar el Menú Principal  ")
            sonido2.play()
            limpiar_terminal()
            return
        
        # Si hay misiones agendadas entonces las mostramos
        limpiar_terminal()
        print("================ [MISIONES AGENDADAS 📬] ===============")
        print("|------------------------------------------------------|")
        for x, mision_datos in enumerate(misiones_planificadas_alianza):
            print(f"| ❇️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos["nombre"]} |")
            print("|------------------------------------------------------|")
        print("========================================================")
        input("\nPresiona Enter ↩️   para volver al menú principal ")
        sonido2.play()
        limpiar_terminal()
        return
    
    
    if bando.Imperio == True:
        if len(misiones_planificadas_imperio) < 1: # Verificamos en caso que no haigan misiones agendadas
            limpiar_terminal()
            print("========================================")
            print("| NO HAY MISIONES AGENDADAS TODAVÍA 📭 |")
            print("========================================")
            input("\nPresiona Enter ↩️  Para regresar el Menú Principal  ")
            sonido2.play()
            limpiar_terminal()
            return
        
        # Si hay misiones agendadas entonces las mostramos
        limpiar_terminal()
        print("================== [MISIONES AGENDADAS 📬] ==================")
        print("|-----------------------------------------------------------|")
        for x, mision_datos in enumerate(misiones_planificadas_imperio):
            print(f"| ❇️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos["nombre"]} |")
            print("|-----------------------------------------------------------|")
        print("=============================================================")
        input("\nPresiona Enter ↩️   para volver al menú principal ")
        sonido2.play()
        limpiar_terminal()
        return