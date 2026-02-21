from Functions.listar_misiones import misiones_planificadas_alianza,misiones_planificadas_imperio
from Models.recursos import recursos_alianza,recursos_imperio
from Models.misiones import misiones_alianza,misiones_imperio
from Functions.eliminar_mision_agenda import papelera_reciclaje_alianza,papelera_reciclaje_imperio
import json
import os

# Importamos cada misión (objeto) por separado
from Models.misiones import reconocimiento_tattoine,rescate_pricesa_leia,ataque_estrella_muerte,batalla_hoth,rescate_ciudad_nube,rescate_palacio_jabba,ataque_segunda_estrella_muerte,mision_endor_terrestre,confrontacion_final
from Models.misiones import interrogatorio_prisioneros,destruccion_alderaan,ataque_base_rebelde,captura_solo,construccion_estrella,batalla_endor

# OBTENER LA RUTA BASE DEL PROYECTO
RUTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_SAVED_DATA = os.path.join(RUTA_BASE, "Saved Data")

# En caso de que no exista la carpeta Saved Data
if not os.path.exists(RUTA_SAVED_DATA):
    os.makedirs(RUTA_SAVED_DATA)

# Variable constante para encontrar las misiones (objetos) según sus Ids
TODAS_LAS_MISIONES = {
    "M001": reconocimiento_tattoine,
    "M002": rescate_pricesa_leia,
    "M003": ataque_estrella_muerte,
    "M004": batalla_hoth,
    "M005": rescate_ciudad_nube,
    "M006": rescate_palacio_jabba,
    "M007": ataque_segunda_estrella_muerte,
    "M008": mision_endor_terrestre,
    "M009": confrontacion_final,
    "M010": interrogatorio_prisioneros,
    "M011": destruccion_alderaan,
    "M012": ataque_base_rebelde,
    "M013": captura_solo,
    "M014": construccion_estrella,
    "M015": batalla_endor,
}


def guardar_estado():
    
    # Esto corresponde a los datos guardados de la alianza
    # 1
    agendas_de_recursos_alianza = []
    for recurso in recursos_alianza: # Recorremos todos los recursos de la alianza (objetos de POO)
        agendas_de_recursos_alianza.append(recurso.diccionario()) # Las convertimos en un diccionario y las agregamos a [agendas_de_recursos]
    
    # 2
    misiones_agendadas_alianza = [] 
    for mision in misiones_planificadas_alianza: # Recorremos las misiones que agendamos en la semana (lista de diccionarios)
        misiones_agendadas_alianza.append(mision) # añadimos cada misión (diccionario) a [misiones_agendadas]
    
    # 3
    misiones_restantes_alianza = []
    for m in misiones_alianza: # Recorremos las misiones que nos quedan en las misiones de la alianza (objetos POO)
        misiones_restantes_alianza.append(m.diccionario()) # Las convertimos en un diccionario y las añadimos a [misiones_restantes]
    
    # 4
    papelera_diccionario_alianza = []
    for mision in papelera_reciclaje_alianza: # Recorremos las misiones que están en la papelera (objetos POO)
        papelera_diccionario_alianza.append(mision.diccionario()) # Las convertimmos en un diccionario y las añadimos a [papelera_diccionario]
    
    
    # Guardar todos los archivos como json en la carpeta Save Data
    with open(os.path.join(RUTA_SAVED_DATA,"agendas_recursos_alianza.json"), "w", encoding="utf-8") as archivo:
        json.dump(agendas_de_recursos_alianza, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"misiones_agendadas_alianza.json"), "w", encoding="utf-8") as archivo:
        json.dump(misiones_agendadas_alianza, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"misiones_restantes_alianza.json"), "w", encoding="utf-8") as archivo:
        json.dump(misiones_restantes_alianza, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"papelera_alianza.json"), "w", encoding="utf-8") as archivo:
        json.dump(papelera_diccionario_alianza, archivo, indent=4, ensure_ascii=False)

    
    
    # Esto corresponde a los datos guardados del imperio
    # 1
    agendas_de_recursos_imperio = []
    for recurso in recursos_imperio: # Recorremos todos los recursos de la alianza (objetos de POO)
        agendas_de_recursos_imperio.append(recurso.diccionario()) # Las convertimos en un diccionario y las agregamos a [agendas_de_recursos]
    
    # 2
    misiones_agendadas_imperio = [] 
    for mision in misiones_planificadas_imperio: # Recorremos las misiones que agendamos en la semana (lista de diccionarios)
        misiones_agendadas_imperio.append(mision) # añadimos cada misión (diccionario) a [misiones_agendadas]
    
    # 3
    misiones_restantes_imperio = []
    for m in misiones_imperio: # Recorremos las misiones que nos quedan en las misiones de la alianza (objetos POO)
        misiones_restantes_imperio.append(m.diccionario()) # Las convertimos en un diccionario y las añadimos a [misiones_restantes]
    
    # 4
    papelera_diccionario_imperio = []
    for mision in papelera_reciclaje_imperio: # Recorremos las misiones que están en la papelera (objetos POO)
        papelera_diccionario_imperio.append(mision.diccionario()) # Las convertimmos en un diccionario y las añadimos a [papelera_diccionario]
    
    
    # Guardar todos los archivos como json en la carpeta Save Data
    with open(os.path.join(RUTA_SAVED_DATA,"agendas_recursos_imperio.json"), "w", encoding="utf-8") as archivo:
        json.dump(agendas_de_recursos_imperio, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"misiones_agendadas_imperio.json"), "w", encoding="utf-8") as archivo:
        json.dump(misiones_agendadas_imperio, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"misiones_restantes_imperio.json"), "w", encoding="utf-8") as archivo:
        json.dump(misiones_restantes_imperio, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"papelera_imperio.json"), "w", encoding="utf-8") as archivo:
        json.dump(papelera_diccionario_imperio, archivo, indent=4, ensure_ascii=False)


