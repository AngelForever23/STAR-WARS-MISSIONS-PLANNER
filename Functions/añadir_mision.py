from Models.recursos import recursos_alianza, recursos_imperio
from Models.misiones import misiones_alianza, misiones_imperio
from Models.restricciones_star_wars import validar_co_requisitos_alianza,validar_exclusiones_alianza,validar_co_requisitos_imperio,validar_exclusiones_imperio

from Functions.utilidades import limpiar_terminal
from Functions.utilidades import mostrar_cargando_y_limpiar

from time import sleep
from collections import Counter
from colorama import Fore, Back, Style, init # Importar librería de colores para strings
init(autoreset=True)

# Módulo pygame (para reproducir los sonidos)
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame".
import pygame
pygame.mixer.init()

# Música
from Modules.musica_sonidos import mision_exito
from Modules.musica_sonidos import light_side_mission
from Modules.musica_sonidos import light_side_menu
from Modules.musica_sonidos import dark_side_mission
from Modules.musica_sonidos import dark_side_menu

# Sonidos
from Modules.musica_sonidos import sonido1
from Modules.musica_sonidos import sonido2
from Modules.musica_sonidos import sonido3

pygame.mixer.music.stop()
limpiar_terminal()

def agendar_mision_alianza(): # Sección para seleccionar una Misión
    pygame.mixer.music.set_volume(0.5)
    
    while True:
        if len(misiones_alianza) == 0: # Excepción (Ya se asignaron todas las misiones)
            sleep(0.5)
            sonido3.play()
            pygame.mixer.music.stop()
            print("======================================")
            print("| YA NO QUEDAN MISIONES POR ASIGNAR ⚠️  |")
            print("======================================")
            print("\nNOTA: Puedes elimanar una misión planificada para \nasignarla otro día y con otros recursos.")
            input("\nPresiona Enter ↩️  para volver al Menú Principal. ")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(light_side_menu)
            pygame.mixer.music.play(-1)
            limpiar_terminal()
            return
        
        try: # Mostar las misiones disponibles
            
            print("============ MISIONES DISPONIBLES DE LA ALIANZA ❇️  ============")
            contador = 0
            numero = 0
            print("|-------------------------------------------------------------|")
            for x in range(len(misiones_alianza)): # Mostramos las misiones que tenemos disponible ahora
                print(f"| [{numero}] {Style.BRIGHT}{misiones_alianza[contador].nombre}{Style.RESET_ALL} | ID: [{misiones_alianza[contador].id}]  |")
                contador += 1
                numero += 1
                print("|-------------------------------------------------------------|")
            
            print("===============================================================")
            print(f"\nSelecciona la Misión que deseas agendar (0-{len(misiones_alianza) - 1})")
            print("[-1] Volver Atrás ↩️")
            
            numero = int(input("\n▶  ")) # Selección de la misión para agendar
            
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("============================================")
            print("| Opcion incorrecta ❌ vuelve a intentarlo |")
            print("============================================\n")
            continue
        
        if numero == -1:
            sonido2.play()
            pygame.mixer.music.load(light_side_menu)
            pygame.mixer.music.play(-1)
            limpiar_terminal()
            return
        
        if numero < 0 or numero > (len(misiones_alianza) - 1):
            limpiar_terminal()
            sonido3.play()
            print("=========================================")
            print(f"| Error ⚠️  ingresa un número del (0-{len(misiones_alianza) - 1}) |")
            print("=========================================\n")
            continue
        else:
            sonido1.play()
            limpiar_terminal()
            
            print("==========================================")
            print(f"✅ Misión seleccionada")
            print(f"{Style.BRIGHT}{misiones_alianza[numero].nombre}{Style.RESET_ALL}")
            print("==========================================")
            break

    mision = misiones_alianza[numero].id # AQUÍ SE GUARDA EL ID DE LA MISIÓN <<<

    print("\n")
    mostrar_cargando_y_limpiar("Planificando la Misión") # Sección de Cargando...

    # Sección para seleccionar los recursos
    while True: # Manejamos las excepciones, aquí el usuario puede meter la pata de muchas formas.
        error = False
        try:
            # Ver el inventario completo de la alianza
            print("=============== RECURSOS DISPONIBLES PARA LA MISIÓN 📦 ===============")
            contador = 0
            num = 0
            for x in range(len(recursos_alianza)):
                print(f"| [{num}] {Fore.YELLOW}{Style.BRIGHT}{recursos_alianza[contador].nombre_inventario}{Style.RESET_ALL} {recursos_alianza[contador].tipo_recurso} | ID: [{recursos_alianza[contador].id}] | Unidad/es: [{recursos_alianza[contador].cantidad}] |")
                contador += 1
                num += 1
            print("======================================================================")
            
            print(f"\n{Style.BRIGHT}{misiones_alianza[numero].nombre}{Style.RESET_ALL}")
            print(f"{Style.BRIGHT}< DESCRIPCIÓN >{Style.RESET_ALL}")
            print(f"{Style.BRIGHT}{misiones_alianza[numero].descripcion}{Style.RESET_ALL}")
            
            print(f"\n{Style.BRIGHT}< INSTRUCCIONES >{Style.RESET_ALL}")
            print(f"1. Escoge el recurso deseado seleccionando un número en el rango del (0 - {len(recursos_alianza) - 1}).") 
            print("2. Para asignar varios recursos, cada número debe estar separado por comas (,).")
            print(">>> EJEMPLO: 0,5,6,10")
            # Esto se comentó debido a que las cantidades de recursos fueron simplificadas a 1 para eliminar incoherencias
            # print("3. Para asignar varias unidades del mismo recurso, repite el número.")
            # print("(Asegúrate de no seleccionar una cantidad superior a la cantidad disponible.)")
            # print(">>> EJEMPLO: 8,8,12,12")
            
            print("\n[-1] Cancelar y volver al menú principal ↩️")
            print("[-2] Restricciones de los recursos ⚙️")
            
            print("\nSelecciona tus recursos.")
            seleccion = [int(i) for i in input("▶  ").split(",")] # Selección de los recursos en forma de lista
        
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("=============================================")
            print("| Opcion incorrecta ❌ vuelve a intentarlo |")
            print("=============================================\n")
            continue
            
        
        if len(seleccion) == 1: # Sección de Volver al menú principal
            for x in seleccion:
                if x == -1:
                    mision = None
                    sonido2.play()
                    limpiar_terminal()
                    pygame.mixer.music.load(light_side_menu)
                    pygame.mixer.music.play(-1)
                    return
                
                elif x == -2: # Sección para visualizar las restricciones de la Alianza
                    sonido1.play()
                    limpiar_terminal()
                    print("======================================================")
                    print("| ⚙️  Restricciones de los recursos de la Alianza 🪯   |")
                    print("======================================================")
                    print("| ↔️  CO-REQUISITOS                                   |")
                    print("| Luke Skywalker 👤 <---> Sable de luz ⚔️             |")
                    print("| Han Solo 👤 <---> Bláster 🔫                       |")
                    print("| Lando Calrissian 👤 ---> Halcón Milenario 🛸       |")
                    print("| R2-D2 👾  <---> C-3PO 🤖                           |")
                    print("| X-Wing ✈️  ---> Traje de Piloto 🧥                  |")
                    print("| A-Wing 🛩️  ---> Traje de Piloto 🧥                  |")
                    print("| Equipo de Camuflaje 🌿  ---> Princesa Leia 👤      |")
                    print("|====================================================|")
                    print("| ❌ EXCLUSIONES                                     |")
                    print("| Han Solo 👤 , Lando Calrissian 👤                  |")
                    print("| Detonadores Térmicos 💣 , Escudo Deflector 🛡️       |")
                    print("|====================================================|")
                    input("\nPresiona Enter ↩️  Para volver atrás  ")
                    sonido2.play()
                    volver_seleccion_recursos = True
                    break
        
        if volver_seleccion_recursos:
            volver_seleccion_recursos = False
            limpiar_terminal()
            continue
        
        
        error_recurso_fuera_de_rango = None
        for x in seleccion:
            if x < 0 or x > (len(recursos_alianza) - 1):
                error_recurso_fuera_de_rango = True
                break
        if error_recurso_fuera_de_rango == True:
            limpiar_terminal()
            sonido3.play()
            print("==================================================================")
            print(f"| ⚠️  Error. Selecciona los números entre (0 - {len(recursos_alianza) - 1}) para continuar |")
            print("==================================================================\n")
            continue
        
        if (len(seleccion)) > 12:
            limpiar_terminal()
            sonido3.play()
            print("==================================================================")
            print(f"| ⚠️  Error. No puedes seleccionar más de {len(seleccion) - 1} recursos por misión |")
            print("==================================================================\n")
            print(f"Última selección de recursos: {seleccion}\n")
            continue
        
        # Validar cantidades de recursos
        error_cantidad = False
        contador_seleccion = Counter(seleccion) # Devuelve un diccionario de la lista "selección" de la forma: Clave (# de recurso) : Valor (Cant. de veces que se repite en la lista)
        recursos_seleccionados = [] # Lista donde se almacenan los IDs de la selección de recursos
        for numero_recurso, veces_seleccionado in contador_seleccion.items():
            recurso = recursos_alianza[numero_recurso]
            if veces_seleccionado > recurso.cantidad:
                limpiar_terminal()
                sonido3.play()
                print("===============================================================")
                print(f"Error ❌ Solo hay {recurso.cantidad} unidad/es de {recurso.nombre} disponible/s")
                print(f"Intentaste seleccionar {veces_seleccionado}")
                print("===============================================================\n")
                print(f"Última selección de recursos: {seleccion}\n")
                error_cantidad = True
                break
            
            for x in range(veces_seleccionado): # Si las cantidades del recurso seleccionadas no excenden a las del inventario
                recursos_seleccionados.append(recurso.id) # Las añadimos a los recursos seleccionados
        
        if error_cantidad == True:
            continue
        
        # Se verifica si la selección de recursos cumple la exclusión y los co-requisitos
        corequisito_valor = validar_co_requisitos_alianza(recursos_seleccionados)
        exclusion_valor = validar_exclusiones_alianza(recursos_seleccionados)
        
        # Si los co-requisitos o las exclusiones son violadas, volvemos a intentar.
        if corequisito_valor == False or exclusion_valor == False:
            print("==================================================================\n")
            sonido3.play()
            print(f"Última selección de recursos: {seleccion}\n")
            continue
        
        # Si se seleccionó una  CANTIDAD del mismo RECURSO, hacemos una lista de los recursos seleccionados pero sin repetirlos
        # Para la validación del Horario
        recursos_seleccionados_sin_duplicados = []
        for recurso in recursos_seleccionados: # Quitamos los elementos que se repiten en los recursos seleccionados
            if recurso not in recursos_seleccionados_sin_duplicados:
                recursos_seleccionados_sin_duplicados.append(recurso)
        
        # Verificar Recursos prohibidos
        error_recurso_prohibido = False
        mision_objeto = misiones_alianza[numero]
        for x in recursos_seleccionados_sin_duplicados:
            if x in mision_objeto.recursos_prohibidos_ids:
                error_recurso_prohibido = True
                break
        if error_recurso_prohibido == True:
            limpiar_terminal()
            sonido3.play()
            print("=====================================")
            print("ERROR ❌")
            print(f"⚠️  {x} no puede estar en esta misión.")
            print("NOTA: Lee la descripción.")
            print("=====================================\n")
            print(f"Última selección de recursos: {seleccion}\n")
            continue
        
        # Verificar si todos los recursos que necesita la misión están en la selección.
        error_recurso_faltante = False
        recursos_faltantes = []
        for x in mision_objeto.recursos_requeridos_ids:
            if x not in recursos_seleccionados_sin_duplicados:
                recursos_faltantes.append(x)
                error_recurso_faltante = True
        if error_recurso_faltante == True:
                limpiar_terminal()
                sonido3.play()
                print("===================================================================")
                print(f"⚠️  Error. La misión {misiones_alianza[numero].nombre}")
                print(f"Le faltan los recursos: {recursos_faltantes}")
                print("NOTA: La descripción indica los recursos necesarios para la misión")
                print("===================================================================\n")
                print(f"Última selección de recursos: {seleccion}\n")
                continue
        
        else: # Si no ocurre ninguna excepción, los recursos se seleccionaron perfectamente
            if corequisito_valor == True and exclusion_valor == True:
                sonido1.play()
                print("===============================================================")
                break


    print("\n")
    mostrar_cargando_y_limpiar("Añadiendo los recursos a la misión")


    # Sección del calendario semanal
    while True: # Manejamos las excepciones
        try:
            print("====================")
            print("|  CALENDARIO 📆   |")
            print("====================")
            print("| [0] Lunes        |")
            print("| [1] Martes       |")
            print("| [2] Miércoles    |")
            print("| [3] Jueves       |")
            print("| [4] Viernes      |")
            print("| [5] Sábado       |")
            print("| [6] Domingo      |")
            print("====================")
            print("\nPara agendar la misión en el Calendario Semanal:")
            print("> Elige un día de la semana [0-6]:")
            print("> Presiona [7] para agendar automáticamente:\n")
            opcion = int(input("▶  "))
        
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("==============================================")
            print("| Opcion incorrecta ❌ vuelve a intentarlo |")
            print("=============================================\n")
            continue
        
        if opcion < 0 or opcion > 7:
            limpiar_terminal()
            sonido3.play()
            print("==============================================================")
            print("| Error ⚠️  selecciona un número entre (0-7) para continuar |")
            print("==============================================================\n")
            continue
        
        else:
            sonido1.play()
            
            if opcion == 7: # Sección de "BUSCAR UN HUECO"
                def buscar_hueco_automatico():
                    semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
                    for dia in semana:
                        todos_disponibles = True
                        for x in recursos_seleccionados:
                            for recurso in recursos_alianza:
                                if recurso.id == x:
                                    veces_seleccionado = len(recurso.agenda[dia])
                                    cantidad_necesaria = recursos_seleccionados.count(x)
                                    if veces_seleccionado + cantidad_necesaria > recurso.cantidad:
                                        todos_disponibles = False
                                        break
                            if todos_disponibles == False:
                                break
                        if todos_disponibles == True:
                            return dia
                    return None
                dia = buscar_hueco_automatico() # DIA SELECCIONADO AUTOMÁTICAMENTE
                
                if dia == None: # Excepción (Todo los recursos están ocupados en la semana)
                    limpiar_terminal()
                    sonido3.play()
                    print("=====================================================")
                    print("| ⚠️  No hay días disponibles para esta misión   |")
                    print("| Todos los recursos están ocupados toda la semana |")
                    print("=====================================================")
                    print("Opciones:\n")
                    print("1. Intentar con otros recursos.")
                    print("2. Eliminar una misión para liberar espacio.")
                    input("\nPresiona Enter ↩️  para volver al Ménu  ")
                    sonido2.play()
                    limpiar_terminal()
                    pygame.mixer.music.load(light_side_menu)
                    pygame.mixer.music.play(-1)
                    return
                
                break # Si llegó hasta el break no hubo ningún problema y continúa el código
            
            elif opcion >= 0 or opcion <= 6: # Sección de selección manual
                semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
                dia = semana[opcion]
                break
    
    # Sección para verificar si un recurso está o no en dos misiones a la vez en el mismo día
    def validar_horario_recursos_seleccionados():
        pygame.mixer.music.set_volume(0.3)
        limpiar_terminal()
        contador_seleccion = Counter(recursos_seleccionados_sin_duplicados)
        
        # Verificar conflictos y agendar
        for recurso_seleccion_id, cantidad_necesaria in contador_seleccion.items():
            for recurso in recursos_alianza:
                if recurso.id == recurso_seleccion_id: # ¿El ID del recurso está en la selección?
                    veces_ocupado = len(recurso.agenda[dia]) # Contar cuantas veces está ocupado ese día
                    if veces_ocupado + cantidad_necesaria > recurso.cantidad: # Si los recursos seleccionados están disponibles ese dia...
                        sleep(1)
                        sonido3.play()
                        print("========================================================")
                        print(f"⚠️  CONFLICTO: {recurso.nombre}")
                        print(f"   Cant. Disponible el {dia}: {recurso.cantidad - veces_ocupado}")
                        print(f"   Necesitas: {cantidad_necesaria}")
                        print(f">> Asegúrate que {recurso.nombre} esté libre el {dia}")
                        print("========================================================")
                        return False
                    
                    else:
                        
                        for x in range(cantidad_necesaria):
                            recurso.agenda[dia].append(mision) # Ahora tienen una misión que cumplir
                        recurso.sonido.play() # Reproducir sonido o frase del recurso
                        print(f"✅ {Style.BRIGHT}{recurso.nombre}{Style.RESET_ALL} ahora tiene la misión agendada para el {Fore.YELLOW}{Style.BRIGHT}{dia}{Style.RESET_ALL}.")
                        print(f"Unidades restantes para el {dia}: [{recurso.cantidad - cantidad_necesaria}].\n")
                        sleep(3.7)
        pygame.mixer.music.set_volume(0.5)
        return True # Si llegamos hasta aquí, los recursos seleccionados pueden hacer la misión el día seleccionado

    # Si todo salió bien, elimnamos la misión que seleccionamos de las misiones disponibles.
    # Porque en el universo de Star Wars cada misión es única, no podemos rescatar a Leia el lunes y después volverla a rescatar el martes
    resultado = validar_horario_recursos_seleccionados()
    
    if resultado == True:
        print("\n")
        mostrar_cargando_y_limpiar("Agendando la misión")
        pygame.mixer.music.stop()
        pygame.mixer.music.load(mision_exito)
        pygame.mixer.music.play()
        print("==============================================")
        print(f"|{Fore.YELLOW}{Style.BRIGHT} LA MISIÓN HA SIDO AGENDADA EXITOSAMENTE 🎉 {Style.RESET_ALL}|")
        print("==============================================")
        sleep(5)
        
        # Agendamos la misión y la eliminamos de misiones de la alianza
        from Functions.listar_misiones import agregar_mision_alianza_para_agendar
        agregar_mision_alianza_para_agendar(mision,misiones_alianza[numero].nombre,dia,recursos_seleccionados_sin_duplicados)
        misiones_eliminadas = misiones_alianza[numero]
        from Functions.eliminar_mision_agenda import obtener_misiones_eliminadas_alianza
        obtener_misiones_eliminadas_alianza(misiones_eliminadas)
        misiones_alianza.pop(numero) # Borramos la misión de las misiones de la alianza
        
        while True: # Sección para regresar al menú o agendar otra misión
            print("\n¿Qué deseas hacer?")
            print("[1] Agendar otra misión ➕")
            print("[2] Volver al menú principal 🏠")
            try:
                opcion_final = int(input("\n▶  "))
                if opcion_final == 1:
                    limpiar_terminal()
                    sonido1.play()
                    pygame.mixer.music.load(light_side_mission)
                    pygame.mixer.music.play(-1)
                    return "agendar_otra_mision"
                
                elif opcion_final == 2:
                    sonido2.play()
                    limpiar_terminal()
                    pygame.mixer.music.load(light_side_menu)
                    pygame.mixer.music.play(-1)
                    return "menu"
                
                elif opcion_final > 2 or opcion_final < 1:
                    limpiar_terminal()
                    sonido3.play()
                    print("=================================================")
                    print("| Error ⚠️  Selecciona (1) o (2) para continuar. |")
                    print("=================================================")
                    continue
                
            except ValueError:
                limpiar_terminal()
                sonido3.play()
                print("===========================================")
                print("| ❌ Opción Inválida. Inténtalo de nuevo |")
                print("===========================================")
                continue
        
    if resultado == False: # Si hubo un error a la hora de agendar una misión...
        
        while True: # Sección para regresar al menú o agendar otra misión (Intentarlo nuevamente)
            print("\n¿Qué deseas hacer?")
            print("[1] Intentarlo de nuevo 🔄️")
            print("[2] Volver al menú principal 🏠")
            try:
                opcion_final = int(input("\n▶  "))
                if opcion_final == 1:
                    limpiar_terminal()
                    sonido1.play()
                    pygame.mixer.music.load(light_side_mission)
                    pygame.mixer.music.play(-1)
                    return "reintentar"
                
                elif opcion_final == 2:
                    limpiar_terminal()
                    sonido2.play()
                    pygame.mixer.music.load(light_side_menu)
                    pygame.mixer.music.play(-1)
                    return "menu"
                
                elif opcion_final > 2 or opcion_final < 1:
                    limpiar_terminal()
                    sonido3.play()
                    print("=============================================")
                    print("Error ⚠️  Selecciona (1) o (2) para continuar.")
                    print("=============================================")
                    continue
                
            except ValueError:
                limpiar_terminal()
                sonido3.play()
                print("=======================================")
                print("❌ Opción Inválida. Inténtalo de nuevo")
                print("=======================================")
                continue










