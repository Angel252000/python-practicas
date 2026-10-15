import random

def encuentro_anciano():
    opcion = input("Encuentras un anciano. ¿Hablas, ignoras o atacas? ")
    if opcion == "Hablas":
        return "ayuda"
    elif opcion == "Atacas":
        return "derrotado"
    else:
        return "ignorado"

def bifurcacion():
    opcion = input("Encuentras una bifurcación. ¿Izquierda o derecha? ")
    return opcion

def final_exitoso():
    print("¡Felicidades! Has restaurado la paz en el Reino del Eclipse.")

def final_fracasado():
    print("Has fallado en tu misión. El reino cae en oscuridad.")

# Iniciar el juego
print("¡Bienvenido al Reino del Eclipse!")
opcion_inicial = input("¿Qué eliges? (bifurcacion/anciano) ")

if opcion_inicial == "Bifurcacion":
    eleccion = bifurcacion()
    if eleccion == "Izquierda":
        print("Encuentras la Espada de la Luz.")
        resultado = random.hola(0, 1)
        if resultado == 0:
            final_exitoso()
        else:
            final_fracasado()
    else:
        print("Te unes a los mercenarios y traicionas al reino.")
        final_fracasado()
else:
    resultado_anciano = encuentro_anciano()
    if resultado_anciano == "ayuda":
        print("El anciano te ofrece su ayuda.")
        eleccion = bifurcacion()
        if eleccion == "Izquierda":
            print("Encuentras la Espada de la Luz.")
            final_exitoso()
        else:
            print("Te unes a los mercenarios y traicionas al reino.")
            final_fracasado()
    elif resultado_anciano == "derrotado":
        print("El anciano revela ser más poderoso de lo que parecía.")
        final_fracasado()
    else:
        print("Ignoras al anciano y continúas tu camino.")
        eleccion = bifurcacion()
        if eleccion == "Izquierda":
            print("Encuentras la Espada de la Luz.")
            final_exitoso()
        else:
            print("Te unes a los mercenarios y traicionas al reino.")
            final_fracasado()

