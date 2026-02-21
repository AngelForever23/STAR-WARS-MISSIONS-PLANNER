# Variables bandera del bando seleccionado
Alianza = False
Imperio = False


def seleccionar_alianza():
    global Alianza, Imperio
    Alianza = True
    Imperio = False


def seleccionar_imperio():
    global Alianza, Imperio
    Alianza = False
    Imperio = True


def reiniciar():
    global Alianza, Imperio
    Alianza = False
    Imperio = False


def bando_activo():
    if Alianza:
        return "Alianza"
    if Imperio:
        return "Imperio"
    return None