def agendar_mision_imperio():
    pygame.mixer.music.set_volume(0.5)
    
    while True:
        if len(misiones_imperio) == 0: # Excepción (Ya se asignaron todas las misiones)
            sleep(0.5)
            sonido3.play()
            pygame.mixer.music.stop()
            print("========================================")
            print("| YA NO QUEDAN MISIONES POR ASIGNAR ⚠️  |")
            print("========================================")
            print("\nNOTA: Puedes elimanar una misión planificada para \nasignarla otro día y con otros recursos.")
            input("\nPresiona Enter ↩️  para volver al Menú Principal. ")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(dark_side_menu)
            pygame.mixer.music.play(-1)
            limpiar_terminal()
            return
        
        try: # Mostar las misiones disponibles
            
            print("=============== MISIONES DISPONIBLES DEL IMPERIO ✳️  ===============")
            contador = 0
            numero = 0
            print("|-----------------------------------------------------------------|")
            for x in range(len(misiones_imperio)): # Mostramos las misiones que tenemos disponible ahora
                print(f"| [{numero}] {Style.BRIGHT}{misiones_imperio[contador].nombre}{Style.RESET_ALL} | ID: [{misiones_imperio[contador].id}] |")
                contador += 1
                numero += 1
                print("|-----------------------------------------------------------------|")
            
            print("===================================================================")
            print(f"\nSelecciona la Misión que deseas agendar (0-{len(misiones_imperio) - 1})")
            print("[-1] Volver Atrás ↩️")
            
            numero = int(input("\n▶  ")) # Selección de la misión para agendar
            
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("============================================")
            print("| Opcion incorrecta ❌ vuelve a intentarlo |")
            print("============================================\n")
            continue
        
        if numero == -1:
            sonido2.play()
            pygame.mixer.music.load(dark_side_menu)
            pygame.mixer.music.play(-1)
            limpiar_terminal()
            return
        
        if numero < 0 or numero > (len(misiones_imperio) - 1):
            limpiar_terminal()
            sonido3.play()
            print("=========================================")
            print(f"| Error ⚠️  ingresa un número del (0-{len(misiones_imperio) - 1}) |")
            print("=========================================\n")
            continue
        else:
            sonido1.play()
            limpiar_terminal()
            print("===============================================")
            print(f"✅ Misión seleccionada")
            print(f"{Style.BRIGHT}{misiones_imperio[numero].nombre}{Style.RESET_ALL}")
            print("===============================================")
            break

    mision = misiones_imperio[numero].id # AQUÍ SE GUARDA EL ID DE LA MISIÓN <<<

    print("\n")
    mostrar_cargando_y_limpiar("Planificando la Misión") # Sección de Cargando...

    # Sección para seleccionar los recursos
    while True: # Manejamos las excepciones, aquí el usuario puede meter la pata de muchas formas.
        error = False
        try:
            # Ver el inventario completo del imperio
            print("============== RECURSOS DISPONIBLES PARA LA MISIÓN 📦 ==============")
            contador = 0
            num = 0
            for x in range(len(recursos_imperio)):
                print(f"| [{num}] {Fore.YELLOW}{Style.BRIGHT}{recursos_imperio[contador].nombre_inventario}{Style.RESET_ALL} {recursos_imperio[contador].tipo_recurso} | ID: [{recursos_imperio[contador].id}] | Unidad/es: [{recursos_imperio[contador].cantidad}] |")
                contador += 1
                num += 1
            print("====================================================================")
            
            print(f"\n{Style.BRIGHT}{misiones_imperio[numero].nombre}{Style.RESET_ALL}")
            print(f"{Style.BRIGHT}< DESCRIPCIÓN >{Style.RESET_ALL}")
            print(f"{Style.BRIGHT}{misiones_imperio[numero].descripcion}{Style.RESET_ALL}")
            
            print(f"\n{Style.BRIGHT}< INSTRUCCIONES >{Style.RESET_ALL}")
            print(f"1. Escoge el recurso deseado seleccionando un número en el rango del (0 - {len(recursos_imperio) - 1}).") 
            print("2. Para asignar varios recursos, cada número debe estar separado por comas (,).")
            print(">>> EJEMPLO: 0,15,5,14")
            # Esto se comentó debido a que las cantidades de recursos fueron simplificadas a 1 para eliminar incoherencias
            # print("3. Para asignar varias unidades del mismo recurso, repite el número.")
            # print("(Asegúrate de no seleccionar una cantidad superior a la cantidad disponible.)")
            # print(">>> EJEMPLO: 8,8,12,12")
            
            print("\n[-1] Cancelar y volver al menú principal ↩️")
            print("[-2] Restricciones de los recursos ⚙️")
            
            print("\nSelecciona tus recursos.")
            seleccion = [int(i) for i in input("▶  ").split(",")] # Selección de los recursos en forma de lista
        
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("=============================================")
            print("| Opcion incorrecta ❌ vuelve a intentarlo |")
            print("=============================================\n")
            continue
            
        volver_seleccion_recursos = False
        
        if len(seleccion) == 1: # Sección de Volver al menú principal
            for x in seleccion:
                if x == -1:
                    mision = None
                    sonido2.play()
                    limpiar_terminal()
                    pygame.mixer.music.load(dark_side_menu)
                    pygame.mixer.music.play(-1)
                    return
                
                elif x == -2: # Sección para visualizar las restricciones del Imperio
                    sonido1.play()
                    limpiar_terminal()
                    print("======================================================")
                    print("|  ⚙️  Restricciones de los recursos del Imperio ☸️    |")
                    print("======================================================")
                    print("| ↔️  CO-REQUISITOS                                   |")
                    print("| Darth Vader 🎭 <---> Sable de luz ⚔️                |")
                    print("| Grand M. Tarkin 👤 <---> Estrella de la Muerte 🌑  |")
                    print("| Destructor Estelar 🛸 ---> Almirante Piett 👤      |")
                    print("| Piloto AT AT 🪖  <---> AT AT 🦿                     |")
                    print("| TIE Fighter ✈️  ---> Stormtrooper 🪖                 |")
                    print("| AT-ST 🤖 ---> Stormtrooper 🪖                       |")
                    print("| Stormtrooper 🪖  ---> Bláster Imperial 🔫           |")
                    print("|====================================================|")
                    print("| ❌ EXCLUSIONES                                     |")
                    print("| AT AT 🦿 , AT ST 🤖                                |")
                    print("|====================================================|")
                    input("\nPresiona Enter ↩️  Para volver atrás  ")
                    sonido2.play()
                    volver_seleccion_recursos = True
                    break
        
        if volver_seleccion_recursos:
            volver_seleccion_recursos = False
            limpiar_terminal()
            continue
        
        error_recurso_fuera_de_rango = None
        for x in seleccion:
            if x < 0 or x > (len(recursos_imperio) - 1):
                error_recurso_fuera_de_rango = True
                break
        if error_recurso_fuera_de_rango == True:
            limpiar_terminal()
            sonido3.play()
            print("==================================================================")
            print(f"| ⚠️  Error. Selecciona los números entre (0 - {len(recursos_imperio) - 1}) para continuar |")
            print("==================================================================\n")
            continue
        
        if (len(seleccion)) > 12:
            limpiar_terminal()
            sonido3.play()
            print("==================================================================")
            print(f"| ⚠️  Error. No puedes seleccionar más de {len(seleccion) - 1} recursos por misión |")
            print("==================================================================\n")
            print(f"Última selección de recursos: {seleccion}\n")
            continue
        
        # Validar cantidades de recursos
        error_cantidad = False
        contador_seleccion = Counter(seleccion) # Devuelve un diccionario de la lista "selección" de la forma: Clave (# de recurso) : Valor (Cant. de veces que se repite en la lista)
        recursos_seleccionados = [] # Lista donde se almacenan los IDs de la selección de recursos
        for numero_recurso, veces_seleccionado in contador_seleccion.items():
            recurso = recursos_imperio[numero_recurso]
            if veces_seleccionado > recurso.cantidad:
                limpiar_terminal()
                sonido3.play()
                print("===============================================================")
                print(f"Error ❌ Solo hay {recurso.cantidad} unidad/es de {recurso.nombre} disponible/s")
                print(f"Intentaste seleccionar {veces_seleccionado}")
                print("===============================================================\n")
                print(f"Última selección de recursos: {seleccion}\n")
                error_cantidad = True
                break
            
            for x in range(veces_seleccionado): # Si las cantidades del recurso seleccionadas no excenden a las del inventario
                recursos_seleccionados.append(recurso.id) # Las añadimos a los recursos seleccionados
        
        if error_cantidad == True:
            continue
        
        # Se verifica si la selección de recursos cumple la exclusión y los co-requisitos
        corequisito_valor = validar_co_requisitos_imperio(recursos_seleccionados)
        exclusion_valor = validar_exclusiones_imperio(recursos_seleccionados)
        
        # Si los co-requisitos o las exclusiones son violadas, volvemos a intentar.
        if corequisito_valor == False or exclusion_valor == False:
            print("==================================================================\n")
            print(f"Última selección de recursos: {seleccion}\n")
            sonido3.play()
            continue
        
        # Si se seleccionó una  CANTIDAD del mismo RECURSO, hacemos una lista de los recursos seleccionados pero sin repetirlos
        # Para la validación del Horario
        recursos_seleccionados_sin_duplicados = []
        for recurso in recursos_seleccionados: # Quitamos los elementos que se repiten en los recursos seleccionados
            if recurso not in recursos_seleccionados_sin_duplicados:
                recursos_seleccionados_sin_duplicados.append(recurso)
        
        # Verificar Recursos prohibidos
        error_recurso_prohibido = False
        mision_objeto = misiones_imperio[numero]
        for x in recursos_seleccionados_sin_duplicados:
            if x in mision_objeto.recursos_prohibidos_ids:
                error_recurso_prohibido = True
                break
        if error_recurso_prohibido == True:
            limpiar_terminal()
            sonido3.play()
            print("=====================================")
            print("ERROR ❌")
            print(f"⚠️  {x} no puede estar en esta misión")
            print("NOTA: Lee la descripción.")
            print("=====================================\n")
            print(f"Última selección de recursos: {seleccion}\n")
            continue
        
        # Verificar si todos los recursos que necesita la misión están en la selección.
        error_recurso_faltante = False
        recursos_faltantes = []
        for x in mision_objeto.recursos_requeridos_ids:
            if x not in recursos_seleccionados_sin_duplicados:
                recursos_faltantes.append(x)
                error_recurso_faltante = True
        if error_recurso_faltante == True:
                limpiar_terminal()
                sonido3.play()
                print("===================================================================")
                print(f"⚠️  Error. La misión {misiones_imperio[numero].nombre}")
                print(f"Le faltan los recursos: {recursos_faltantes}")
                print("NOTA: La descripción indica los recursos necesarios para la misión")
                print("===================================================================\n")
                print(f"Última selección de recursos: {seleccion}\n")
                continue
        
        else: # Si no ocurre ninguna excepción, los recursos se seleccionaron perfectamente
            if corequisito_valor == True and exclusion_valor == True:
                sonido1.play()
                print("===============================================================")
                break


    print("\n")
    mostrar_cargando_y_limpiar("Añadiendo los recursos a la misión")


    # Sección del calendario semanal
    while True: # Manejamos las excepciones
        try:
            print("====================")
            print("|  CALENDARIO 📆   |")
            print("====================")
            print("| [0] Lunes        |")
            print("| [1] Martes       |")
            print("| [2] Miércoles    |")
            print("| [3] Jueves       |")
            print("| [4] Viernes      |")
            print("| [5] Sábado       |")
            print("| [6] Domingo      |")
            print("====================")
            print("\nPara agendar la misión en el Calendario Semanal:")
            print("> Elige un día de la semana [0-6]:")
            print("> Presiona [7] para agendar automáticamente:\n")
            opcion = int(input("▶  "))
        
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("============================================")
            print("| Opcion incorrecta ❌ vuelve a intentarlo |")
            print("============================================\n")
            continue
        
        if opcion < 0 or opcion > 7:
            limpiar_terminal()
            sonido3.play()
            print("============================================================")
            print("| Error ⚠️  selecciona un número entre (0-7) para continuar |")
            print("============================================================\n")
            continue
        
        else:
            sonido1.play()
            
            if opcion == 7: # Sección de "BUSCAR UN HUECO"
                def buscar_hueco_automatico():
                    semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
                    for dia in semana:
                        todos_disponibles = True
                        for x in recursos_seleccionados:
                            for recurso in recursos_imperio:
                                if recurso.id == x:
                                    veces_seleccionado = len(recurso.agenda[dia])
                                    cantidad_necesaria = recursos_seleccionados.count(x)
                                    if veces_seleccionado + cantidad_necesaria > recurso.cantidad:
                                        todos_disponibles = False
                                        break
                            if todos_disponibles == False:
                                break
                        if todos_disponibles == True:
                            return dia
                    return None
                dia = buscar_hueco_automatico() # DIA SELECCIONADO AUTOMÁTICAMENTE
                
                if dia == None: # Excepción (Todo los recursos están ocupados en la semana)
                    limpiar_terminal()
                    sonido3.play()
                    print("=================================================")
                    print("| ⚠️  No hay días disponibles para esta misión   |")
                    print("| Todos los recursos están ocupados toda la semana |")
                    print("=================================================")
                    print("Opciones:\n")
                    print("1. Intentar con otros recursos.")
                    print("2. Eliminar una misión para liberar espacio.")
                    input("\nPresiona Enter ↩️  para volver al Ménu  ")
                    sonido2.play()
                    limpiar_terminal()
                    pygame.mixer.music.load(dark_side_menu)
                    pygame.mixer.music.play(-1)
                    return
                
                break # Si llegó hasta el break no hubo ningún problema y continúa el código
            
            elif opcion >= 0 or opcion <= 6: # Sección de selección manual
                semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
                dia = semana[opcion]
                break
    
    # Sección para verificar si un recurso está o no en dos misiones a la vez en el mismo día
    def validar_horario_recursos_seleccionados():
        limpiar_terminal()
        pygame.mixer.music.set_volume(0.2)
        contador_seleccion = Counter(recursos_seleccionados_sin_duplicados)
        
        # Verificar conflictos y agendar
        for recurso_seleccion_id, cantidad_necesaria in contador_seleccion.items():
            for recurso in recursos_imperio:
                if recurso.id == recurso_seleccion_id: # ¿El ID del recurso está en la selección?
                    veces_ocupado = len(recurso.agenda[dia]) # Contar cuantas veces está ocupado ese día
                    if veces_ocupado + cantidad_necesaria > recurso.cantidad: # Si los recursos seleccionados están disponibles ese dia...
                        sleep(1)
                        sonido3.play()
                        print("========================================================")
                        print(f"⚠️  CONFLICTO: {recurso.nombre}")
                        print(f"   Cant. Disponible el {dia}: {recurso.cantidad - veces_ocupado}")
                        print(f"   Necesitas: {cantidad_necesaria}")
                        print(f">> Asegúrate que {recurso.nombre} esté libre el {dia}")
                        print("========================================================")
                        return False
                    
                    else:
                        
                        for x in range(cantidad_necesaria):
                            recurso.agenda[dia].append(mision) # Ahora tienen una misión que cumplir
                        recurso.sonido.play() # Reproducir sonido o frase del recurso
                        print(f"✅ {Style.BRIGHT}{recurso.nombre}{Style.RESET_ALL} ahora tiene la misión agendada para el {Fore.YELLOW}{Style.BRIGHT}{dia}{Style.RESET_ALL}.")
                        print(f"Unidades restantes para el {dia}: [{recurso.cantidad - cantidad_necesaria}].\n")
                        sleep(3.7)
        pygame.mixer.music.set_volume(0.5)
        return True # Si llegamos hasta aquí, los recursos seleccionados pueden hacer la misión el día seleccionado

    # Si todo salió bien, elimnamos la misión que seleccionamos de las misiones disponibles.
    # Porque en el universo de Star Wars cada misión es única, no podemos capturar a Han Solo el lunes y después volverl a capturar el martes
    resultado = validar_horario_recursos_seleccionados()
    
    if resultado == True:
        print("\n")
        mostrar_cargando_y_limpiar("Agendando la misión")
        pygame.mixer.music.stop()
        pygame.mixer.music.load(mision_exito)
        pygame.mixer.music.play()
        print("==============================================")
        print(f"|{Fore.YELLOW}{Style.BRIGHT} LA MISIÓN HA SIDO AGENDADA EXITOSAMENTE 🎉 {Style.RESET_ALL}|")
        print("==============================================")
        sleep(5)
        
        # Agendamos la misión y la eliminamos de misiones del imperio
        from Functions.listar_misiones import agregar_mision_imperio_para_agendar
        agregar_mision_imperio_para_agendar(mision,misiones_imperio[numero].nombre,dia,recursos_seleccionados_sin_duplicados)
        misiones_eliminadas = misiones_imperio[numero]
        from Functions.eliminar_mision_agenda import obtener_misiones_eliminadas_imperio
        obtener_misiones_eliminadas_imperio(misiones_eliminadas)
        misiones_imperio.pop(numero) # Borramos la misión de las misiones del imperio
        
        while True: # Sección para regresar al menú o agendar otra misión
            print("\n¿Qué deseas hacer?")
            print("[1] Agendar otra misión ➕")
            print("[2] Volver al menú principal 🏠")
            try:
                opcion_final = int(input("\n▶  "))
                if opcion_final == 1:
                    limpiar_terminal()
                    sonido1.play()
                    pygame.mixer.music.load(dark_side_mission)
                    pygame.mixer.music.play(-1)
                    return "agendar_otra_mision"
                
                elif opcion_final == 2:
                    sonido2.play()
                    limpiar_terminal()
                    pygame.mixer.music.load(dark_side_menu)
                    pygame.mixer.music.play(-1)
                    return "menu"
                
                elif opcion_final > 2 or opcion_final < 1:
                    limpiar_terminal()
                    sonido3.play()
                    print("=================================================")
                    print("| Error ⚠️  Selecciona [1] o [2] para continuar |")
                    print("=================================================")
                    continue
                
            except ValueError:
                limpiar_terminal()
                sonido3.play()
                print("===========================================")
                print("| ❌ Opción Inválida. Inténtalo de nuevo |")
                print("===========================================")
                continue
        
    if resultado == False: # Si hubo un error a la hora de agendar una misión...
        
        while True: # Sección para regresar al menú o agendar otra misión (Intentarlo nuevamente)
            print("\n¿Qué deseas hacer?")
            print("[1] Intentarlo de nuevo 🔄️")
            print("[2] Volver al menú principal 🏠")
            try:
                opcion_final = int(input("\n▶  "))
                if opcion_final == 1:
                    limpiar_terminal()
                    sonido1.play()
                    pygame.mixer.music.load(dark_side_mission)
                    pygame.mixer.music.play(-1)
                    return "reintentar"
                
                elif opcion_final == 2:
                    limpiar_terminal()
                    sonido2.play()
                    pygame.mixer.music.load(dark_side_menu)
                    pygame.mixer.music.play(-1)
                    return "menu"
                
                elif opcion_final > 2 or opcion_final < 1:
                    limpiar_terminal()
                    sonido3.play()
                    print("=================================================")
                    print("| Error ⚠️  Selecciona [1] o [2] para continuar |")
                    print("=================================================")
                    continue
                
            except ValueError:
                limpiar_terminal()
                sonido3.play()
                print("===========================================")
                print("| ❌ Opción Inválida. Inténtalo de nuevo |")
                print("===========================================")
                continue