from musica_sonidos import sonido2
from utilidades import limpiar_terminal

# Importación de los colores para los textos
from colorama import Fore, Back, Style, init
init(autoreset=True)

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame"

misiones_planificadas = [] # Aquí se almacenan los datos importantes de las misiones agendadas [{ID,nombre,día,recursos}]

# Guardar una misión agendada en [misiones_planificadas]
def agregar_mision_para_agendar(id_mision, nombre_mision, dia_semana, recursos_usados_ids):
    mision_info = {
        "id": id_mision,
        "nombre": nombre_mision,
        "dia": dia_semana,
        "recursos": recursos_usados_ids
    }
    misiones_planificadas.append(mision_info)


def mostrar_misiones_agendadas():
    
    if len(misiones_planificadas) < 1: # Verificamos en caso que no haigan misiones agendadas
        limpiar_terminal()
        print("=====================================")
        print("NO HAY MISIONES AGENDADAS TODAVÍA 📭")
        print("=====================================")
        input("\nPresiona Enter ↩️  Para regresar el Menú Principal  ")
        sonido2.play()
        limpiar_terminal()
        return
    
    # Si hay misiones agendadas entonces las mostramos
    limpiar_terminal()
    print("=============== [MISIONES AGENDADAS 📬] ===============")
    print("-------------------------------------------------------")
    for x, mision_datos in enumerate(misiones_planificadas):
        print(f"❇️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos["nombre"]}")
        print("-------------------------------------------------------")
    input("\nPresiona Enter ↩️   para volver al menú principal ")
    sonido2.play()
    limpiar_terminal()
    return