def clasificar_animal():
    tiene_pelo = input("¿El animal tiene pelo? (si/no): ")
    tiene_plumas = input("¿El animal tiene plumas? (si/no): ")
    tiene_columna = input("¿El animal tiene columna vertebral? (si/no): ")
    pone_huevos = input("¿El animal pone huevos? (si/no): ")
    tiene_exoesqueleto = input("¿El animal tiene exoesqueleto? (si/no): ")
    
    tiene_patas = int(input("¿Cuántas patas tiene? "))

    if tiene_patas  == 0:
        print("es un pez")
    elif tiene_patas == 2:
        print(" es una ave.")
    elif tiene_patas == 4:
        print("es un mamifero o un reptil.")
    elif tiene_patas == 6:
        print("Es un insecto.")
    else:
        print("No puedo determinar qué animal tiene esa cantidad de patas.")

    tiene_pelo = tiene_pelo == "si"
    tiene_plumas = tiene_plumas == "si"
    pone_huevos = pone_huevos == "si"
    tiene_columna = tiene_columna == "si"
    vive_en_agua = tiene_exoesqueleto == "si"

    clasificacion = ""

    if tiene_pelo and tiene_columna and not pone_huevos:
        clasificacion = "mamífero, "
    if tiene_plumas and pone_huevos:
        clasificacion = "ave, "
    if tiene_columna and not vive_en_agua and not pone_huevos:
        clasificacion = "reptil, "
    if vive_en_agua and not tiene_columna:
        clasificacion = "pez, "
    if tiene_patas and tiene_exoesqueleto == "si":
        clasificacion = "insecto, "
    
    if clasificacion:
        print("El animal es un", clasificacion.rstrip(", "))
    else:
        print("No se pudo determinar la clasificación del animal.")

def new_func():
    clasificacion = ""
    return clasificacion

clasificar_animal()
