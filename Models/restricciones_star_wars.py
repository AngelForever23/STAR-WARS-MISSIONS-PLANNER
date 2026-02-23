from Functions.utilidades import limpiar_terminal

""" Reglas 🔧 del Dominio de STAR WARS 🌌 """

restricciones_alianza = {
    # Co-requisitos: {recurso_principal : recurso_necesario}
    "co_requisitos" : {
    "A000":"A011",  # Luke Skywalker ↔️ Sable de luz [LUKE NECESITA SU SABLE PARA PELEAR]
    "A011":"A000",
    "A003":"A012",  # Han ➡️ Bláster [HAN SOLO NUNCA DEJA SU BLÁSTER ATRÁS]
    "A005":"A008",  # Lando ➡️ Halcón Milenario [TANTO LANDO COMO HAN SOLO MANEJAN EL HALCÓN MILENARIO]
    "A006":"A007",  # R2D2 ↔️ C-3PO [SIEMPRE ANDAN JUNTOS]
    "A007":"A006",
    "A009":"A013",  # X-Wing ➡️ Traje de Piloto [TODA NAVE NECESITA EL EQUIPO CORRECTO PARA PILOTARLA]
    "A010":"A013",  # A-Wing ➡️ Traje de Piloto [TODA NAVE NECESITA EL EQUIPO CORRECTO PARA PILOTARLA]
    "A016":"A002",  # Equipo de Camuflaje ➡️ Leia [LEIA (Líder en esta misión) USA ESTE TRAJE EN ENDOR]
    },
    
    # Exclusiones : (recurso1,recurso2)
    "exclusiones":[
        ("A003","A005"), # Han ❌ Lando (tensión por el Halcón, rivales de Sabacc)
        ("A015", "A014") # Detonadores ❌ Escudo Deflector (riesgo de explosión propia)
    ]
}

restricciones_imperio = {
    "co_requisitos": {
        "I000":"I015",  # Vader ↔️ sable de luz [VADER SIEMPRE LLEVA CONSIGO SU SABLE]
        "I015":"I000",
        "I008":"I001",  # Estrella de la Muerte ↔️ Tarkin [TARKIN ES EL COMANDANTE DE LA ESTRELLA DE LA MUERTE]
        "I001":"I008",
        "I009":"I003",  # Destructor Estelar ➡️ Piett [LA NAVE "DESTRUCTOR ESTELAR" NECESITA A ALMIRANTE PIETT (ESTÁ A CARGO)]
        "I007":"I011",  # Piloto de AT-AT ↔️ AT-AT [EL VEHÍCULO AT-AT REQUIERE A ALGUIEN ESPECIALIZADO QUE SEPA MANEJARLO]
        "I011":"I007",
        "I010":"I005",  # TIE Fighter ➡️ Piloto (Stormtropper)  [ESTA NAVE CAZA REQUIERE QUE UN SOLDADO (STORMTROPPER) LA DIRIJA]
        "I012":"I005",  # AT-ST ➡️ Piloto (Stormtropper) [ESTE VEHÍCULO REQUIERE QUE UN SOLDADO (STORMTROPPER) LA DIRIJA)]
        "I005":"I014",  # Stormtrooper ➡️ Bláster [CUALQUIER SOLDADO NECESITA UN ARMA]
    },
    
    "exclusiones": [
        ("I011","A012"),  # AT-AT ❌ AT-ST (Vehículos hechos para terrenos diferentes, diferencias entre tamaño y movilidad)
    ]
}


def validar_co_requisitos_alianza(recursos_seleccionados, correquisito = restricciones_alianza["co_requisitos"]):
    for recurso in recursos_seleccionados: # Recorremos cada recurso seleccionado
        if recurso in correquisito: # ¿Este recurso tiene un correquisito?
            recurso_necesario = correquisito[recurso]
            if recurso_necesario not in recursos_seleccionados: # ¿El recurso necesario está en la selección?
                limpiar_terminal()
                print("==================================================================")
                print(f"⚠️  Error: {recurso} necesita a {recurso_necesario}\nTus recursos seleccionados no cumplen la regla de co-requisito ❌")
                return False
    # Si llegó hasta aquí no hubo ningún problema
    limpiar_terminal()
    print("===============================================================")
    print("Tus recuros seleccionados cumplen la regla de co-requisito  ✅")
    return True

def validar_exclusiones_alianza(recursos_seleccionados, exclusion = restricciones_alianza["exclusiones"]):
    for recurso1,recurso2 in exclusion: # Tomamos los valores de cada tupla de las exclusiones
        if recurso1 in recursos_seleccionados and recurso2 in recursos_seleccionados: # Si los recursos conflictivos están en la selección informamos el error
                    print(f"⚠️  Error: {recurso1} y {recurso2} no pueden estar en la misma misión")
                    print("Tus recursos seleccionados NO cumplen la regla de exclusión mutua ❌")
                    return False
    print("Tus recursos seleccionados cumplen la regla exclusión mutua ✅")
    return True # Si llegó hasta aquí no hubo ningún problema




def validar_co_requisitos_imperio(recursos_seleccionados, correquisito = restricciones_imperio["co_requisitos"]):
    for recurso in recursos_seleccionados: # Recorremos cada recurso seleccionado
        if recurso in correquisito: # ¿Este recurso tiene un correquisito?
            recurso_necesario = correquisito[recurso]
            if recurso_necesario not in recursos_seleccionados: # ¿El recurso necesario está en la selección?
                limpiar_terminal()
                print("==================================================================")
                print(f"⚠️  Error: {recurso} necesita a {recurso_necesario}\nTus recursos seleccionados no cumplen la regla de co-requisito ❌")
                return False
    # Si llegó hasta aquí no hubo ningún problema
    limpiar_terminal()
    print("===============================================================")
    print("Tus recuros seleccionados cumplen la regla de co-requisito  ✅")
    return True

def validar_exclusiones_imperio(recursos_seleccionados, exclusion = restricciones_imperio["exclusiones"]):
    for recurso1,recurso2 in exclusion: # Tomamos los valores de cada tupla de las exclusiones
        if recurso1 in recursos_seleccionados and recurso2 in recursos_seleccionados: # Si los recursos conflictivos están en la selección informamos el error
                    print(f"⚠️  Error: {recurso1} y {recurso2} no pueden estar en la misma misión")
                    print("Tus recursos seleccionados NO cumplen la regla de exclusión mutua ❌")
                    return False
    print("Tus recursos seleccionados cumplen la regla exclusión mutua ✅")
    return True # Si llegó hasta aquí no hubo ningún problema

