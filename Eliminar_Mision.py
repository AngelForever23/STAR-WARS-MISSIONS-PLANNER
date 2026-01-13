from listar_misiones import misiones_planificadas
from Misiones_Alianza import misiones_alianza
from Recursos_Alianza import recursos_alianza
from musica_sonidos import sonido1
from musica_sonidos import sonido2
from musica_sonidos import sonido3


# Importación de los colores para los textos
from colorama import Fore, Back, Style, init
init(autoreset=True)


papelera_reciclaje = [] # Aquí se añaden las misiones que vayamos eliminando

def obtener_misiones_eliminadas(misiones_eliminadas):
    papelera_reciclaje.append(misiones_eliminadas)

# Importación de la limpieza de la terminal
import os
import time
import sys
def limpiar_terminal():
    os.system('cls')
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame"

def eliminar_mision():
    if len(misiones_planificadas) == 0:
        print("===========================================")
        print("No hay misiones agendadas para eliminar ⚠️")
        print("===========================================")
        input("\nPresiona Enter ↩️  para volver al Menú Principal  ")
        sonido2.play()
        limpiar_terminal()
        return
    else:
        while True:
            try:
                numero = 0
                print("=============== ELIMINAR AGENDA 🗑️  ===============")
                print("--------------------------------------------------")
                for x, mision_datos in enumerate(misiones_planificadas):
                    print(f"{numero}. ❇️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos["nombre"]}")
                    print("--------------------------------------------------")
                    numero += 1
                
                print("\nIntroduce el índice de la Misión para eliminarla.")
                print("[-1] Volver Atrás ↩️")
                indice = int(input("▶  "))
                
                if indice == -1:
                    sonido2.play()
                    limpiar_terminal()
                    return
                
                if indice < 0 or indice > len(misiones_planificadas) - 1:
                    limpiar_terminal()
                    sonido3.play()
                    print("=====================================================")
                    print("⚠️  Error. El índice introducido está fuera de rango.")
                    print("=====================================================\n")
                    continue
            
            except ValueError:
                limpiar_terminal()
                sonido3.play()
                print("==================================================")
                print("❌ Opción incorrecta. Introduce un número válido")
                print("==================================================\n")
                continue
            
            else:
                # Si no ocurrió ninguna excepción borramos la misión de la lista de misiones planificadas
                sonido1.play()
                limpiar_terminal()
                while True:
                    try:
                        print(f"¿Estás seguro que deseas eliminar la misión \n{mision_datos["nombre"]} de la agenda?")
                        print("\n1 Borrar 🗑️ \n2 Cancelar ❌")
                        respuesta = int(input("▶ "))
                        
                        if respuesta < 1 or respuesta > 2:
                            limpiar_terminal()
                            sonido3.play()
                            print("==============================================")
                            print("Error ⚠️  selecciona (1) o (2) para continuar.")
                            print("==============================================\n")
                            continue
                        
                        if respuesta == 2:
                            limpiar_terminal()
                            sonido2.play()
                            return
                    
                    except ValueError:
                        limpiar_terminal()
                        sonido3.play()
                        print("==================================================")
                        print("❌ Opción incorrecta. Introduce un número válido")
                        print("==================================================\n")
                        continue
                    
                    else:
                        misiones_alianza.append(papelera_reciclaje[indice]) # Regresamos la misión a las misiones de la Alianza
                        
                        # mision_seleccionada es un diccionario de la forma:
                        # {id,nombre,dia,recursos}
                        mision_seleccionada = misiones_planificadas[indice]
                        
                        recursos_mision = mision_seleccionada['recursos'] # Lista de IDs de los recursos usados en la misión
                        dia_mision = mision_seleccionada['dia'] # Día agendado para la misión
                        id_mision = mision_seleccionada['id'] # Id de la Misión
                        
                        for recurso_id in set(recursos_mision): # Recorrer los Ids de los recursos (no repetidos) usados en la misión
                            for r in recursos_alianza:
                                if r.id == recurso_id: # Encuentra una coincidencia
                                    cantidad_liberar = recursos_mision.count # ¿Cúantas veces aparece?
                                    
                                    for x in range(cantidad_liberar): # Eliminar la cantidad exacta
                                        if id_mision in r.agenda[dia_mision]:
                                            r.agenda[dia_mision].remove(id_mision)
                        
                        misiones_planificadas.pop(indice) # Eliminamos la mision de la Agenda
                        limpiar_terminal()
                        print("La Misión ha sido eliminada con éxito.")
                        input("\nPresiona Enter ↩️  para continuar  ")
                        sonido2.play()
                        limpiar_terminal()
                        return