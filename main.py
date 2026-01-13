# Importación de la limpieza de la terminal
import os
import time
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de "Bienvenido a Pygame"
def limpiar_terminal():
    os.system('cls')
limpiar_terminal()

# Importación de los colores para los textos
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Importación de la música y sonidos
import pygame
pygame.mixer.init()

# Importamos los sonidos y música del módulo musica_sonidos
from musica_sonidos import star_wars_intro
from musica_sonidos import light_side
from musica_sonidos import light_side_menu
from musica_sonidos import light_side_mission
from musica_sonidos import dark_side
from musica_sonidos import dark_side_menu
from musica_sonidos import sonido1
from musica_sonidos import sonido2
from musica_sonidos import sonido3
from musica_sonidos import sonido4
from musica_sonidos import sonido5

pygame.mixer.music.load(star_wars_intro) # Suena la música 😎 "ESTO VA A SER ÉPICO PAPUS"
pygame.mixer.music.play(-1)

# Variables bandera
Alianza = False
Imperio = False

# Elegir un bando
while True:
    try:
        print(f"{Fore.YELLOW}{Style.BRIGHT}[STAR WARS MISSIONS PLANNER PROJECT 🚀]{Style.RESET_ALL}")
        print(f"\n{Style.BRIGHT}Hace mucho tiempo, en una galaxia muy, muy lejana...{Style.RESET_ALL} ")
        print(f"\n▶ Selecciona un Bando: ")
        print(f"\n1.{Fore.BLUE}{Style.BRIGHT} Alianza Rebelde 🪯{Style.RESET_ALL} \nUna coalición de mundos oprimidos que luchan por la libertad.\nOpera con recursos limitados pero con gran determinación.\nGolpea al Imperio con tácticas rápidas y precisas.\nÚnete si quieres devolverle la esperanza a la galaxia.")
        print(f"\n2.{Fore.RED}{Style.BRIGHT} Imperio Galáctico ☸️{Style.RESET_ALL} \nUn régimen poderoso que impone orden absoluto en la galaxia.\nControla vastas flotas y ejércitos disciplinados.\nAplasta cualquier resistencia sin dudar.\nElige este bando si buscas fuerza, control y autoridad total.")
        opcion= int(input("\n▶ Elige (1 ó 2): "))
        if opcion == 1:
            sonido1.play()
            pygame.mixer.music.load(light_side)
            pygame.mixer.music.play()
            #Limpiamos la terminal
            limpiar_terminal()
            print("==================================")
            print(f"Seleción exitosa ✅ \n{Fore.BLUE}{Style.BRIGHT}Bienvenido a la Alianza Rebelde.{Style.RESET_ALL}")
            print("==================================")
            Alianza = True
        if opcion == 2:
            sonido1.play()
            pygame.mixer.music.load(dark_side)
            pygame.mixer.music.play()
            limpiar_terminal() #Limpiamos la terminal
            print("=================================")
            print(f"Seleción exitosa ✅ \n{Fore.RED}{Style.BRIGHT}Bienvenido a el Imperio Galáctico{Style.RESET_ALL}.")
            print("=================================")
            Imperio = True
    except ValueError:
        sonido3.play()
        limpiar_terminal() #Limpiamos la terminal
        print("=============================================")
        print("Error ⚠️  selecciona (1) o (2) para continuar.")
        print("=============================================\n")
        continue
    if opcion < 1 or opcion > 2:
        sonido3.play()
        limpiar_terminal() #Limpiamos la terminal
        print("=============================================")
        print("Error ⚠️  selecciona (1) o (2) para continuar.")
        print("=============================================\n")
        continue
    else:
        break

# Sección de Cargando...
def mostrar_cargando_y_limpiar(mensaje="Cargando"):
    print(f"\n{mensaje} ", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True) 
        sys.stdout.flush()
        time.sleep(1.5) 
    time.sleep(1.5)
    limpiar_terminal()
mostrar_cargando_y_limpiar()


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
            print(f"\n{Fore.BLUE}{Style.BRIGHT}[MENÚ PRINCIPAL DE LA ALIANZA ⚔️ ]{Style.RESET_ALL}")
        elif Imperio == True:
            print(f"\n{Fore.RED}{Style.BRIGHT}[MENÚ PRINCIPAL DEL IMPERIO 🤖]{Style.RESET_ALL}")
        print("\n1. Listar Misiones 📋\n2. Añadir Misión ➕\n3. Eliminar Misión ❌\n4. Ver Detalles 👀\n5. Salir 📤")
        opcion = int(input("\n▶ Tu opcion: "))
    
        if opcion == 1:
            sonido1.play()
            from listar_misiones import mostrar_misiones_agendadas
            mostrar_misiones_agendadas()
            salir_confirmado = False
    
        elif opcion == 2:
            sonido1.play()
            limpiar_terminal()
            pygame.mixer.music.stop()
            from añadir_mision import añadir_nueva_mision # Importar todo el módulo para añadir la misión
            pygame.mixer.music.load(light_side_mission)
            pygame.mixer.music.play(-1)
            añadir_nueva_mision() # Llamar a la función
            salir_confirmado = False
    
        elif opcion == 3:
            sonido1.play()
            time.sleep(0.25)
            print("En proceso")
            salir_confirmado = True
    
        elif opcion == 4:
            sonido1.play()
            time.sleep(0.25)
            print("En proceso")
            salir_confirmado = True
    
        elif opcion == 5: # Función de salir
            sonido4.play()
            limpiar_terminal() #Limpiamos la terminal
            salir_confirmado = False
            while True:
                print("\n¿Estás seguro de que deseas salir? 😟\nPresiona 1 para salir ❌\nPresiona 2 para volver atrás ↩️\n")
                try:
                    preguntar = int(input("▶  "))
                    
                    if preguntar == 1:
                        sonido1.play()
                        limpiar_terminal()
                        pygame.mixer.music.stop()
                        sonido5.play()
                        print("==================================")
                        print("Que la Fuerza te acompañe ✒️  (...)")
                        print("==================================")
                        time.sleep(1.25)
                        print("\nHas salido de la aplicación.")
                        time.sleep(1.5)
                        salir_confirmado = True
                        break
                    
                    elif preguntar == 2:
                        limpiar_terminal()
                        sonido2.play()
                        break
                        
                    elif preguntar < 1 or preguntar > 2:
                        sonido3.play()
                        limpiar_terminal() #Limpiamos la terminal
                        print("\n============================")
                        print("Error ⚠️  selecciona (1) o (2).")
                        print("==============================")
                except ValueError:
                    sonido3.play()
                    limpiar_terminal() #Limpiamos la terminal
                    print("\n==============================")
                    print("Error ⚠️  selecciona (1) o (2).")
                    print("==============================")
                    continue
    
    except ValueError:
        sonido3.play()
        limpiar_terminal()
        print("\n========================================")
        print("Opcion incorrecta ❌ vuelve a intentarlo")
        print("========================================")
        continue
    
    if opcion < 1 or opcion > 5:
        sonido3.play()
        limpiar_terminal() #Limpiamos la terminal
        print("\n=====================================")
        print("Error ⚠️  ingresa un número del 1 - 5.")
        print("=====================================")
        continue
    if salir_confirmado:
        break