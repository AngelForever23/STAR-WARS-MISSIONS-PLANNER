from Recursos_Alianza import recursos_alianza
from musica_sonidos import sonido2

# Importación de la limpieza de la terminal
import os
import time
import sys
def limpiar_terminal():
    os.system('cls')
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame"

misiones_planificadas = []

# Guarda una misión agendada en el estado global
def agregar_mision_para_agendar(id_mision, nombre_mision, dia_semana, recursos_usados_ids):
    mision_info = {
        "id": id_mision,
        "nombre": nombre_mision,
        "dia": dia_semana,
        "recursos": recursos_usados_ids
    }
    misiones_planificadas.append(mision_info)

# Retorna todas las misiones agendadas
def obtener_misiones_agendadas():
    return misiones_planificadas

def eliminar_mision_agendada(indice):
    # Elimina una misión agendada por su índice
    if 0 <= indice < len(misiones_planificadas):
        return misiones_planificadas.pop(indice)
    return None

def mostrar_misiones_agendadas():
    # Verificamos en caso que no haigan misiones agendadas
    if len(misiones_planificadas) < 1:
        limpiar_terminal()
        print("=====================================")
        print("NO HAY MISIONES AGENDADAS TODAVÍA 📭")
        print("=====================================")
        input("\nPresiona Enter ↩️  Para regresar el Menú Principal")
        sonido2.play()
        limpiar_terminal()
        return
    # Si hay misiones agendadas entonces las mostramos
    limpiar_terminal()
    print("============== [Misiones Agendadas 📬] ==============")
    numero = 1
    for x, mision_datos in enumerate(misiones_planificadas):
        print(f"{numero}. ❇️  Misión: {mision_datos["nombre"]}")
        print(f"▶ Bando 🚩 : Alianza 🪯 .")
        print(f"▶ 🆔: {mision_datos["id"]}.")
        print(f"▶ Agenda 🗓️ : El {mision_datos["dia"]}.")
        print(f"▶ Duración ⏳: 1 día.")
        print(f"▶ Recursos usados 📦:")
        # Mostrar los nombres de los recursos agendados en la misión
        for recurso_id in mision_datos['recursos']:
            for recurso in recursos_alianza:
                if recurso.id == recurso_id:
                    print(f"-> {recurso.nombre}")
                    break
        print("=====================================================")
        numero += 1
    input("\nPresiona Enter ↩️  para volver al menú principal")
    sonido2.play()
    limpiar_terminal()
    return