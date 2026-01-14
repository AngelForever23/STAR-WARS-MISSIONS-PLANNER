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
        self.descripcion = descripcion # Descripción
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
luke_skywalker = Recurso("A000", "Luke Skywalker 👤", "Luke Skywalker   👤",  "(Personaje)", "Alianza", 1, resourse_sounds[0],
                        "Héroe y Jedi protagonista de Star Wars.")
princesa_leia = Recurso("A001", "Princesa Leia 👤", "Princesa Leia    👤", "(Personaje)", "Alianza", 1, resourse_sounds[1],
                        "Princesa rebelde y Senadora conocida por su liderazgo, inteligencia y valentía.")
han_solo = Recurso("A002", "Han Solo 👤", "Han Solo         👤", "(Personaje)", "Alianza", 1, resourse_sounds[2],
                    "Contrabandista corelliano capitán del Halcón Milenario.")
chewbacca = Recurso("A003", "Chewbacca 🦁", "Chewbacca        🦁", "(Personaje)", "Alianza", 1, resourse_sounds[3],
                    "Leal amigo y copiloto de Han Solo.")
obi_wan = Recurso("A004", "Obi-Wan Kenobi 👤", "Obi-Wan Kenobi   👤", "(Personaje)", "Alianza", 1,  resourse_sounds[4],
                    "Legendario Maestro Jedi, paciente y astuto.")
r2_d2 = Recurso("A005", "R2-D2 👾", "R2-D2            👾", " (Droide)  ", "Alianza", 1, resourse_sounds[5],
                "Droide astromecánico pequeño e inteligente, muy hábil en la reparación.")
c_3po = Recurso("A006", "C-3PO 🤖", "C-3PO            🤖", " (Droide)  ", "Alianza", 1, resourse_sounds[6],
                "Droide de protocolo dorado y compañero inseparable de R2-D2.")
halcon_milenario = Recurso("A007", "Halcón Milenario 🛸", "Halcón Milenario 🛸", "  (Nave)   ", "Alianza", 1, resourse_sounds[7],
                "Carguero ligero YT-1300 modificado por Han Solo y Chewbacca, conocido como (el cubo de basura más velóz de la galaxia).")
x_wing = Recurso("A008", "X-Wing ✈️ ", "X-Wing           ✈️", "   (Nave)   ", "Alianza", 5, resourse_sounds[8],
                "Nave tipo caza estelar de la Alianza Rebelde.")
y_wing = Recurso("A009", "Y-Wing 🛩️ ", "Y-Wing           🛩️", "   (Nave)   ", "Alianza", 1, resourse_sounds[9],
                "Nave tipo caza-bombardero robusto y veterano.")
lightsaber = Recurso("A010", "Sable de Luz ⚔️ ", "Sable de Luz    ⚔️ ", " (Equipo)  ", "Alianza", 2, resourse_sounds[10],
                    "Espada de energía, elegante y poderosa. Usada por los Jedi y Sith.")
blaster = Recurso("A011", "Bláster 🔫", "Bláster         🔫", " (Equipo)  ", "Alianza", 5, resourse_sounds[11],
                "Armas de energía que disparan rayos de plasma comprimido")
traje_piloto = Recurso("A012", "Traje de Piloto 🧥", "Traje de Piloto 🧥", " (Equipo)  ", "Alianza", 5, resourse_sounds[12],
                        "Monos de vuelo ajustados, funcionales y con equipo integrado.")

# Lista con los recursos para acceder fácilmente
recursos_alianza = [
    luke_skywalker,
    princesa_leia,
    han_solo,
    chewbacca,
    obi_wan,
    r2_d2,
    c_3po,
    halcon_milenario,
    x_wing,
    y_wing,
    lightsaber,
    blaster,
    traje_piloto
    ]