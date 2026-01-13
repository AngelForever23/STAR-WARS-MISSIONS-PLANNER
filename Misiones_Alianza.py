import datetime
from datetime import timedelta
from typing import List

# from añadir_mision import guardar_dia
# from añadir_mision import dia
# guardar_dia_semana = guardar_dia(dia)

class Evento:
    def __init__(self, id_evento: str,nombre: str, bando: str,fecha_inicio: datetime,fecha_fin: datetime,recursos_requeridos_ids: List[str],recursos_prohibidos_ids: List[str],descripcion: str = ""):
        self.id = id_evento # Identificador único del evento
        self.nombre = nombre # Nombre de la misión
        self.bando = bando # Bando ('República' o 'Separatista')
        self.fecha_inicio = fecha_inicio # El tiempo en que ocurre el evento.
        self.fecha_fin = fecha_fin
        self.recursos_requeridos_ids = recursos_requeridos_ids # Lista de IDs de los recursos que este evento necesita.
        self.recursos_prohibidos_ids = recursos_prohibidos_ids # Lista de IDs de los recursos que no pueden estar en la misión
        self.descripcion = descripcion

    def obtener_duracion_dias(self) -> int:
        return(self.fecha_fin - self.fecha_inicio).days

    def obtener_dia_semana(self):
        semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
        return semana[self.fecha_inicio.weekday()] # weekday() devuelve un número del 0 - 6 de un objeto datetime

        
    def __str__(self): # Devuelve una representación legible del evento.
        dia_semana = self.obtener_dia_semana()
        duracion_dias = self.obtener_duracion_dias()
        return (f"❇️  Misión: {self.nombre} | Bando: {self.bando} | "f"Inicio 🕛 : {dia_semana} | Duración ⏳ : {duracion_dias} día.")

    def diccionario(self): #Serializa el objeto Evento para guardarlo en JSON.
        return {
            "id": self.id,
            "nombre": self.nombre,
            "bando": self.bando,
            # Convertimos los objetos datetime a strings para que JSON pueda guardarlos
            "fecha_inicio": self.fecha_inicio.isoformat(),
            "fecha_fin": self.fecha_fin.isoformat(),
            "recursos_requeridos_ids": self.recursos_requeridos_ids
            }


hoy = datetime.datetime.now().replace(hour=8,minute=00,second=00,microsecond=00)
mañana = hoy + timedelta(days=1)

# [M001] 
recognition_mission_tattol = Evento(
    id_evento="M001",
    nombre="Reconocimiento en Tattoine 🏜️ ",
    bando="Alianza 🪯 ",
    fecha_inicio=hoy,
    fecha_fin=mañana,
    recursos_requeridos_ids=["A001","A003","A005","A006"],
    recursos_prohibidos_ids= ["A000","A002","A004","A007","A008","A009","A010","A011","A012"],
    descripcion= """Misión Secreta de la Rebelión donde la Princesa Leia 
llevó los planos de la Estrella de la Muerte a Obi-Wan, 
por medio de un holograma transmitido por R2-D2 y C-3PO""")

# [M002]
rescue_princess_leia = Evento(
    id_evento="M002",
    nombre="Rescate de la Princesa Leia 👑",
    bando="Alianza 🪯 ",
    fecha_inicio=hoy,
    fecha_fin=mañana,
    recursos_requeridos_ids=["A000","A002","A003","A010","A011"],
    recursos_prohibidos_ids=["A001"],
    descripcion=  """Misión crucial donde Luke Skywalker, 
Han Solo y Chewbacca intentarán liberar a Leia 
de la Celda 2187 de la Estrella de la Muerte.""") 

# [M003] 
attack_death_star = Evento(
    id_evento="M003",
    nombre="Ataque a la Estrella de la Muerte 🌑",
    bando="Alianza 🪯 ",
    fecha_inicio=hoy,
    fecha_fin=mañana,
    recursos_requeridos_ids=["R001","R009","R011","R013"],
    recursos_prohibidos_ids=[],
    descripcion= """Misión liderada por Luke Skywalker 
para destruir la Estrella de la Muerte,
estación espacial imperial del tamaño 
de la luna con gran poder destructivo.""") 

# [M004]
battle_hoth = Evento(
    id_evento="M004",
    nombre="Batalla de Hoth 🥶",
    bando="Alianza 🪯 ",
    fecha_inicio=hoy,
    fecha_fin=mañana,
    recursos_requeridos_ids=["A001","A002","A008","A011"],
    recursos_prohibidos_ids=[],
    descripcion= """Enfrentamiento en el gélido planeta Hoth, 
donde el Imperio Galáctico ataca la Base Secreta 
Rebelde para destruir su generador de escudo.""") 

# Lista de todas las misiones disponibles
misiones_alianza = [recognition_mission_tattol,rescue_princess_leia,attack_death_star,battle_hoth,]

# print(misiones_alianza[1])
# Para las misiones del Imperio usaré este emoji ✳️