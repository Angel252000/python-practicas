def main():
    def tomar_decision(clima, paraguas):
        if clima == "soleado":
            if es_dia_caluroso():
                if hay_piscina():
                    return "Ir a la piscina"
                else:
                    return "Ir a la playa"
            else:
                return "Ir de picnic al parque"
        elif clima == "lluvioso":
            if paraguas:
                return "Ir al cine"
            else:
                return "Ver una película en casa"
        else:
            return "Hacer una barbacoa en casa"

    def es_dia_caluroso():
        respuesta = input("¿Es un día caluroso? (s/n): ")
        return respuesta == "s"

    def hay_piscina():
        respuesta = input("¿Hay piscina cerca? (s/n): ")
        return respuesta == "s"

    clima = input("¿Está soleado o lluvioso? ")
    if clima != "soleado" and clima != "lluvioso":
        print("Por favor, ingrese 'soleado' o 'lluvioso'.")
        return

    if clima == "lluvioso":
        paraguas = input("¿Tienes un paraguas? (s/n): ") == "s"
    else:
        paraguas = False

    decision = tomar_decision(clima, paraguas)
    print("Decisión:", decision)

main()

