# Importamos todo lo que nos hace falta
from Recursos_Alianza import recursos_alianza
from Misiones_Alianza import misiones_alianza
from Restricciones import validar_co_requisitos,validar_exclusiones
from collections import Counter

# Módulo necesarios para la limpieza de la terminal
import os
import time
import sys
def limpiar_terminal():
    os.system('cls')

# Menú de Carga
def mostrar_cargando_y_limpiar(mensaje):
    print(f"\n{mensaje} ", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True) 
        sys.stdout.flush()
        time.sleep(1) 
    time.sleep(1)
    limpiar_terminal()

# Módulo pygame (para reproducir los sonidos)
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame"
import pygame
pygame.mixer.init()

# Música
from musica_sonidos import mision_exito_alianza
from musica_sonidos import light_side_mission
from musica_sonidos import light_side_menu

# Sonidos
from musica_sonidos import sonido1
from musica_sonidos import sonido2
from musica_sonidos import sonido3

pygame.mixer.music.stop()
limpiar_terminal()

def añadir_nueva_mision():
    # Sección para seleccionar una Misión
    while True: # Manejando las excepciones
        if len(misiones_alianza) == 0:
            time.sleep(0.5)
            sonido3.play()
            pygame.mixer.music.stop()
            print("=====================================")
            print("YA NO QUEDAN MISIONES POR ASIGNAR ⚠️")
            print("=====================================")
            print("\nNOTA: Puedes elimanar una misión planificada para \nasignarla otro día y con otros recursos.")
            input("\nPresiona Enter ↩️  para volver al Menú Principal. ")
            pygame.mixer.music.stop()
            pygame.mixer.music.load(light_side_menu)
            pygame.mixer.music.play(-1)
            limpiar_terminal()
            return
        
        try:
            print("========= MISIONES DISPONIBLES DE LA ALIANZA ❇️  =========")
            contador = 0
            numero = 0
            for x in range(len(misiones_alianza)): # Mostramos las misiones que tenemos disponible ahora
                print(f"{numero}. {misiones_alianza[contador].nombre} | ID: [{misiones_alianza[contador].id}]")
                print(f"[{misiones_alianza[contador].descripcion}]")
                contador += 1
                numero += 1
                print("=========================================================")
            numero = int(input(f"\nSelecciona la Misión que deseas agendar (0-{len(misiones_alianza) - 1}): \n▶  "))
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("========================================")
            print("Opcion incorrecta ❌ vuelve a intentarlo")
            print("========================================\n")
            continue
        if numero < 0 or numero > 3:
            limpiar_terminal()
            sonido3.play()
            print("=====================================")
            print(f"Error ⚠️  ingresa un número del (0-{len(misiones_alianza) - 1}).")
            print("=====================================\n")
            continue
        else:
            sonido1.play()
            limpiar_terminal()
            print(f"\nMisión seleccionada ✅ \n{misiones_alianza[numero].nombre}")
            break

    mision = misiones_alianza[numero].id # IMPORTANTE 👁️. ESTE ES EL ID DE LA MISIÓN SELECCIONADA <<<

    def mostrar_cargando_y_limpiar(mensaje):
        print(f"\n{mensaje} ", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True) 
            sys.stdout.flush()
            time.sleep(1) 
        time.sleep(1)
        limpiar_terminal()
    mostrar_cargando_y_limpiar("Planificando misión") # Sección de Cargando...
    
    # Sección para seleccionar los recursos
    # Manejamos las excepciones, aquí el usuario puede meter la pata de muchas formas.
    while True:
        error = False
        try:
            # Ver el inventario completo de la alianza
            print("============= RECURSOS DISPONIBLES PARA LA MISIÓN 📦 ============")
            contador = 0
            num = 0
            for x in range(len(recursos_alianza)):
                print(f"{num}. {recursos_alianza[contador].nombre_inventario} {recursos_alianza[contador].tipo_recurso} | ID: [{recursos_alianza[contador].id}] | Unidad/es: [{recursos_alianza[contador].cantidad}]")
                contador += 1
                num += 1
            print("=================================================================")
            print(f"\nNOTA IMPORTANTE")
            print(f"1. Escoge el recurso deseado para la misión seleccionando un número en el rango del (0 - {len(recursos_alianza) - 1}).") 
            print(">>> EJEMPLO: 1 [Princesa Leia]")
            print("2. Para asignar varios recursos, cada número debe estar separado por comas (,)")
            print(">>> EJEMPLO: 0,5,6,10. [Luke, R2-D2, C-3PO, Sable de Luz]")
            print("3. Para asignar varias unidades del mismo recurso solo repite el número al seleccionarlo.")
            print("[Asegúrate de no seleccionar una cantidad superior a la cantidad disponible de unidades]")
            print(">>> EJEMPLO: 8,8,12,12 [X-Wing (2), Traje de Piloto (2)")
            print("\nLa descripción de cada misión te dice cuales son los recursos que debes usar.")
            print(misiones_alianza[numero].descripcion)
            print("\nSelecciona tus recursos.")
            seleccion = [int(i) for i in input("▶  ").split(",")] # Selección de los recursos en forma de lista por ejemplo [1,4,5,11]

        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("=========================================")
            print("Opcion incorrecta ❌ vuelve a intentarlo")
            print("=========================================\n")
            continue
            
        error1 = None
        for j in seleccion:
            if j < 0 or j > (len(recursos_alianza) - 1):
                error1 = True
                break
        if error1 == True:
            limpiar_terminal()
            sonido3.play()
            print("==============================================================")
            print(f"Error ⚠️  selecciona los números entre (0 - {len(recursos_alianza) - 1}) para continuar.")
            print("==============================================================\n")
            continue
            
        if (len(seleccion)) > 13:
            limpiar_terminal()
            sonido3.play()
            print("==================================================")
            print(f"Error ⚠️  No puedes seleccionar más de {len(recursos_alianza) - 1} recursos.")
            print("==================================================\n")
            continue
        
        # Validar cantidades de recursos
        error_cantidad = False
        contador_seleccion = Counter(seleccion) # Devuelve un diccionario de la lista "selección", clave (# de recurso) : Valor (Cant. de veces que se repite en la lista)
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
                error_cantidad = True
                break
            
            for _ in range(veces_seleccionado): # Si las cantidades del recurso seleccionadas no excenden a las del inventario
                recursos_seleccionados.append(recurso.id) # Las añadimos a los recursos seleccionados
        
        if error_cantidad == True:
            continue
        # Se verifica si la selección de recursos cumple la exclusión y los co-requisitos
        corequisito_valor = validar_co_requisitos(recursos_seleccionados)
        exclusion_valor = validar_exclusiones(recursos_seleccionados)
        
        # Si los co-requisitos o las exclusiones son violadas, volvemos a intentar.
        if corequisito_valor == False or exclusion_valor == False:
            print("==================================================================\n")
            sonido3.play()
            continue
        
        # Si se seleccionó una  CANTIDAD del mismo RECURSO, hacemos una lista de los recursos seleccionados pero sin repetirlos
        recursos_seleccionados_sin_duplicados = []
        for recurso in recursos_seleccionados: # Quitamos los elementos que se repiten en los recursos seleccionados
            if recurso not in recursos_seleccionados_sin_duplicados:
                recursos_seleccionados_sin_duplicados.append(recurso)
        
        # Verificar Recursos prohibidos
        recurso_prohibido_error = False
        mision_objeto = misiones_alianza[numero]
        for recurso_id in recursos_seleccionados_sin_duplicados:
            if recurso_id in mision_objeto.recursos_prohibidos_ids:
                recurso_prohibido_error = True
                break
        if recurso_prohibido_error == True:
            limpiar_terminal()
            sonido3.play()
            print("=====================================")
            print("ERROR ❌")
            print(f"⚠️  {recurso_id} no puede estar en esta misión")
            print("=====================================\n")
            continue
            
        else: # Si no ocurre ninguna excepción, los recursos se seleccionaron perfectamente
            if corequisito_valor == True and exclusion_valor == True:
                sonido1.play()
                print("===============================================================")
                break


