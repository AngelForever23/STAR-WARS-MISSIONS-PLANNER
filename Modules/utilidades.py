# Función para limpiar la terminal
def limpiar_terminal():
    import os
    os.system('cls')


# Función para mostrar un mensaje de "Cargando..." con animación.
def mostrar_cargando_y_limpiar(mensaje): # <-- Aquí se escribe el mensaje de "Carga"
    from time import sleep
    frames = ["🌑","🌒","🌓","🌔","🌕"]
    for frame in frames:
        print(f"\r{frame} {mensaje}...", end="", flush=True)
        sleep(0.9)
    sleep(1)
    limpiar_terminal()
