from utilidades import limpiar_terminal
from utilidades import mostrar_cargando_y_limpiar

from colorama import Fore, Back, Style, init # Importar librería de colores para strings
init(autoreset=True)

import time
import pyfiglet # Importar librería para generar ASCII Art para el Strig de bienvenida (Pantalla Inicio 1 [AF Studio])
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame".
import pygame # Importación de la música y sonidos
pygame.mixer.init()

# Importamos los sonidos y música del módulo musica_sonidos
from musica_sonidos import star_wars_intro
from musica_sonidos import light_side
from musica_sonidos import light_side_menu
from musica_sonidos import light_side_mission
from musica_sonidos import dark_side
from musica_sonidos import dark_side_menu
from musica_sonidos import sonido0
from musica_sonidos import sonido1
from musica_sonidos import sonido2
from musica_sonidos import sonido3
from musica_sonidos import sonido4
from musica_sonidos import sonido5

from persistencia import cargar_estado
estado_cargado = cargar_estado()

# Pantalla de incio 1 (Empiezas por primera vez o juegas tu partida guardada)
limpiar_terminal()
if estado_cargado == False:
    print(f"\n         {Back.LIGHTBLUE_EX}{Style.BRIGHT}BIENVENIDO/A.{Style.RESET_ALL}")
    print("\n")
    mostrar_cargando_y_limpiar("Iniciando una nueva partida")
    limpiar_terminal()
    sonido0.play()
    nombre_estudio = pyfiglet.figlet_format("AF STUDIO")
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{nombre_estudio}")
    presentacion = pyfiglet.figlet_format(f"  Presenta")
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{presentacion}")
    time.sleep(3)
    limpiar_terminal()
elif estado_cargado == True:
    print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Datos cargados exitosamente{Style.RESET_ALL}.")
    print("\n")
    mostrar_cargando_y_limpiar("Cargando partida guardada")
    limpiar_terminal()
    sonido0.play()
    nombre_estudio = pyfiglet.figlet_format("AF STUDIO")
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{nombre_estudio}")
    presentacion = pyfiglet.figlet_format("  Presenta")
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{presentacion}")
    time.sleep(3)
    limpiar_terminal()

# Variables bandera (Elección de bando)
Alianza = False
Imperio = False

# Comienza la música a sonar
pygame.mixer.music.load(star_wars_intro)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

primera_vez = True

