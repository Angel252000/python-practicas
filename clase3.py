distancia_hotel_a_catedral = 9
distancia_catedral_a_fuente = 2
distancia_fuente_a_vaticano = 3.5
distancia_vaticano_a_sendero = 7.2

distancia_hotel_a_catedral_m = distancia_hotel_a_catedral * (600 / 5)
distancia_catedral_a_fuente_m = distancia_catedral_a_fuente * (600 / 5)
distancia_fuente_a_vaticano_m = distancia_fuente_a_vaticano * (600 / 5)
distancia_vaticano_a_sendero_m = distancia_vaticano_a_sendero * (600 / 5)

print("Distancia del hotel a la catedral:", distancia_hotel_a_catedral_m, "m.")
print("Distancia de la catedral a la fuente:", distancia_catedral_a_fuente_m, "m.")
print("Distancia de la fuente al Vaticano:", distancia_fuente_a_vaticano_m, "m.")
print("Distancia del Vaticano al sendero:", distancia_vaticano_a_sendero_m, "m.")

distancia_total_m = distancia_hotel_a_catedral_m + distancia_catedral_a_fuente_m + distancia_fuente_a_vaticano_m + distancia_vaticano_a_sendero_m
tiempo_total_min = distancia_total_m * (8 / 600)
print("Tiempo total caminando en el día:", tiempo_total_min, "min.")
