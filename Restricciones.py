# Importación de la limpieza de la terminal
import os
import time
import sys
def limpiar_terminal():
    os.system('cls')

""" Reglas 📋 del Dominio de STAR WARS 🌌 """
restricciones = {
    # Co-requisitos: {recurso_principal : recurso_necesario}
    "co_requisitos" : {
    "A005":"A006", # R2D2 Necesita a C-3PO [SIEMPRE ANDAN JUNTOS]
    "A006":"A005", # C-3PO Necesita a R2D2 (Viceversa) [SIEMPRE ANDAN JUNTOS]
    "A008":"A012", # X-Wing Necesita un Traje de Piloto [TODA NAVE NECESITA EL EQUIPO CORRECTO PARA PILOTARLA]
    "A012":"A008", # Traje de Piloto Necesita un X-Wing (Viceversa) [EL TRAJE SOLO LO USAS CUANDO VAS A VOLAR]
    "A010":"A000", # Sable de luz necesita a Luke Skywalker [LUKE NECESITA SU SABLE PARA PELEAR]
    "A000":"A010", # Luke Skywalker necesita a Sable de luz (Viceversa) [EL SABLE REQUIERE UN PORTADOR]
    "A002":"A011", # Han solo necesita su Bláster [HAN SOLO NUNCA DEJA SU BLÁSTER ATRÁS]
    "A011":"A002", # Bláster necesita a Han Solo [CUALQUIER BLÁSTER NECESITA UN PORTADOR]
    },
    
    # Exclusiones : (recurso1,recurso2)
    "exclusiones":[
        ("A000","I001"), # Luke y Vader no pueden estar juntos
        ("A007","I003") # Halcón Milenario no puede estar con TIE Fighters
    ]
}


# co_requisitos
# {'A005': 'A006', 'A006': 'A005', 'A008': 'A012', 'A012': 'A008', 'A010': 'A000', 'A000': 'A010'}
def validar_co_requisitos(recursos_seleccionados, correquisito = restricciones["co_requisitos"]):
    for recurso in recursos_seleccionados: # Recorremos cada recurso seleccionado
        if recurso in correquisito: # ¿Este recurso tiene un correquisito?
            recurso_necesario = correquisito[recurso]
            if recurso_necesario not in recursos_seleccionados: # ¿El recurso necesario está en la selección?
                limpiar_terminal()
                print("==================================================================")
                print(f"Error ⚠️  , {recurso} necesita a {recurso_necesario}\nTus recursos seleccionados no cumplen la regla de co-requisito ❌")
                return False
    # Si llegó hasta aquí no hubo ningún problema
    limpiar_terminal()
    print("===============================================================")
    print("Tus recuros seleccionados cumplen la regla de co-requisito ✅")
    return True

# [('A000', 'I001'), ('A007', 'I003')]
def validar_exclusiones(recursos_seleccionados, exclusion = restricciones["exclusiones"]):
    for recurso1,recurso2 in exclusion: # Tomamos los valores de cada tupla de las exclusiones
        if recurso1 in recursos_seleccionados and recurso2 in recursos_seleccionados: # Si los recursos conflictivos están en la selección informamos el error
                    print(f"\n⚠️  Error: {recurso1} y {recurso2} no pueden estar en la misma misión")
                    print("Tus recursos seleccionados NO cumplen la regla de exclusión mutua ❌")
                    return False
    print("Tus recursos seleccionados cumplen la regla exclusión mutua ✅")
    return True