# Pantalla de inicio 2 (Elegir un bando). El Imperio estará disponible en próximas actualizaciones
while True:
    try:
        if primera_vez == True: # Cuando entras por primera vez te sale la "animación" de presentación de la aplicación.
            
            titulo = pyfiglet.figlet_format("    STAR WARS")
            print(f"{Fore.YELLOW}{Style.BRIGHT}{titulo}{Style.RESET_ALL}")
            
            subtitulo = pyfiglet.figlet_format("Missions Planner", font="small")
            print(f"{Fore.YELLOW}{Style.BRIGHT}{subtitulo}{Style.RESET_ALL}")
            time.sleep(2)
            
            mensaje_intro = ["     Hace mucho tiempo,","     Hace mucho tiempo, en una galaxia muy,","     Hace mucho tiempo, en una galaxia muy, muy lejana..."]
            
            for msg in mensaje_intro:
                print(f"\r{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}", end="", flush=True)
                time.sleep(1.5)
            time.sleep(1.25)
            
            print("\n")
            print(f"\n       Selecciona el Bando al que quieres pertenecer: ")
            print(f"\n[1]{Fore.BLUE}{Style.BRIGHT}                ALIANZA REBELDE 🪯{Style.RESET_ALL} \nUna coalición de mundos oprimidos que luchan por la libertad.\nOpera con recursos limitados pero con gran determinación.\nGolpea al Imperio con tácticas rápidas y precisas.\nÚnete si quieres devolverle la esperanza a la galaxia.")
            print(f"\n[2]{Fore.RED}{Style.BRIGHT}                IMPERIO GALÁCTICO ☸️{Style.RESET_ALL} \nUn régimen poderoso que impone orden absoluto en la galaxia.\nControla vastas flotas y ejércitos disciplinados.\nAplasta cualquier resistencia sin dudar.\nElige este bando si buscas fuerza, control y autoridad total.")
            opcion= int(input("\n▶  "))
            
            if opcion == 1:
                
                sonido1.play()
                pygame.mixer.music.load(light_side)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                limpiar_terminal() #Limpiamos la terminal
                print("====================================")
                print(f"|        Seleción exitosa ✅       |\n|{Fore.BLUE}{Style.BRIGHT} Bienvenido a la ALIANZA REBELDE  {Style.RESET_ALL}|")
                print("====================================")
                Alianza = True
            
            if opcion == 2: # EL BANDO DEL IMPERIO ESTÁ EN DESARROLLO
                limpiar_terminal()
                sonido3.play()
                print("==============================================")
                print(f"El{Fore.RED}{Style.BRIGHT} IMPERIO GALÁCTICO ☸️{Style.RESET_ALL}  está en desarrollo... \nPróximamente disponible.")
                print("==============================================")
                input("\nPresione Enter para volver atrás ↩️  ")
                sonido2.play()
                limpiar_terminal()
                continue
            
        else: # Si metiste la pata solamente te muestra un mensaje de error
            titulo = pyfiglet.figlet_format("    STAR WARS")
            print(f"{Fore.YELLOW}{Style.BRIGHT}{titulo}{Style.RESET_ALL}")
            
            subtitulo = pyfiglet.figlet_format("Missions Planner", font="small")
            print(f"{Fore.YELLOW}{Style.BRIGHT}{subtitulo}{Style.RESET_ALL}")
            
            print(f"\n{Fore.WHITE}{Style.BRIGHT}     Hace mucho tiempo, en una galaxia muy, muy lejana...{Style.RESET_ALL} ")
            print("\n")
            print(f"       Selecciona el Bando al que quieres pertenecer: ")
            print(f"\n[1]{Fore.BLUE}{Style.BRIGHT}                ALIANZA REBELDE 🪯{Style.RESET_ALL} \nUna coalición de mundos oprimidos que luchan por la libertad.\nOpera con recursos limitados pero con gran determinación.\nGolpea al Imperio con tácticas rápidas y precisas.\nÚnete si quieres devolverle la esperanza a la galaxia.")
            print(f"\n[2]{Fore.RED}{Style.BRIGHT}                IMPERIO GALÁCTICO ☸️{Style.RESET_ALL} \nUn régimen poderoso que impone orden absoluto en la galaxia.\nControla vastas flotas y ejércitos disciplinados.\nAplasta cualquier resistencia sin dudar.\nElige este bando si buscas fuerza, control y autoridad total.")
            
            opcion= int(input("\n▶  "))
            
            if opcion == 1:
                sonido1.play()
                pygame.mixer.music.load(light_side)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                limpiar_terminal() #Limpiamos la terminal
                print("====================================")
                print(f"|        Seleción exitosa ✅       |\n|{Fore.BLUE}{Style.BRIGHT} Bienvenido a la ALIANZA REBELDE  {Style.RESET_ALL}|")
                print("====================================")
                Alianza = True
            
            if opcion == 2: # EL BANDO DEL IMPERIO ESTÁ EN DESARROLLO
                limpiar_terminal()
                sonido3.play()
                print("==============================================")
                print(f"El{Fore.RED}{Style.BRIGHT} IMPERIO GALÁCTICO ☸️{Style.RESET_ALL}  está en desarrollo... \nPróximamente disponible.")
                print("==============================================")
                input("\nPresione Enter para volver atrás ↩️  ")
                sonido2.play()
                limpiar_terminal()
                primera_vez = False
                continue
                    
                    # Esto es para cuando se habilite el Imperio (IGNORAR)
                    # pygame.mixer.music.load(dark_side)
                    # pygame.mixer.music.set_volume(0.3)
                    # pygame.mixer.music.play()
                    # limpiar_terminal()
                    # print("=================================")
                    # print(f"Seleción exitosa ✅ \n{Fore.RED}{Style.BRIGHT}Bienvenido a el IMPERIO GALÁCTICO ☸️{Style.RESET_ALL}.")
                    # print("=================================")
                    # Imperio = True
    
    except ValueError:
        sonido3.play()
        limpiar_terminal()
        print("        ================================================")
        print("        | Error ⚠️  selecciona [1] o [2] para continuar |")
        print("        ================================================\n")
        primera_vez = False
        continue
    
    if opcion < 1 or opcion > 2:
        sonido3.play()
        limpiar_terminal()
        print("        ================================================")
        print("        | Error ⚠️  selecciona [1] o [2] para continuar |")
        print("        ================================================\n")
        primera_vez = False
        continue
    
    else:
        break

