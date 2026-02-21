from Modules.utilidades import limpiar_terminal
from Modules.utilidades import mostrar_cargando_y_limpiar

from colorama import Fore, Back, Style, init # Importar librería de colores para strings
init(autoreset=True)
import pyfiglet # Importar librería para generar ASCII Art para el Strig de bienvenida (Pantalla Inicio 1 [AF Studio])

import Modules.bando as bando
import random
from time import sleep

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame".
import pygame # Importación de la música y sonidos
pygame.mixer.init()

# Importamos los sonidos y música del módulo musica_sonidos
from Modules.musica_sonidos import star_wars_intro
from Modules.musica_sonidos import light_side, light_side_menu, light_side_mission
from Modules.musica_sonidos import dark_side, dark_side_menu, dark_side_mission
from Modules.musica_sonidos import sonido0, sonido1, sonido2, sonido3, sonido4, sonido5

from Modules.persistencia import cargar_estado
estado_cargado = cargar_estado()

# Pantalla de incio 1 (Empiezas por primera vez o juegas tu partida guardada)
limpiar_terminal()
if not estado_cargado:
    print("   ==========================")
    print(f"   |      {Fore.YELLOW}{Style.BRIGHT}BIENVENIDO/A{Style.RESET_ALL}      |")
    print("   ==========================")
    print("\n")
    mostrar_cargando_y_limpiar("Iniciando una nueva partida ")
    
    limpiar_terminal()

else:
    print("==================================")
    print(f"|{Fore.GREEN}{Style.BRIGHT} ✅ Datos cargados exitosamente {Style.RESET_ALL}|")
    print("==================================")
    print("\n")
    mostrar_cargando_y_limpiar("Cargando partida guardada ")

# Presentación de AF STUDIO
limpiar_terminal()
sonido0.play()
print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{pyfiglet.figlet_format('AF STUDIO')}")
print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}{pyfiglet.figlet_format('  Presenta')}")
sleep(3)
limpiar_terminal()


# Comienza la música a sonar
pygame.mixer.music.load(star_wars_intro)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Función de pantalla de selección de bando
def mostrar_pantalla_seleccion_bando(primera_vez):
    titulo = pyfiglet.figlet_format("    STAR WARS")
    print(f"{Fore.YELLOW}{Style.BRIGHT}{titulo}{Style.RESET_ALL}")
    subtitulo = pyfiglet.figlet_format("Missions Planner", font="small")
    print(f"{Fore.YELLOW}{Style.BRIGHT}{subtitulo}{Style.RESET_ALL}")
    
    
    if primera_vez:
        texto_intro = [
            "     Hace mucho tiempo,",
            "     Hace mucho tiempo, en una galaxia muy,",
            "     Hace mucho tiempo, en una galaxia muy, muy lejana..."
        ]
        sleep(2)
        for msg in texto_intro:
            print(f"\r{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}", end="", flush=True)
            sleep(1.5)
        sleep(1)
        print("\n")
    else:
        print(f"\n{Fore.WHITE}{Style.BRIGHT}     Hace mucho tiempo, en una galaxia muy, muy lejana...{Style.RESET_ALL}\n")

    print("       Selecciona el Bando al que quieres pertenecer:\n")
    print(f"[1]{Fore.BLUE}{Style.BRIGHT}                ALIANZA REBELDE 🪯{Style.RESET_ALL}")
    print("Una coalición de mundos oprimidos que luchan por la libertad.")
    print("Opera con recursos limitados pero con gran determinación.")
    print("Golpea al Imperio con tácticas rápidas y precisas.")
    print("Únete si quieres devolverle la esperanza a la galaxia.\n")
    print(f"[2]{Fore.RED}{Style.BRIGHT}                IMPERIO GALÁCTICO ☸️{Style.RESET_ALL}")
    print("Un régimen poderoso que impone orden absoluto en la galaxia.")
    print("Controla vastas flotas y ejércitos disciplinados.")
    print("Aplasta cualquier resistencia sin dudar.")
    print("Elige este bando si buscas fuerza, control y autoridad total.\n")
    
    try:
        opcion = int(input("▶  "))
        
    except ValueError:
        sonido3.play()
        limpiar_terminal()
        print("        ================================================")
        print("        | Error ⚠️  selecciona [1] o [2] para continuar |")
        print("        ================================================\n")
        return False

    
    if opcion == 1:
        pygame.mixer.music.stop()
        sonido1.play()
        sleep(0.25)
        pygame.mixer.music.load(light_side)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        limpiar_terminal()
        print("=====================================")
        print(f"|        Selección exitosa ✅       |")
        print(f"|{Fore.BLUE}{Style.BRIGHT}  Bienvenido a la ALIANZA REBELDE  {Style.RESET_ALL}|")
        print("=====================================")
        bando.seleccionar_alianza()
        return True

    elif opcion == 2:
        pygame.mixer.music.stop()
        sonido1.play()
        sleep(0.25)
        pygame.mixer.music.load(dark_side)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        limpiar_terminal()
        print("=====================================")
        print(f"|        Selección exitosa ✅       |")
        print(f"|{Fore.RED}{Style.BRIGHT} Bienvenido a el IMPERIO GALÁCTICO {Style.RESET_ALL}|")
        print("=====================================")
        bando.seleccionar_imperio()
        return True

    else:
        sonido3.play()
        limpiar_terminal()
        print("        ================================================")
        print("        | Error ⚠️  selecciona [1] o [2] para continuar |")
        print("        ================================================\n")
        return False






