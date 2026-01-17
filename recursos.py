# Clase Recurso para asignar las propiedades y funciones de los objetos
class Recurso:
    def __init__(self, id_recurso: str, nombre: str, nombre_inventario: str, tipo_recurso: str, bando: str,  cantidad: int, sonido, descripcion: str = ""):
        self.id = id_recurso # Identificador único del recurso
        self.nombre = nombre # Nombre del recurso
        self.nombre_inventario = nombre_inventario
        self.tipo_recurso = tipo_recurso
        self.bando = bando # Bando al que pertenece ('República' o 'Separatista')
        self.cantidad = cantidad # Cantidad de unidades en la tropa
        self.sonido = sonido # Sonido o Frase que hace cada recurso cuando lo seleccionas
        self.descripcion = descripcion # Descripción de cada recurso
        
        # Agenda Semanal de cada recurso
        self.agenda = {
            "Lunes": [],
            "Martes": [],
            "Miércoles": [],
            "Jueves": [],
            "Viernes": [],
            "Sábado": [],
            "Domingo": []
        }
    
    # Esta función es importante ya que en un json no se pueden guardar los objetos (POO),
    # así que la transformamos en un diccionario.
    def diccionario(self): # Serializa el objeto para guardarlo en JSON.
        return {
            "nombre": self.nombre,
            "agenda": self.agenda
        }

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Esto esconde el mensaje de bienvenida de pygame

# Importamos pygame (Para reproducir música) 
import pygame
pygame.mixer.init()
from musica_sonidos import resourse_sounds

# Recursos de la Alianza
luke_skywalker = Recurso("A000", "Luke Skywalker 👤", "Luke Skywalker    👤",  "(Personaje)", "Alianza", 1, resourse_sounds[0],
                        "Héroe y Jedi protagonista de Star Wars.")

obi_wan = Recurso("A001", "Obi-Wan Kenobi 👤", "Obi-Wan Kenobi    👤", "(Personaje)", "Alianza", 1,  resourse_sounds[1],
                    "Legendario Maestro Jedi, paciente y astuto.")

princesa_leia = Recurso("A002", "Princesa Leia 👤", "Princesa Leia     👤", "(Personaje)", "Alianza", 1, resourse_sounds[2],
                        "Princesa rebelde y Senadora conocida por su liderazgo.")

han_solo = Recurso("A003", "Han Solo 👤", "Han Solo          👤", "(Personaje)", "Alianza", 1, resourse_sounds[3],
                    "Contrabandista corelliano capitán del Halcón Milenario.")

chewbacca = Recurso("A004", "Chewbacca 🦁", "Chewbacca         🦁", "(Personaje)", "Alianza", 1, resourse_sounds[4],
                    "Leal amigo y copiloto de Han Solo.")

lando_calrissian = Recurso("A005", "Lando Calrissian 👤", "Lando Calrissian  👤", "(Personaje)", "Alianza", 1, resourse_sounds[5],
                            "Antiguo propietario del Halcón Milenario y administrador de Ciudad Nube.")

r2_d2 = Recurso("A006", "R2-D2 👾", "R2-D2             👾", " (Droide)  ", "Alianza", 1, resourse_sounds[6],
                "Droide astromecánico pequeño e inteligente, muy hábil en la reparación.")

c_3po = Recurso("A007", "C-3PO 🤖", "C-3PO             🤖", " (Droide)  ", "Alianza", 1, resourse_sounds[7],
                "Droide de protocolo dorado y compañero inseparable de R2-D2.")

halcon_milenario = Recurso("A008", "Halcón Milenario 🛸", "Halcón Milenario  🛸", "  (Nave)   ", "Alianza", 1, resourse_sounds[8],
                "Carguero ligero YT-1300 modificado por Han Solo y Chewbacca.")

x_wing = Recurso("A009", "X-Wing ✈️ ", "X-Wing            ✈️", "   (Nave)   ", "Alianza", 5, resourse_sounds[9],
                "Nave tipo caza estelar de la Alianza Rebelde.")

a_wing = Recurso("A010", "A-Wing 🛩️", "A-Wing           🛩️", "   (Nave)   "   , "Alianza", 3, resourse_sounds[10],
                "Interceptor rebelde, el caza más rápido de la galaxia.")

lightsaber = Recurso("A011", "Sable de Luz ⚔️ ", "Sable de Luz     ⚔️ ", " (Equipo)  ", "Alianza", 1, resourse_sounds[11],
                    "Espada de energía, elegante y poderosa. Usada por los Jedi y Sith.")

blaster = Recurso("A012", "Bláster 🔫", "Bláster          🔫", " (Equipo)  ", "Alianza", 5, resourse_sounds[12],
                "Armas de energía que disparan rayos de plasma comprimido")

traje_piloto = Recurso("A013", "Traje de Piloto 🧥", "Traje de Piloto  🧥", " (Equipo)  ", "Alianza", 5, resourse_sounds[13],
                        "Monos de vuelo ajustados, funcionales y con equipo integrado.")

escudo_deflector = Recurso("A014", "Escudo Deflector 🛡️", "Escudo Deflector 🛡️ ", " (Equipo)  ", "Alianza", 3, resourse_sounds[14],
                            "Dispositivo de protección personal contra disparos láser.")

detonadores_termicos = Recurso("A015", "Detonadores Térmicos 💣", "Detonadores      💣", " (Equipo)  ", "Alianza", 4, resourse_sounds[15],
                                "Explosivos compactos de gran potencia destructiva usados por Leia.")

equipo_camuflaje = Recurso("A016", "Equipo de Camuflaje 🌿", "Equipo Camuflaje 🌿", " (Equipo)  ", "Alianza", 5, resourse_sounds[16],
                            "Vestimenta para misiones encubiertas en entornos forestales.")



# Lista con los recursos para acceder fácilmente
recursos_alianza = [
    luke_skywalker,
    obi_wan,
    princesa_leia,
    han_solo,
    chewbacca,
    lando_calrissian,
    r2_d2,
    c_3po,
    halcon_milenario,
    x_wing,
    a_wing,
    lightsaber,
    blaster,
    traje_piloto,
    escudo_deflector,
    detonadores_termicos,
    equipo_camuflaje,
    ]