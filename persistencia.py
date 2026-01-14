from listar_misiones import misiones_planificadas
from Recursos_Alianza import recursos_alianza
from Misiones_Alianza import misiones_alianza
from Eliminar_Mision import papelera_reciclaje
import json
import os

# Importamos cada misión (objeto) por separado
from Misiones_Alianza import recognition_mission_tattol,rescue_princess_leia,battle_hoth,attack_death_star

# Variable constante para "mapear" las misiones (objetos) según sus Ids
TODAS_LAS_MISIONES = {
    "M001": recognition_mission_tattol,
    "M002": rescue_princess_leia,
    "M003": battle_hoth,
    "M004": attack_death_star
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
    
    
    # 1.1 Guardamos las agendas de los recursos como json
    with open("agendas_recursos.json", "w", encoding="uft-8") as archivo:
        json.dump(agendas_de_recursos, archivo, indent=4, ensure_ascii=False)
    
    # 2.2 Guardamos las misiones agendadas como json
    with open("misiones_agendadas.json", "w", encoding="uft-8") as archivo:
        json.dump(misiones_agendadas, archivo, indent=4, ensure_ascii=False)
    
    # 3.3 Guardamos las misiones restantes de la alianza como json
    with open("misiones_restantes.json", "w", encoding="uft-8") as archivo:
        json.dump(misiones_restantes, archivo, indent=4, ensure_ascii=False)
    
    # 4.4 Guardamos la papelera reutilizble de las misiones como json
    with open("papelera.json", "w", encoding="uft-8") as archivo:
        json.dump(papelera_diccionario, archivo, indent=4, ensure_ascii=False)


def cargar_estado():
    
        # Verificar si existen los archivos Json antes de cargarlos 
    archivos = ["agendas_recursos.json","misiones_agendadas.json","misiones_restantes.json","papelera.json"]
    
    # Si algún archivo no existe entonces es la primera vez que se abre la aplicación
    if not all(os.path.exists(archivo) for archivo in archivos):
        return False # No hay estado que cargar
    
    
    try:
        # 1. Cargar las agendas de los recursos
        with open("agendas_recursos.json", "r") as archivo:
            agendas_recursos_cargadas = json.load(archivo)

        for indice, agenda_recurso in enumerate(agendas_recursos_cargadas): # Separamos 
            recursos_alianza[indice].agenda = agenda_recurso["agenda"]

        # 2. Cargar las misiones agendadas
        with open("misiones_agendadas.json", "r") as archivo:
            misiones_agendadas_cargadas = json.load(archivo)
            misiones_planificadas.clear() # Limpiamos las misiones planificadas (viejas)
            misiones_planificadas.extend(misiones_agendadas_cargadas) # Añadimos las misiones que agendamos (diccionarios) a [misiones_planificadas]

        # 3. Cargar las misiones restantes
        misiones_alianza.clear() # Borramos todas las misiones de la alianza

        with open("misiones_restantes.json", "r") as archivo:
            mision_diccionario = json.load(archivo)

        for datos_mision in mision_diccionario: # Misión diccionario es la lista que contiene las misiones (dicionario) que nos quedan [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            misiones_alianza.append(mision_objeto)

        # 4. Cargar la papelera de reciclaje
        with open("papelera.json", "r") as archivo:
            papelera_diccionario = json.load(archivo) 

        for datos_mision in papelera_diccionario: # Papelera diccionario es la lista que contiene las misiones (dicionario) que fueron agendadas y eliminadas [{},{}]
            mision_id = datos_mision["id"]
            mision_objeto = TODAS_LAS_MISIONES[mision_id]
            papelera_reciclaje.append(mision_objeto)
        
        return True
    
    except Exception as e:
        print(f"Error al cargar el estado: {e}")
        return False




