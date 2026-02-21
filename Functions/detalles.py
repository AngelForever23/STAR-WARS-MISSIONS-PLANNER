import Modules.bando as bando
from Functions.listar_misiones import misiones_planificadas_alianza,misiones_planificadas_imperio
from Models.recursos import recursos_alianza,recursos_imperio
from Modules.utilidades import limpiar_terminal

from Modules.musica_sonidos import sonido1
from Modules.musica_sonidos import sonido2
from Modules.musica_sonidos import sonido3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame"

from colorama import Fore, Back, Style, init # Importar librería de colores para strings
init(autoreset=True)

def ver_detalles():
    limpiar_terminal()
    
    if bando.Alianza == True:
        while True:
            try: # El usuario selecciona que desea hacer
                print("==============================")
                print("| VER DETALLES SOBRE 👀 ...  |")
                print("| [1] ❇️  Misiones Agendadas  |")
                print("| [2] 📦 Recursos            |")
                print("==============================")
                print("\n[-1] Volver Atrás ↩️")
                respuesta = int(input("\n▶  "))
                
                if respuesta == -1:
                    limpiar_terminal()
                    sonido2.play()
                    return
                
                if respuesta < 1 or respuesta > 2:
                    limpiar_terminal()
                    sonido3.play()
                    print("=======================================================")
                    print("| ⚠️  Error. El índice introducido está fuera de rango |")
                    print("=======================================================\n")
                    continue
                
            except ValueError:
                limpiar_terminal()
                sonido3.play()
                print("====================================================")
                print("| ❌ Opción incorrecta. Introduce un número válido |")
                print("====================================================\n")
                continue
            
            else:
                if respuesta == 1: # Excepción (No hay misiones agendadas)
                    
                    if len(misiones_planificadas_alianza) < 1:
                        limpiar_terminal()
                        sonido1.play()
                        print("========================================")
                        print("| NO HAY MISIONES AGENDADAS TODAVÍA 📭 |")
                        print("========================================")
                        input("\nPresiona Enter ↩️  para retroceder. ")
                        sonido2.play()
                        limpiar_terminal()
                        continue
                    
                    else: # Mostrar las misiones que se agendaron y los recursos que se usaron
                        sonido1.play()
                        limpiar_terminal()
                        print("================ INFO DE MISIONES ❇️  ===============")
                        for x, mision_datos in enumerate(misiones_planificadas_alianza):
                            print("|--------------------------------------------------|")
                            print(f"| ❇️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos["nombre"]}")
                            print(f"| 🗓️  {Fore.BLUE}{Style.BRIGHT}Agenda{Style.RESET_ALL}: El {mision_datos["dia"]} | Duración ⏳: 1 día.")
                            print(f"| 📦 {Fore.YELLOW}{Style.BRIGHT}Recursos usados{Style.RESET_ALL}:                                       ")
                            # Mostrar los nombres de los recursos agendados en la misión
                            for recurso_id in mision_datos['recursos']:
                                for recurso in recursos_alianza:
                                    if recurso.id == recurso_id:
                                        print(f"| --> {recurso.nombre_inventario}")
                                        break
                        print("====================================================")
                        input("\nPresiona Enter ↩️  para retroceder. ")
                        limpiar_terminal()
                        sonido2.play()
                        continue
                
                
                if respuesta == 2: # Mostrar la agenda de los recursos
                    sonido1.play()
                    limpiar_terminal()
                    while True:
                        try:
                            print("============================================ INFO DE RECURSOS 📦 ============================================")
                            contador = 0
                            num = 0
                            for x in range(len(recursos_alianza)):
                                print(f"| {num}. {Fore.YELLOW}{Style.BRIGHT}{recursos_alianza[contador].nombre_inventario}{Style.RESET_ALL} {recursos_alianza[contador].tipo_recurso} | {recursos_alianza[contador].descripcion}")
                                contador += 1
                                num += 1
                            print("=============================================================================================================")
                            
                            print("\nSelecciona el índice del recurso para ver su agenda 📆")
                            print("[-1] Volver Atrás ↩️")
                            indice = int(input("\n▶  ")) # El usuario selecciona un recurso
                        
                            if indice == -1:
                                limpiar_terminal()
                                sonido2.play()
                                break
                        
                            if indice < 0 or indice > len(recursos_alianza) - 1:
                                limpiar_terminal()
                                sonido3.play()
                                print("===================================================================")
                                print(f"| ⚠️  Error. Selecciona los números entre (0 - {len(recursos_alianza) - 1}) para continuar. |")
                                print("===================================================================\n")
                                continue
                        
                        except ValueError:
                            limpiar_terminal()
                            sonido3.play()
                            print("====================================================")
                            print("| ❌ Opción incorrecta. Introduce un número válido |")
                            print("====================================================\n")
                            continue
                        
                        else: # Mostramos la agenda del recurso seleccionado
                            
                            agenda_recurso_seleccionado = recursos_alianza[indice].agenda
                            limpiar_terminal()
                            sonido1.play()
                            resource = recursos_alianza[indice].nombre
                            print("=========================================")
                            print(f"| 📆  Agenda de {resource}")
                            print("=========================================")
                            
                            for y in agenda_recurso_seleccionado.items():
                                dia = y[0]
                                valor = y[1]
                            
                                if len(valor) == 0:
                                    valor = "Libre"
                            
                                print(f"| {dia} : {valor}")
                        
                            contador += 1
                            num += 1
                        print("=========================================")
                        input("\nPresiona Enter ↩️  Para Volver Atrás. ")
                        sonido2.play()
                        limpiar_terminal()
                        continue
    
    
    if bando.Imperio == True:
        while True:
            try: # El usuario selecciona que desea hacer
                print("==============================")
                print("| VER DETALLES SOBRE 👀 ...  |")
                print("| [1] ❇️  Misiones Agendadas  |")
                print("| [2] 📦 Recursos            |")
                print("==============================")
                print("\n [-1] Volver atrás ↩️")
                
                respuesta = int(input("\n▶  "))
                
                if respuesta == -1:
                    limpiar_terminal()
                    sonido2.play()
                    return
                
                if respuesta < 1 or respuesta > 2:
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
            
            else:
                if respuesta == 1: # Excepción (No hay misiones agendadas)
                    
                    if len(misiones_planificadas_imperio) < 1:
                        limpiar_terminal()
                        sonido1.play()
                        print("========================================")
                        print("| NO HAY MISIONES AGENDADAS TODAVÍA 📭 |")
                        print("========================================")
                        input("\nPresiona Enter ↩️  para retroceder. ")
                        sonido2.play()
                        limpiar_terminal()
                        continue
                    
                    else: # Mostrar las misiones que se agendaron y los recursos que se usaron
                        sonido1.play()
                        limpiar_terminal()
                        print("===================== INFO DE MISIONES ✳️  ===================")
                        print("|-----------------------------------------------------------")
                        for x, mision_datos in enumerate(misiones_planificadas_imperio):
                            print(f"| ✳️  {Fore.GREEN}{Style.BRIGHT}Misión{Style.RESET_ALL}: {mision_datos["nombre"]}")
                            print(f"| 🗓️  {Fore.BLUE}{Style.BRIGHT}Agenda{Style.RESET_ALL}: El {mision_datos["dia"]} | Duración ⏳: 1 día.")
                            print(f"| 📦 {Fore.YELLOW}{Style.BRIGHT}Recursos usados{Style.RESET_ALL}:                                       ")
                            # Mostrar los nombres de los recursos agendados en la misión
                            for recurso_id in mision_datos['recursos']:
                                for recurso in recursos_imperio:
                                    if recurso.id == recurso_id:
                                        print(f"| --> {recurso.nombre_inventario}")
                                        break
                            print("|-----------------------------------------------------------")
                        print("=============================================================")
                        input("\nPresiona Enter ↩️  para retroceder. ")
                        limpiar_terminal()
                        sonido2.play()
                        continue
                
                
                if respuesta == 2: # Mostrar la agenda de los recursos
                    sonido1.play()
                    limpiar_terminal()
                    while True:
                        try:
                            print("============================================ INFO DE RECURSOS 📦 ============================================")
                            contador = 0
                            num = 0
                            for x in range(len(recursos_imperio)):
                                print(f"{num}. {Fore.YELLOW}{Style.BRIGHT}{recursos_imperio[contador].nombre_inventario}{Style.RESET_ALL} {recursos_imperio[contador].tipo_recurso} | {recursos_imperio[contador].descripcion}")
                                contador += 1
                                num += 1
                            print("=============================================================================================================")
                            
                            print("\nSelecciona el índice del recurso para ver su agenda 📆")
                            print("[-1] Volver Atrás ↩️")
                            indice = int(input("\n▶  ")) # El usuario selecciona un recurso
                        
                            if indice == -1:
                                limpiar_terminal()
                                sonido2.play()
                                break
                        
                            if indice < 0 or indice > len(recursos_imperio) - 1:
                                limpiar_terminal()
                                sonido3.play()
                                print("==================================================================")
                                print(f"| ⚠️  Error. Selecciona los números entre (0 - {len(recursos_imperio) - 1}) para continuar. |")
                                print("==================================================================\n")
                                continue
                        
                        except ValueError:
                            limpiar_terminal()
                            sonido3.play()
                            print("======================================================")
                            print("| ❌ Opción incorrecta. Introduce un número válido |")
                            print("======================================================\n")
                            continue
                        
                        else: # Mostramos la agenda del recurso seleccionado
                            
                            agenda_recurso_seleccionado = recursos_imperio[indice].agenda
                            limpiar_terminal()
                            sonido1.play()
                            resource = recursos_imperio[indice].nombre
                            print("=========================================")
                            print(f"| 📆  Agenda de {resource}")
                            print("=========================================")
                            
                            for y in agenda_recurso_seleccionado.items():
                                dia = y[0]
                                valor = y[1]
                            
                                if len(valor) == 0:
                                    valor = "Libre"
                            
                                print(f"| {dia} : {valor}")
                        
                            contador += 1
                            num += 1
                        print("=========================================")
                        input("\nPresiona Enter ↩️  Para Volver Atrás. ")
                        sonido2.play()
                        limpiar_terminal()
                        continue