# Segunda Sección de Cargando...
    mostrar_cargando_y_limpiar("Añadiendo los recursos a la misión")

    # Sección del calendario semanal
    while True: # Manejamos las excepciones
        try:
            print("==============")
            print("CALENDARIO 📆")
            print("==============")
            print("0. Lunes")
            print("1. Martes")
            print("2. Miércoles")
            print("3. Jueves")
            print("4. Viernes")
            print("5. Sábado")
            print("6. Domingo")
            print("==============")
            print("\nPara agendar la misión en el Calendario Semanal:")
            print("Elige un día de la semana (0-6):\n")
            opcion = int(input("▶  "))
        except ValueError:
            limpiar_terminal()
            sonido3.play()
            print("==========================================")
            print("Opcion incorrecta ❌ vuelve a intentarlo")
            print("=========================================\n")
            continue
        if opcion < 0 or opcion > 6:
            limpiar_terminal()
            sonido3.play()
            print("==========================================================")
            print("Error ⚠️  selecciona un número entre (0-6) para continuar.")
            print("==========================================================\n")
            continue
        else:
            sonido1.play()
            break

    semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    dia = semana[opcion] # IMPORTANTE 👁️. ESTE ES EL DIA DE LA SEMANA QUE SELECCIONAMOS <<<


    def validar_horario_recursos_seleccionados():
        pygame.mixer.music.set_volume(0.30) # 30% del Volumen de la Música de fondo
        contador_seleccion = Counter(recursos_seleccionados_sin_duplicados)
        # Verificar conflictos y agendar
        for recurso_seleccion_id, cantidad_necesaria in contador_seleccion.items():
            for recurso in recursos_alianza:
                if recurso.id == recurso_seleccion_id: # ¿El ID del recurso está en la selección?
                    veces_ocupado = len(recurso.agenda[dia]) # Contar cuantas veces está ocupado ese día
                    if veces_ocupado + cantidad_necesaria > recurso.cantidad: # Si los recursos seleccionados están disponibles ese dia...
                        mision_actual = recurso.agenda[dia]
                        sonido3.play()
                        print("========================================================")
                        print(f"⚠️  CONFLICTO: {recurso.nombre}")
                        print(f"    Cant. Disponible el {dia}: {recurso.cantidad - veces_ocupado}")
                        print(f"    Necesitas: {cantidad_necesaria}")
                        print(f">>> Asegúrate que {recurso.nombre} esté libre el {dia}.")
                        print("========================================================")
                        return False
                    else:
                        
                        for _ in range(cantidad_necesaria):
                            recurso.agenda[dia].append(mision) # Ahora tienen una misión que cumplir
                        recurso.sonido.play() # Reproducir sonido o frase del recurso
                        print(f"✅ {recurso.nombre} ahora tiene la misión agendada para el {dia}.")
                        print(f"Unidades restantes para el {dia}: [{recurso.cantidad - cantidad_necesaria}].\n")
                        time.sleep(3.7)
        
        pygame.mixer.music.set_volume(1.0) # 100% del Volumen de la música de fondo
        return True # Si llegamos hasta aquí, los recursos seleccionados pueden hacer la misión el día que seleccionaste

    # Terera sección de cargando (Última)
    def mostrar_cargando_y_limpiar(mensaje=f"Agendando la misión para el {dia}"):
        print(f"\n{mensaje} ", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True) 
            sys.stdout.flush()
            time.sleep(1.5) 
        time.sleep(2)
    limpiar_terminal()

    # Si todo salió bien, elimnamos la misión que seleccionamos de las misiones disponibles. 
    # Porque en el universo de star wars cada misión es única, no podemos rescatar a Leia el lunes y después volverla a rescatar el martes
    resultado = validar_horario_recursos_seleccionados()
    if resultado == True:
        mostrar_cargando_y_limpiar() # Sección de cargando 3
        pygame.mixer.music.stop
        pygame.mixer.music.load(mision_exito_alianza)
        pygame.mixer.music.play()
        print("\nLA MISIÓN HA SIDO AGENDADA EXITOSAMENTE 🎉.")
        time.sleep(5)
        
        # Guardamos la misión y todos sus datos en estado_aplicación
        from listar_misiones import agregar_mision_para_agendar
        agregar_mision_para_agendar(mision,misiones_alianza[numero].nombre,dia,recursos_seleccionados_sin_duplicados)
        misiones_alianza.pop(numero) # Borramos la misión de las misiones de la alianza
        
        while True: # Sección para regresar al menú o agendar otra misión
            print("\n¿Qué deseas hacer?")
            print("1. Agendar otra misión ➕")
            print("2. Volver al menú principal 🏠")
            try:
                opcion_final = int(input("\n▶  "))
                if opcion_final == 1:
                    limpiar_terminal()
                    sonido1.play()
                    pygame.mixer.music.load(light_side_mission)
                    pygame.mixer.music.play(-1)
                    from añadir_mision import añadir_nueva_mision
                    añadir_nueva_mision() # Reiniciamos el módulo
                    break
                elif opcion_final == 2:
                    sonido2.play()
                    limpiar_terminal()
                    pygame.mixer.music.load(light_side_menu)
                    pygame.mixer.music.play(-1)
                    break
                elif opcion_final > 2 or opcion_final < 1:
                    limpiar_terminal()
                    sonido3.play()
                    print("=============================================")
                    print("Error ⚠️  Selecciona (1) o (2) para continuar.")
                    print("=============================================")
                    continue
            except:
                limpiar_terminal()
                sonido3.play()
                print("=======================================")
                print("❌ Opción Inválida. Inténtalo de nuevo")
                print("=======================================")
                continue
        
    if resultado == False:
        while True: # Sección para regresar al menú o agendar otra misión
            print("\n¿Qué deseas hacer?")
            print("1. Intentarlo de nuevo 🔄️")
            print("2. Volver al menú principal 🏠")
            try:
                opcion_final = int(input("\n▶  "))
                if opcion_final == 1:
                    limpiar_terminal()
                    sonido1.play()
                    pygame.mixer.music.load(light_side_mission)
                    pygame.mixer.music.play(-1)
                    from añadir_mision import añadir_nueva_mision
                    añadir_nueva_mision() # Reiniciamos el módulo
                    break
                elif opcion_final == 2:
                    limpiar_terminal()
                    sonido2.play()
                    pygame.mixer.music.load(light_side_menu)
                    pygame.mixer.music.play(-1)
                    break
                elif opcion_final > 2 or opcion_final < 1:
                    limpiar_terminal()
                    sonido3.play()
                    print("=============================================")
                    print("Error ⚠️  Selecciona (1) o (2) para continuar.")
                    print("=============================================")
                    continue
            except:
                limpiar_terminal()
                sonido3.play()
                print("=======================================")
                print("❌ Opción Inválida. Inténtalo de nuevo")
                print("=======================================")
                continue