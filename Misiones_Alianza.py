import datetime
from typing import List

class Evento:
    def __init__(self, id_evento: str,nombre: str, bando: str,recursos_requeridos_ids: List[str],recursos_prohibidos_ids: List[str],descripcion: str = ""):
        self.id = id_evento # Identificador único del evento
        self.nombre = nombre # Nombre de la misión
        self.bando = bando # Bando ('República' o 'Separatista')
        self.recursos_requeridos_ids = recursos_requeridos_ids # Lista de IDs de los recursos que este evento necesita.
        self.recursos_prohibidos_ids = recursos_prohibidos_ids # Lista de IDs de los recursos que no pueden estar en la misión
        self.descripcion = descripcion # Descripción sobre la misión

    def diccionario(self): #Serializa el objeto Evento para guardarlo en JSON.
        return {
            "id": self.id,
            "nombre": self.nombre,
            "bando": self.bando,
            "recursos_requeridos_ids": self.recursos_requeridos_ids,
            "recursos_prohibidos_ids": self.recursos_prohibidos_ids,
            "descripcion": self.descripcion
            }

# [M001]
recognition_mission_tattol = Evento(
    id_evento="M001",
    nombre="Reconocimiento en Tattoine 🏜️ ",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A001","A005","A006"],
    recursos_prohibidos_ids= ["A000","A002","A003","A007","A008","A009","A010","A011","A012"],
    descripcion= """Misión Secreta de la Rebelión donde la Princesa Leia 
llevó los planos de la Estrella de la Muerte a Obi-Wan,
por medio de un holograma transmitido por R2-D2 y C-3PO""")

# [M002]
rescue_princess_leia = Evento(
    id_evento="M002",
    nombre="Rescate de la Princesa Leia 👑",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A000","A002","A003","A004"],
    recursos_prohibidos_ids=["A001","A008","A009","A012"],
    descripcion=  """Misión crucial donde Luke Skywalker,
Han Solo y Chewbacca intentarán liberar a Leia
de la Celda 2187 de la Estrella de la Muerte.""")

# [M003] 
attack_death_star = Evento(
    id_evento="M003",
    nombre="Ataque a la Estrella de la Muerte 🌑",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A000","A008","A012"],
    recursos_prohibidos_ids=["A004","A009"],
    descripcion= """Misión liderada por Luke Skywalker 
para destruir la Estrella de la Muerte,
estación espacial imperial del tamaño 
de la luna con gran poder destructivo.""") 

# [M004]
battle_hoth = Evento(
    id_evento="M004",
    nombre="Batalla de Hoth 🥶",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A000","A001","A002"],
    recursos_prohibidos_ids=["A004","A009"],
    descripcion= """Enfrentamiento en el gélido planeta Hoth, 
donde el Imperio Galáctico ataca la Base Secreta 
Rebelde para destruir su generador de escudo.""")

# Lista de todas las misiones disponibles
misiones_alianza = [recognition_mission_tattol,rescue_princess_leia,attack_death_star,battle_hoth,]

# Para las misiones del Imperio usaré este emoji ✳️