# Función de carga y música del menú principal
def cargar_frase_y_musica_menu():
    dado = random.randint(1, 6)

    if bando.Alianza:
        frases = [
            "La guerra no hace a uno más grandioso ",
            "El odio conduce al Lado Oscuro ",
            "Tu enfoque determina tu realidad ",
            "No existe tal cosa como la suerte ",
            "La fe es nuestra esperanza ",
            "Hazlo o no lo hagas, pero no lo intentes ",
        ]
        mostrar_cargando_y_limpiar(frases[dado - 1])
        pygame.mixer.music.load(light_side)
        pygame.mixer.music.play(-1)
    
    elif bando.Imperio:
        frases = [
            "¡Juntos dominaremos la galaxia! ",
            "¡Poder! ¡Poder ilimitado! ",
            "Todo marcha según lo planeado ",
            "Aún tienes mucho que aprender ",
            "No le temas a la oscuridad. Abrázala ",
            "¡Por fin tendremos venganza! ",
        ]
        mostrar_cargando_y_limpiar(frases[dado - 1])
        pygame.mixer.music.load(dark_side)
        pygame.mixer.music.play(-1)



primera_vez = True

while True:
    # Pantalla de selección de bando
    bando_elegido = False
    
    while not bando_elegido:
        bando_elegido = mostrar_pantalla_seleccion_bando(primera_vez)
        primera_vez = False

    print("\n")
    cargar_frase_y_musica_menu()
    limpiar_terminal()

    # Menú principal
    cambiar_bando = False

    if bando.Alianza == True:
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(light_side_menu)
        pygame.mixer.music.play(-1)

    if bando.Imperio == True:
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(dark_side_menu)
        pygame.mixer.music.play(-1)

    while True:
        try:
            if bando.Alianza:
                print("===================================")
                print(f"| {Fore.BLUE}{Style.BRIGHT}MENÚ PRINCIPAL DE LA ALIANZA ⚔️{Style.RESET_ALL}  |")
                print("===================================")
            elif bando.Imperio:
                print("===================================")
                print(f"|  {Fore.RED}{Style.BRIGHT}MENÚ PRINCIPAL DEL IMPERIO 🤖{Style.RESET_ALL}  |")
                print("===================================")

            print("| [1] Listar Misiones          📋 |")
            print("| [2] Añadir Misión            ➕ |")
            print("| [3] Eliminar Misión          ❌ |")
            print("| [4] Ver Detalles             👀 |")
            print("| [5] Salir                    📤 |")
            print("| [-1] Cambiar de Bando        🔄 |")
            print("===================================")
            opcion = int(input("\n▶  "))

            # [-1] Cambiar de bando
            if opcion == -1:
                sonido2.play()
                limpiar_terminal()
                from Modules.persistencia import guardar_estado
                guardar_estado()
                pygame.mixer.music.stop()
                print(f"{Fore.YELLOW}{Style.BRIGHT}           Datos guardados 💾{Style.RESET_ALL}\n")
                mostrar_cargando_y_limpiar("Volviendo a la selección de bando ")
                limpiar_terminal()
                bando.reiniciar()
                cambiar_bando = True
                pygame.mixer.music.load(star_wars_intro)
                pygame.mixer.music.play(-1)
                break

            # [1] Listar misiones
            elif opcion == 1:
                sonido1.play()
                from Functions.listar_misiones import mostrar_misiones_agendadas
                mostrar_misiones_agendadas()

            # [2] Añadir misión
            elif opcion == 2:
                sonido1.play()
                limpiar_terminal()
                pygame.mixer.music.stop()

                if bando.Alianza:
                    from Functions.añadir_mision import agendar_mision_alianza
                    pygame.mixer.music.load(light_side_mission)
                    pygame.mixer.music.play(-1)
                    while True:
                        resultado = agendar_mision_alianza()
                        if resultado in ("agendar_otra_mision", "reintentar"):
                            continue
                        else:
                            break
                    pygame.mixer.music.load(light_side_menu)
                    pygame.mixer.music.play(-1)

                elif bando.Imperio:
                    from Functions.añadir_mision import agendar_mision_imperio
                    pygame.mixer.music.load(dark_side_mission)
                    pygame.mixer.music.play(-1)
                    while True:
                        resultado = agendar_mision_imperio()
                        if resultado in ("agendar_otra_mision", "reintentar"):
                            continue
                        else:
                            break
                    pygame.mixer.music.load(dark_side_menu)
                    pygame.mixer.music.play(-1)

            # [3] Eliminar misión
            elif opcion == 3:
                sonido1.play()
                limpiar_terminal()
                from Functions.eliminar_mision_agenda import eliminar_mision
                eliminar_mision()

            # [4] Ver detalles
            elif opcion == 4:
                sonido1.play()
                from Functions.detalles import ver_detalles
                ver_detalles()

            # [5] Salir
            elif opcion == 5:
                sonido4.play()
                limpiar_terminal()
                salir_confirmado = False

                while True:
                    print("=========================================")
                    print("| ¿Estás seguro de que deseas salir? 😟 |")
                    print("| [1] Salir ❌                          |")
                    print("| [2] Volver atrás ↩️                    |")
                    print("=========================================")
                    try:
                        preguntar = int(input("\n▶  "))

                        if preguntar == 1:
                            sonido1.play()
                            limpiar_terminal()
                            pygame.mixer.music.stop()
                            sonido5.play()
                            print("======================================")
                            print("| Que la Fuerza te acompañe ✒️  (...) |")
                            print("======================================")
                            print(f"\n{Fore.YELLOW}{Style.BRIGHT}Guardando datos{Style.RESET_ALL} 💾")
                            from Modules.persistencia import guardar_estado
                            guardar_estado()  # Guarda AMBOS bandos
                            sleep(1.25)
                            print("\nCompletado ✅\n")
                            sleep(2)
                            limpiar_terminal()
                            mostrar_cargando_y_limpiar("Saliendo de la aplicación")
                            salir_confirmado = True
                            break

                        elif preguntar == 2:
                            limpiar_terminal()
                            sonido2.play()
                            break

                        else:
                            sonido3.play()
                            limpiar_terminal()
                            print("\n=================================")
                            print("| Error ⚠️  selecciona [1] o [2] |")
                            print("=================================\n")

                    except ValueError:
                        sonido3.play()
                        limpiar_terminal()
                        print("\n=================================")
                        print("| Error ⚠️  selecciona [1] o [2] |")
                        print("=================================\n")

                if salir_confirmado:
                    cambiar_bando = False
                    break

            else:
                sonido3.play()
                limpiar_terminal()
                print("\n=====================================")
                print("| Error ⚠️  ingresa un número válido |")
                print("=====================================\n")

        except ValueError:
            sonido3.play()
            limpiar_terminal()
            print("\n============================================")
            print("| Opción incorrecta ❌ vuelve a intentarlo |")
            print("============================================\n")
            continue

    # Decidir: salir del todo o volver a elegir bando
    if not cambiar_bando:
        break