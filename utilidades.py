# Función para limpiar la terminal
def limpiar_terminal():
    import os
    os.system('cls')


# Función para mostrar un mensaje de "Cargando..."
def mostrar_cargando_y_limpiar(mensaje): # <-- Aquí se escribe el mensaje de "Carga"
    import time
    import sys
    print(f"\n{mensaje} ", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True) 
        sys.stdout.flush()
        time.sleep(1.5) 
    time.sleep(1.5)
    limpiar_terminal()