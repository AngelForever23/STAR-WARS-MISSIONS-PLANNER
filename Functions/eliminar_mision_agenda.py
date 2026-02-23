import Modules.bando as bando
from Functions.listar_misiones import misiones_planificadas_alianza,misiones_planificadas_imperio
from Models.misiones import misiones_alianza, misiones_imperio
from Models.recursos import recursos_alianza, recursos_imperio
from Modules.musica_sonidos import sonido1
from Modules.musica_sonidos import sonido2
from Modules.musica_sonidos import sonido3
from Functions.utilidades import limpiar_terminal

from colorama import Fore, Back, Style, init # Importar librería de colores para strings
init(autoreset=True)

papelera_reciclaje_alianza = []  # Aquí se añaden las misiones que vayamos eliminando
papelera_reciclaje_imperio = []  # Aquí se añaden las misiones que vayamos eliminando

def obtener_misiones_eliminadas_alianza(misiones_eliminadas):
    papelera_reciclaje_alianza.append(misiones_eliminadas)

def obtener_misiones_eliminadas_imperio(misiones_eliminadas):
    papelera_reciclaje_imperio.append(misiones_eliminadas)

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame".

def eliminar_mision():
    if bando.Alianza == True:
        if len(misiones_planificadas_alianza) == 0: # Excepción (No hay misiones agendadas)
            print("==============================================")
            print("| No hay misiones agendadas para eliminar ⚠️  |")
            print("==============================================")
            input("\nPresiona Enter ↩️  para volver al Menú Principal  ")
            sonido2.play()
            limpiar_terminal()
            return
        else:
            while True:
                
                try: # Mostramos las misiones para eliminar
                    numero = 0
                    
                    print("=================== ELIMINAR AGENDA 🗑️  ====================")
                    print("|---------------------------------------------------------|")
                    for x, mision_datos in enumerate(misiones_planificadas_alianza):
                        print(f"| {numero}. ❇️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos['nombre']} |")
                        print("|---------------------------------------------------------|")
                        numero += 1
                    print("===========================================================")
                    
                    print("\nIntroduce el índice de la Misión para eliminarla.")
                    print("[-1] Volver Atrás ↩️")
                    indice = int(input("\n▶  ")) # El usuario selecciona la misión que desea eliminar
                    
                    if indice == -1:
                        sonido2.play()
                        limpiar_terminal()
                        return
                    
                    if indice < 0 or indice > len(misiones_planificadas_alianza) - 1:
                        limpiar_terminal()
                        sonido3.play()
                        print("========================================================")
                        print("| ⚠️  Error. El índice introducido está fuera de rango. |")
                        print("========================================================\n")
                        continue
                
                except ValueError:
                    limpiar_terminal()
                    sonido3.play()
                    print("====================================================")
                    print("| ❌ Opción incorrecta. Introduce un número válido |")
                    print("====================================================\n")
                    continue
                
                else: # Pregunta al usuario si de verdad está seguro de eliminar
                    mision_seleccionada = misiones_planificadas_alianza[indice]
                    
                    sonido1.play()
                    limpiar_terminal()
                    
                    while True: # Confirmación para eliminar la misión
                        try:
                            print("=============================================================")
                            print(f"| {Fore.YELLOW}{Style.BRIGHT}¿Estás seguro que deseas eliminar la misión de la agenda?{Style.RESET_ALL} |  ")
                            print(f"| {mision_seleccionada['nombre']}                 |")
                            print("=============================================================")
                            print("\n[1] Borrar 🗑️ \n[2] Cancelar ❌")
                            respuesta = int(input("\n▶  "))
                            
                            if respuesta < 1 or respuesta > 2:
                                limpiar_terminal()
                                sonido3.play()
                                print("==================================================")
                                print("| Error ⚠️  selecciona [1] o [2] para continuar. |")
                                print("==================================================\n")
                                continue
                            if respuesta == 2:
                                limpiar_terminal()
                                sonido2.play()
                                return
                        
                        except ValueError:
                            limpiar_terminal()
                            sonido3.play()
                            print("======================================================")
                            print("| ❌ Opción incorrecta. Introduce un número válido |")
                            print("======================================================\n")
                            continue
                        
                        else: # Sección para eliminar la misión definitivamente
                            
                            id_mision_a_eliminar = mision_seleccionada['id']
                            
                            mision_objeto = None
                            for i, m in enumerate(papelera_reciclaje_alianza): # Buscar la misión (objeto) en la papelera
                                if m.id == id_mision_a_eliminar:
                                    mision_objeto = m
                                    break
                            
                            # Devolver la misión a las misiones disponibles
                            if mision_objeto:
                                misiones_alianza.append(mision_objeto)
                            
                            recursos_mision = mision_seleccionada['recursos']
                            dia_mision = mision_seleccionada['dia']
                            id_mision = mision_seleccionada['id']
                            
                            # Liberar los recursos de la agenda
                            for recurso_id in set(recursos_mision):  # La lista de los recursos de la misión ya no tendrán duplicados (por convertirla en conjunto)
                                for r in recursos_alianza:
                                    if r.id == recurso_id:
                                        cantidad_liberar = recursos_mision.count(recurso_id)
                                        
                                        # Eliminar la misión de la agenda del recurso
                                        for x in range(cantidad_liberar):
                                            if id_mision in r.agenda[dia_mision]:
                                                r.agenda[dia_mision].remove(id_mision)
                            
                            # Eliminar la misión de las planificadas
                            misiones_planificadas_alianza.pop(indice)
                            
                            limpiar_terminal()
                            sonido1.play()
                            print(f"{Fore.YELLOW}{Style.BRIGHT}La Misión ha sido eliminada con éxito {Style.RESET_ALL}.")
                            input("\nPresiona Enter ↩️  para continuar  ")
                            sonido2.play()
                            limpiar_terminal()
                            return
    
    
    
    
    
    if bando.Imperio == True:
        if len(misiones_planificadas_imperio) == 0: # Excepción (No hay misiones agendadas)
            print("==============================================")
            print("| No hay misiones agendadas para eliminar ⚠️  |")
            print("==============================================")
            input("\nPresiona Enter ↩️  para volver al Menú Principal  ")
            sonido2.play()
            limpiar_terminal()
            return
        else:
            while True:
                
                try: # Mostramos las misiones para eliminar
                    numero = 0
                    print("====================== ELIMINAR AGENDA 🗑️  ======================")
                    print("|--------------------------------------------------------------|")
                    for x, mision_datos in enumerate(misiones_planificadas_imperio):
                        print(f"| {numero}. ❇️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos['nombre']} |")
                        print("|--------------------------------------------------------------|")
                        numero += 1
                    print("================================================================")
                    
                    print("\nIntroduce el índice de la Misión para eliminarla.")
                    print("[-1] Volver Atrás ↩️")
                    indice = int(input("\n▶  ")) # El usuario selecciona la misión que desea eliminar
                    
                    if indice == -1:
                        sonido2.play()
                        limpiar_terminal()
                        return
                    
                    if indice < 0 or indice > len(misiones_planificadas_imperio) - 1:
                        limpiar_terminal()
                        sonido3.play()
                        print("=========================================================")
                        print("| ⚠️  Error. El índice introducido está fuera de rango. |")
                        print("=========================================================\n")
                        continue
                
                except ValueError:
                    limpiar_terminal()
                    sonido3.play()
                    print("======================================================")
                    print("| ❌ Opción incorrecta. Introduce un número válido |")
                    print("======================================================\n")
                    continue
                
                else: # Pregunta al usuario si de verdad está seguro de eliminar
                    mision_seleccionada = misiones_planificadas_imperio[indice]
                    
                    sonido1.play()
                    limpiar_terminal()
                    
                    while True: # Confirmación para eliminar la misión
                        try:
                            print("==========================================================")
                            print(f"{Fore.YELLOW}{Style.BRIGHT}¿Estás seguro que deseas eliminar la misión de la agenda?{Style.RESET_ALL}\n{mision_seleccionada['nombre']}")
                            print("==========================================================")
                            print("\n[1] Borrar 🗑️ \n[2] Cancelar ❌")
                            respuesta = int(input("\n▶  "))
                            
                            if respuesta < 1 or respuesta > 2:
                                limpiar_terminal()
                                sonido3.play()
                                print("==================================================")
                                print("| Error ⚠️  selecciona (1) o (2) para continuar. |")
                                print("==================================================\n")
                                continue
                            if respuesta == 2:
                                limpiar_terminal()
                                sonido2.play()
                                return
                        
                        except ValueError:
                            limpiar_terminal()
                            sonido3.play()
                            print("======================================================")
                            print("| ❌ Opción incorrecta. Introduce un número válido |")
                            print("======================================================\n")
                            continue
                        
                        else: # Sección para eliminar la misión definitivamente
                            
                            id_mision_a_eliminar = mision_seleccionada['id']
                            
                            mision_objeto = None
                            for i, m in enumerate(papelera_reciclaje_imperio): # Buscar la misión (objeto) en la papelera
                                if m.id == id_mision_a_eliminar:
                                    mision_objeto = m
                                    break
                            
                            # Devolver la misión a las misiones disponibles
                            if mision_objeto:
                                misiones_imperio.append(mision_objeto)
                            
                            recursos_mision = mision_seleccionada['recursos']
                            dia_mision = mision_seleccionada['dia']
                            id_mision = mision_seleccionada['id']
                            
                            # Liberar los recursos de la agenda
                            for recurso_id in set(recursos_mision):  # La lista de los recursos de la misión ya no tendrán duplicados (por convertirla en conjunto)
                                for r in recursos_imperio:
                                    if r.id == recurso_id:
                                        cantidad_liberar = recursos_mision.count(recurso_id)
                                        
                                        # Eliminar la misión de la agenda del recurso
                                        for x in range(cantidad_liberar):
                                            if id_mision in r.agenda[dia_mision]:
                                                r.agenda[dia_mision].remove(id_mision)
                            
                            # Eliminar la misión de las planificadas
                            misiones_planificadas_imperio.pop(indice)
                            
                            limpiar_terminal()
                            sonido1.play()
                            print(f"{Fore.YELLOW}{Style.BRIGHT}La Misión ha sido eliminada con éxito.{Style.RESET_ALL}")
                            input("\nPresiona Enter ↩️  para continuar  ")
                            sonido2.play()
                            limpiar_terminal()
                            return