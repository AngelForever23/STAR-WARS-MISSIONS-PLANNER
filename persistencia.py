from listar_misiones import misiones_planificadas
from recursos import recursos_alianza
from misiones import misiones_alianza
from eliminar_mision_agenda import papelera_reciclaje
import json
import os

# Importamos cada misión (objeto) por separado
from misiones import reconocimiento_tattoine,rescate_pricesa_leia,ataque_estrella_muerte,batalla_hoth,rescate_ciudad_nube,rescate_palacio_jabba,ataque_segunda_estrella_muerte,mision_endor_terrestre,confrontacion_final

# OBTENER LA RUTA BASE DEL PROYECTO
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
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
}


def guardar_estado():
    
    # 1
    agendas_de_recursos = []
    for recurso in recursos_alianza: # Recorremos todos los recursos de la alianza (objetos de POO)
        agendas_de_recursos.append(recurso.diccionario()) # Las convertimos en un diccionario y las agregamos a [agendas_de_recursos]
    
    # 2
    misiones_agendadas = [] 
    for mision in misiones_planificadas: # Recorremos las misiones que agendamos en la semana (lista de diccionarios)
        misiones_agendadas.append(mision) # añadimos cada misión (diccionario) a [misiones_agendadas]
    
    # 3
    misiones_restantes = []
    for m in misiones_alianza: # Recorremos las misiones que nos quedan en las misiones de la alianza (objetos POO)
        misiones_restantes.append(m.diccionario()) # Las convertimos en un diccionario y las añadimos a [misiones_restantes]
    
    # 4
    papelera_diccionario = []
    for mision in papelera_reciclaje: # Recorremos las misiones que están en la papelera (objetos POO)
        papelera_diccionario.append(mision.diccionario()) # Las convertimmos en un diccionario y las añadimos a [papelera_diccionario]
    
    
    # Guardar todos los archivos como json en la carpeta Save Data
    with open(os.path.join(RUTA_SAVED_DATA,"agendas_recursos.json"), "w", encoding="utf-8") as archivo:
        json.dump(agendas_de_recursos, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"misiones_agendadas.json"), "w", encoding="utf-8") as archivo:
        json.dump(misiones_agendadas, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"misiones_restantes.json"), "w", encoding="utf-8") as archivo:
        json.dump(misiones_restantes, archivo, indent=4, ensure_ascii=False)
    
    with open(os.path.join(RUTA_SAVED_DATA,"papelera.json"), "w", encoding="utf-8") as archivo:
        json.dump(papelera_diccionario, archivo, indent=4, ensure_ascii=False)


def cargar_estado():
    
    # Verificar si existen los archivos Json antes de cargarlos 
    archivos = [
        os.path.join(RUTA_SAVED_DATA,"agendas_recursos.json"),
        os.path.join(RUTA_SAVED_DATA,"misiones_agendadas.json"),
        os.path.join(RUTA_SAVED_DATA,"misiones_restantes.json"),
        os.path.join(RUTA_SAVED_DATA,"papelera.json")]
    
    # Si algún archivo json no existe entonces es la primera vez que se abre la aplicación o el usuario los borró :)
    if not all(os.path.exists(archivo) for archivo in archivos):
        return False # No hay estado que cargar
    
    
    try:
        # 1. Cargar las agendas de los recursos
        with open(os.path.join(RUTA_SAVED_DATA,"agendas_recursos.json"), "r", encoding="utf-8") as archivo:
            agendas_recursos_cargadas = json.load(archivo)

        for indice, agenda_recurso in enumerate(agendas_recursos_cargadas): # Separamos 
            recursos_alianza[indice].agenda = agenda_recurso["agenda"]

        # 2. Cargar las misiones agendadas
        with open(os.path.join(RUTA_SAVED_DATA,"misiones_agendadas.json"), "r", encoding="utf-8") as archivo:
            misiones_agendadas_cargadas = json.load(archivo)
            misiones_planificadas.clear() # Limpiamos las misiones planificadas (viejas)
            misiones_planificadas.extend(misiones_agendadas_cargadas) # Añadimos las misiones que agendamos (diccionarios) a [misiones_planificadas]

        # 3. Cargar las misiones restantes
        misiones_alianza.clear() # Borramos todas las misiones de la alianza

        with open(os.path.join(RUTA_SAVED_DATA,"misiones_restantes.json"), "r", encoding="utf-8") as archivo:
            mision_diccionario = json.load(archivo)

        for datos_mision in mision_diccionario: # Misión diccionario es la lista que contiene las misiones (dicionario) que nos quedan [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            misiones_alianza.append(mision_objeto)

        # 4. Cargar la papelera de reciclaje
        papelera_reciclaje.clear()
        with open(os.path.join(RUTA_SAVED_DATA,"papelera.json"), "r", encoding="utf-8") as archivo:
            papelera_diccionario = json.load(archivo) 

        for datos_mision in papelera_diccionario: # Papelera diccionario es la lista que contiene las misiones (dicionario) que fueron agendadas y eliminadas [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            papelera_reciclaje.append(mision_objeto)
        
        return True
    
    except Exception as e:
        print(f"❌ Error al cargar el estado: \n▶ {e}")
        return False




