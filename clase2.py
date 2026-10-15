def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    print("¡Hola! Soy tu amiguito conversor de temperatura.")
    print("¿Sabías que puedo decirte cuánto hace en Fahrenheit si me dices en Celsius? ¡Te puedo ayudar!")
   
    print("Dime una temperatura en Celsius y te diré cuánto es en Fahrenheit.")
    celsius = float(input("Temperatura en Celsius: "))

    fahrenheit = celsius_a_fahrenheit(celsius)

    print(f"Wow, ¡eso es genial! {celsius} grados Celsius equivalen a aproximadamente {fahrenheit} grados Fahrenheit.")

main()  