# Posterior de elegir tu bando, se muestra un Menú de Carga...
print("\n")
mostrar_cargando_y_limpiar("Cargando")

# Verificar que bando fue el escogido
if Alianza == True:
    pygame.mixer.music.load(light_side_menu)
    pygame.mixer.music.play(-1)

elif Imperio == True:
    pygame.mixer.music.load(dark_side_menu)
    pygame.mixer.music.play(-1)

limpiar_terminal()

# Menú Principal y Funciones
while True:
    try:
        if Alianza == True:
            print("===================================")
            print(f"| {Fore.BLUE}{Style.BRIGHT}MENÚ PRINCIPAL DE LA ALIANZA ⚔️{Style.RESET_ALL}  |")
            print("===================================")
        elif Imperio == True:
            print("==================================")
            print(f"| {Fore.RED}{Style.BRIGHT}MENÚ PRINCIPAL DEL IMPERIO 🤖{Style.RESET_ALL} |")
            print("==================================")
        print("| [1] Listar Misiones          📋 |\n| [2] Añadir Misión            ➕ |\n| [3] Eliminar Misión          ❌ |\n| [4] Ver Detalles             👀 |\n| [5] Salir                    📤 |")
        print("===================================")
        opcion = int(input("\n▶  "))
    
        if opcion == 1: # Función para listar las misiones agendadas
            sonido1.play()
            from listar_misiones import mostrar_misiones_agendadas
            mostrar_misiones_agendadas()
            salir_confirmado = False
    
        elif opcion == 2: # Función de añadir misión (Lógica principal de la app)
            sonido1.play()
            limpiar_terminal()
            pygame.mixer.music.stop()
            from añadir_mision import añadir_nueva_mision
            pygame.mixer.music.load(light_side_mission)
            pygame.mixer.music.play(-1)
            
            while True:
                resultado = añadir_nueva_mision()
                if resultado == "agendar_otra_mision" or resultado == "reintentar":
                    continue
                else:
                    break
                
            salir_confirmado = False
    
        elif opcion == 3: # Función de eliminar misión
            sonido1.play()
            limpiar_terminal()
            from eliminar_mision_agenda import eliminar_mision
            eliminar_mision()
            salir_confirmado = False
    
        elif opcion == 4: # Función de ver detalles
            sonido1.play()
            from detalles import ver_detalles
            ver_detalles()
            salir_confirmado = False
    
        elif opcion == 5: # Función de salir
            sonido4.play()
            limpiar_terminal()
            salir_confirmado = False
            while True:
                print("\n¿Estás seguro de que deseas salir? 😟\nPresiona [1] para salir ❌\nPresiona [2] para volver atrás ↩️\n")
                try:
                    preguntar = int(input("▶  "))
                    
                    if preguntar == 1:
                        sonido1.play()
                        limpiar_terminal()
                        pygame.mixer.music.stop()
                        sonido5.play()
                        print("======================================")
                        print("| Que la Fuerza te acompañe ✒️  (...) |")
                        print("======================================")
                        print("\nTu partida está siendo guardada en estos momentos 💾 ⬇️")
                        from persistencia import guardar_estado
                        guardar_estado()
                        time.sleep(1.25)
                        print("\nCompletado ✅\n")
                        time.sleep(2)
                        limpiar_terminal()
                        mostrar_cargando_y_limpiar("Saliendo de la aplicación")
                        salir_confirmado = True
                        
                        break
                    
                    elif preguntar == 2:
                        limpiar_terminal()
                        sonido2.play()
                        break
                        
                    elif preguntar < 1 or preguntar > 2:
                        sonido3.play()
                        limpiar_terminal()
                        print("\n===============================")
                        print("| Error ⚠️  selecciona [1] o [2] |")
                        print("=================================\n")
                except ValueError:
                    sonido3.play()
                    limpiar_terminal()
                    print("\n=================================")
                    print("| Error ⚠️  selecciona [1] o [2] |")
                    print("=================================\n")
                    continue
    
    except ValueError:
        sonido3.play()
        limpiar_terminal()
        print("\n============================================")
        print("| Opcion incorrecta ❌ vuelve a intentarlo |")
        print("============================================\n")
        continue
    
    if opcion < 1 or opcion > 5:
        sonido3.play()
        limpiar_terminal()
        print("\n========================================")
        print("| Error ⚠️  ingresa un número del (1-5) |")
        print("========================================\n")
        continue
    if salir_confirmado:
        break