def cargar_estado():
    
    # Verificar si existen los archivos Json antes de cargarlos 
    archivos = [
        os.path.join(RUTA_SAVED_DATA,"agendas_recursos_alianza.json"),
        os.path.join(RUTA_SAVED_DATA,"misiones_agendadas_alianza.json"),
        os.path.join(RUTA_SAVED_DATA,"misiones_restantes_alianza.json"),
        os.path.join(RUTA_SAVED_DATA,"papelera_alianza.json"),
        os.path.join(RUTA_SAVED_DATA,"agendas_recursos_imperio.json"),
        os.path.join(RUTA_SAVED_DATA,"misiones_agendadas_imperio.json"),
        os.path.join(RUTA_SAVED_DATA,"misiones_restantes_imperio.json"),
        os.path.join(RUTA_SAVED_DATA,"papelera_imperio.json")]
    
    # Si algún archivo json no existe entonces es la primera vez que se abre la aplicación o el usuario los borró :)
    if not all(os.path.exists(archivo) for archivo in archivos):
        return False # No hay estado que cargar
    
    
    try:
        # 1. Cargar las agendas de los recursos de la alianza
        with open(os.path.join(RUTA_SAVED_DATA,"agendas_recursos_alianza.json"), "r", encoding="utf-8") as archivo:
            agendas_recursos_cargadas = json.load(archivo)

        for indice, agenda_recurso in enumerate(agendas_recursos_cargadas): # Separamos 
            recursos_alianza[indice].agenda = agenda_recurso["agenda"]

        # 2. Cargar las misiones agendadas de la alianza
        with open(os.path.join(RUTA_SAVED_DATA,"misiones_agendadas_alianza.json"), "r", encoding="utf-8") as archivo:
            misiones_agendadas_cargadas = json.load(archivo)
            misiones_planificadas_alianza.clear() # Limpiamos las misiones planificadas (viejas)
            misiones_planificadas_alianza.extend(misiones_agendadas_cargadas) # Añadimos las misiones que agendamos (diccionarios) a [misiones_planificadas]

        # 3. Cargar las misiones restantes de la alianza
        misiones_alianza.clear() # Borramos todas las misiones de la alianza

        with open(os.path.join(RUTA_SAVED_DATA,"misiones_restantes_alianza.json"), "r", encoding="utf-8") as archivo:
            mision_diccionario = json.load(archivo)

        for datos_mision in mision_diccionario: # Misión diccionario es la lista que contiene las misiones (dicionario) que nos quedan [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            misiones_alianza.append(mision_objeto)

        # 4. Cargar la papelera de reciclaje de la alianza
        papelera_reciclaje_alianza.clear()
        with open(os.path.join(RUTA_SAVED_DATA,"papelera_alianza.json"), "r", encoding="utf-8") as archivo:
            papelera_diccionario_alianza = json.load(archivo) 

        for datos_mision in papelera_diccionario_alianza: # Papelera diccionario es la lista que contiene las misiones (dicionario) que fueron agendadas y eliminadas [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            papelera_reciclaje_alianza.append(mision_objeto)
        
        
        
        
        # 1. Cargar las agendas de los recursos del imperio
        with open(os.path.join(RUTA_SAVED_DATA,"agendas_recursos_imperio.json"), "r", encoding="utf-8") as archivo:
            agendas_recursos_cargadas = json.load(archivo)

        for indice, agenda_recurso in enumerate(agendas_recursos_cargadas): # Separamos 
            recursos_imperio[indice].agenda = agenda_recurso["agenda"]

        # 2. Cargar las misiones agendadas del imperio
        with open(os.path.join(RUTA_SAVED_DATA,"misiones_agendadas_imperio.json"), "r", encoding="utf-8") as archivo:
            misiones_agendadas_cargadas = json.load(archivo)
            misiones_planificadas_imperio.clear() # Limpiamos las misiones planificadas (viejas)
            misiones_planificadas_imperio.extend(misiones_agendadas_cargadas) # Añadimos las misiones que agendamos (diccionarios) a [misiones_planificadas]

        # 3. Cargar las misiones restantes del imperio
        misiones_imperio.clear() # Borramos todas las misiones del imperio

        with open(os.path.join(RUTA_SAVED_DATA,"misiones_restantes_imperio.json"), "r", encoding="utf-8") as archivo:
            mision_diccionario = json.load(archivo)

        for datos_mision in mision_diccionario: # Misión diccionario es la lista que contiene las misiones (dicionario) que nos quedan [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            misiones_imperio.append(mision_objeto)

        # 4. Cargar la papelera de reciclaje del imperio
        papelera_reciclaje_imperio.clear()
        with open(os.path.join(RUTA_SAVED_DATA,"papelera_imperio.json"), "r", encoding="utf-8") as archivo:
            papelera_diccionario_imperio = json.load(archivo) 

        for datos_mision in papelera_diccionario_imperio: # Papelera diccionario es la lista que contiene las misiones (dicionario) que fueron agendadas y eliminadas [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            papelera_reciclaje_imperio.append(mision_objeto)
        
        return True
    
    except Exception as e:
        print(f"❌ Error al cargar el estado: \n▶ {e}")
        return False




