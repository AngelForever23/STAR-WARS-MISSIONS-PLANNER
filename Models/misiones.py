from typing import List

class Evento:
    def __init__(self, id_evento: str,nombre: str, bando: str,recursos_requeridos_ids: List[str],recursos_prohibidos_ids: List[str],descripcion: str = ""):
        self.id = id_evento # Identificador único del evento
        self.nombre = nombre # Nombre de la misión
        self.bando = bando # Bando ('Alianza' o 'Imperio')
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

# MISIONES DE LA ALIANZA REBELDE
# Misiones [M001,M002,M003] badadas en la Película "Star Wars Episode 4 - A New Hope"
# [M001]
reconocimiento_tattoine = Evento(
    id_evento="M001",
    nombre="🏜️  Reconocimiento en Tattoine            ",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A002","A006","A007"], # Leia y los drides
    recursos_prohibidos_ids= ["A003","A004","A005","A008","A009","A010","A012","A013","A014","A015","A016"],
    descripcion= """Misión Secreta de la Rebelión donde la Princesa Leia 
llevó los planos de la Estrella de la Muerte a Obi-Wan,
por medio de un holograma transmitido por R2-D2 y C-3PO""")

# [M002]
rescate_pricesa_leia = Evento(
    id_evento="M002",
    nombre="👑 Rescate de la Princesa Leia           ",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A000","A001","A003","A004"], # Luke ,Obi ,Han ,Chewacca
    recursos_prohibidos_ids=["A002","A005","A009","A010","A013","A014","A015","A016"], 
    descripcion=  """Misión crucial donde Luke Skywalker, Obi-Wan,
Han Solo y Chewbacca intentarán liberar a Leia
de la Celda 2187 de la Estrella de la Muerte.""")

# [M003] 
ataque_estrella_muerte = Evento(
    id_evento="M003",
    nombre="🌑 Ataque a la Estrella de la Muerte     ",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A000","A009","A013"], # Luke, X-Wing, Traje,
    recursos_prohibidos_ids=["A001","A005","A010","A015","A016"],
    descripcion= """Luke Skywalker lidera un batallón de X-Wings,
para destruir la Estrella de la Muerte,
estación espacial imperial del tamaño
de la luna con gran poder destructivo.""")

# Misiones [M004,M005] basadas en la Película "Star Wars Episode 5 - The Empire Strikes Back"
# [M004]
batalla_hoth = Evento(
    id_evento="M004",
    nombre="🥶 Batalla de Hoth                       ",
    bando="Alianza 🪯 ",
    recursos_requeridos_ids=["A000","A002","A003","A010","A014"], # Luke, Leia, Han, A-Wing, Escudos
    recursos_prohibidos_ids=["A001","A005","A015","A016"],
    descripcion= """Enfrentamiento en el gélido planeta Hoth,
donde el Imperio Galáctico ataca la Base Secreta
Rebelde para destruir su generador de escudo.""")

# [M005]
rescate_ciudad_nube = Evento(
    id_evento="M005",
    nombre="☁️  Rescate en Ciudad Nube                ",
    bando="Alianza 🪯",
    recursos_requeridos_ids=["A000","A005","A006","A007","A008"], # Luke, Lando, R2-D2, C-3PO, Hálcon
    recursos_prohibidos_ids=["A001","A003","A009","A010","A013","A014","A015","A016"],
    descripcion="""Misión de rescate en Bespin después de la trampa de Vader.
Luke enfrenta a Vader y descubre la verdad sobre su padre.
Lando ayuda a escapar tras traicionar al Imperio."""
)

# Misiones [M006,M007,M008,M009] basadas en la Película "Star Wars Episode 6 - Return of the Jedi"
# [M006]
rescate_palacio_jabba = Evento(
    id_evento="M006",
    nombre="🏜️  Rescate de Han Solo - Palacio de Jabba",
    bando="Alianza 🪯",
    recursos_requeridos_ids=["A000","A002","A006","A007","A015"],  # Luke, Leia, droides, detonadores
    recursos_prohibidos_ids=["A001","A003","A005","A008","A009", "A010", "A012", "A013", "A014", "A016"],
    descripcion="""Misión de infiltración al palacio de Jabba el Hutt en Tatooine.
Leia se disfraza como cazarrecompensas Boushh con detonadores térmicos.
Luke demuestra sus poderes Jedi rescatando a Han Solo de la carbonita."""
)

# [M007]
ataque_segunda_estrella_muerte = Evento(
    id_evento="M007",
    nombre="🌑 Ataque a la Estrella de la Muerte II  ",
    bando="Alianza 🪯",
    recursos_requeridos_ids=["A005","A008"],  # Lando, Halcón
    recursos_prohibidos_ids=["A000","A001","A002","A003","A004","A006","A007","A011","A012","A015","A016"],
    descripcion="""Batalla espacial épica liderada por Lando en el Halcón Milenario
y Almirante Ackbar desde el Crucero Mon Calamari.
Los cazas rebeldes deben destruir el reactor de la Estrella de la Muerte
mientras la flota Imperial les tiende una trampa."""
)

# [M008]
mision_endor_terrestre = Evento(
    id_evento="M008",
    nombre="🌲 Misión en la Luna de Endor            ",
    bando="Alianza 🪯",
    recursos_requeridos_ids=["A000","A002","A003","A004","A016"],  # Luke, Leia, Han, Chewie, Camuflaje
    recursos_prohibidos_ids=["A001","A005","A008","A009","A010","A013"],
    descripcion="""Misión de comandos en la luna boscosa de Endor.
El equipo debe infiltrarse con camuflaje para destruir el generador
de escudo que protege la Segunda Estrella de la Muerte,
con ayuda de los Ewoks nativos."""
)

