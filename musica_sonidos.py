import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.mixer.init()

# OBTENER LA RUTA BASE DEL PROYECTO
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
RUTA_AUDIO = os.path.join(RUTA_BASE, "Audio")

# MUSICA DE FONDO 
star_wars_intro = os.path.join(RUTA_AUDIO, "Background Music", "Star Wars Intro.mp3")
light_side = os.path.join(RUTA_AUDIO, "Background Music", "light_side.mp3")
light_side_menu = os.path.join(RUTA_AUDIO, "Background Music", "light_side_menu.mp3")
light_side_mission = os.path.join(RUTA_AUDIO, "Background Music", "light_side_mission.mp3")
dark_side = os.path.join(RUTA_AUDIO, "Background Music", "dark_side.mp3")
dark_side_menu = os.path.join(RUTA_AUDIO, "Background Music", "dark_side_menu.mp3")
mision_exito_alianza = os.path.join(RUTA_AUDIO, "Background Music", "Mision_exito_alianza.mp3")

# EFECTOS DE SONIDO
sonido_error = os.path.join(RUTA_AUDIO, "Sounds", "Error.mp3")
buttonproceed = os.path.join(RUTA_AUDIO, "Sounds", "Buttonproceed.mp3")
buttonback = os.path.join(RUTA_AUDIO, "Sounds", "Buttonback.mp3")
door = os.path.join(RUTA_AUDIO, "Sounds", "Door.mp3")
exit_sound = os.path.join(RUTA_AUDIO, "Sounds", "Exit.mp3")
welcome_sound = os.path.join(RUTA_AUDIO, "Sounds", "Welcome.mp3")

# Cargar sonidos
sonido0 = pygame.mixer.Sound(welcome_sound)
sonido1 = pygame.mixer.Sound(buttonproceed)
sonido2 = pygame.mixer.Sound(buttonback)
sonido3 = pygame.mixer.Sound(sonido_error)
sonido4 = pygame.mixer.Sound(door)
sonido5 = pygame.mixer.Sound(exit_sound)

# SONIDOS DE RECURSOS
luke_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Luke_sound.mp3"))
obi_wan_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Obi_wan_sound.mp3"))
princess_leia_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Princess_leia_sound.mp3"))
han_solo_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Han_solo_sound.mp3"))
chewbacca_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Chewbacca_sound.mp3"))
lando_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Lando_sound.mp3"))
r2_d2_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "R2d2_sound.mp3"))
c3po_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "C3po_sound.mp3"))
halcon_milenario_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Mighty_falcon_sound.mp3"))
x_wing_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "X_wing_sound.mp3"))
a_wing_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "A_wing_sound.mp3"))
lightsaber_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Lightsaber_sound.mp3"))
blaster_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Gun_blaster_sound.mp3"))
traje_piloto_sound = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Equipment_traje_piloto_sound.mp3"))
escudo_deflector = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Escudo_deflector_sound.mp3"))
detonadores_termicos = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Detonador_sound.mp3"))
equipo_camuflaje = pygame.mixer.Sound(os.path.join(RUTA_AUDIO, "Resource Sounds", "Equipo_camuflaje_sound.mp3"))

# Lista para acceder fácilmente a los sonidos de los recursos
resourse_sounds = [
    luke_sound,
    obi_wan_sound,
    princess_leia_sound,
    han_solo_sound,
    chewbacca_sound,
    lando_sound,
    r2_d2_sound,
    c3po_sound,
    halcon_milenario_sound,
    x_wing_sound,
    a_wing_sound,
    lightsaber_sound,
    blaster_sound,
    traje_piloto_sound,
    escudo_deflector,
    detonadores_termicos,
    equipo_camuflaje,
]