# [M009]
confrontacion_final = Evento(
    id_evento="M009",
    nombre="⚔️  Confrontación Final                   ",
    bando="Alianza 🪯",
    recursos_requeridos_ids=["A000","A011"],  # Solo Luke y su Sable de Luz
    recursos_prohibidos_ids=["A001","A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010", "A012", "A013", "A014", "A015","A016"],
    descripcion="""Luke se enfrenta al Emperador Palpatine y Darth Vader
en el trono de la Segunda Estrella de la Muerte.
Misión solitaria donde Luke debe redimir a su padre
y derrotar al lado oscuro."""
)

# Lista de todas las misiones disponibles de la alianza 
misiones_alianza = [
    reconocimiento_tattoine,
    rescate_pricesa_leia,
    ataque_estrella_muerte,
    batalla_hoth,
    rescate_ciudad_nube,
    rescate_palacio_jabba,
    ataque_segunda_estrella_muerte,
    mision_endor_terrestre,
    confrontacion_final
]

#===================================================================================================================================================#

# MISIONES DEL IMPERIO GALÁCTICO
# Misiones [M010,M011] badadas en la Película "Star Wars Episode 4 - A New Hope"
# [M010]
interrogatorio_prisioneros = Evento(
    id_evento="M010",
    nombre="❗ Interrogatorio de Prisioneros Rebeldes     ",
    bando="Imperio ☸️",
    recursos_requeridos_ids=["I000", "I001", "I006"],  # Vader, Tarkin, Oficial Imperial
    recursos_prohibidos_ids=["I002", "I004", "I007", "I010", "I011", "I012", "I013"],
    descripcion="""La princesa Leia y otros prisioneros rebeldes
son interrogados y amenzados para obtener
la ubicación de la base rebelde enemiga."""
)

# [M011]
destruccion_alderaan = Evento(
    id_evento="M011",
    nombre="💥 Destrucción de Alderaan                    ",
    bando="Imperio ☸️",
    recursos_requeridos_ids=["I001", "I008"],  # Tarkin, Estrella de la Muerte
    recursos_prohibidos_ids=["I002", "I004", "I007", "I011", "I012", "I013"],
    descripcion="""Demostración del poder imperial destruyendo 
el planeta Alderaan para intimidar a la Rebelión y 
obligar a la Princesa Leia a revelar la ubicación de la base rebelde."""
)

# Misiones [M012,M013] basadas en la Película "Star Wars Episode 5 - The Empire Strikes Back"
# [M012]
ataque_base_rebelde = Evento(
    id_evento="M012",
    nombre="❄️  Ataque a la Base Rebelde (Hoth)            ",
    bando="Imperio ☸️",
    recursos_requeridos_ids=["I000", "I003", "I009","I011", "I007", "I013"],  # Vader, Piett, Destructor Estelar, AT-AT, Piloto de AT-AT, Sonda Droide
    recursos_prohibidos_ids=["I001", "I002", "I004", "I008"],
    descripcion="""Asalto masivo a la base rebelde en el planeta Hoth 
usando caminantes AT-AT para destruir el generador 
de escudo y capturar a los líderes rebeldes."""
)

# [M013]
captura_solo = Evento(
    id_evento="M013",
    nombre="🧊 Captura de Han Solo                        ",
    bando="Imperio ☸️",
    recursos_requeridos_ids=["I000", "I004", "I005"],  # Vader, Boba Fett, Stormtroppers
    recursos_prohibidos_ids=["I001", "I002", "I003", "I007", "I008", "I009", "I010", "I011", "I012", "I013"],
    descripcion="""Trampa para capturar a Han Solo en Ciudad Nube.
Vader congela a Solo en carbonita como regalo 
para Jabba el Hutt y cebo para Luke Skywalker."""
)

# Misiones [M014,M015] basadas en la Película "Star Wars Episode 6 - Return of the Jedi"
# [M014]
construccion_estrella = Evento(
    id_evento="M014",
    nombre="🛠️  Construcción de la Estrella de la Muerte II",
    bando="Imperio ☸️",
    recursos_requeridos_ids=["I000", "I005", "I006"],  # Vader, Stormtroppers, Oficial Imp.
    recursos_prohibidos_ids=["I001", "I002", "I008", "I004", "I007", "I011", "I012", "I013"],
    descripcion="""Después del ataque de los rebeldes, 
la estación quedó completamente destruida, 
Vader y Tarkin inician su construcción."""
)

# [M015]
batalla_endor = Evento(
    id_evento="M015",
    nombre="🌲 Batalla de Endor                           ",
    bando="Imperio ☸️",
    recursos_requeridos_ids=["I000", "I002", "I005", "I012"],  # Vader, Emperador, Stormtropper, AT-ST
    recursos_prohibidos_ids=["I001" , "I004", "I007", "I008", "I013"],
    descripcion="""Trampa del Emperador para destruir la flota rebelde
y convertir a Luke Skywalker al lado oscuro.
La nueva Estrella de la Muerte aguarda completamente operacional."""
)

# Lista de todas las misiones disponibles del imperio 
misiones_imperio = [
    interrogatorio_prisioneros,
    destruccion_alderaan,
    ataque_base_rebelde,
    captura_solo,
    construccion_estrella,
    batalla_endor
]