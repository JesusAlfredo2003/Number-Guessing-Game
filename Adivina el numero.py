import random

def adivina_el_numero():
    print("🎯 Bienvenido al juego 'Adivina el número'")
    print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

    # Generar número aleatorio
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            # Solicitar número al usuario
            entrada = input("Introduce tu número (o 'e' para salir): ").strip()

            # Opción para salir
            if entrada.lower() == 'e':
                print("Has salido del juego. El número era:", numero_secreto)
                break

            # Validar que sea un número entero
            numero = int(entrada)

            if numero < 1 or numero > 100:
                print("⚠️ Por favor, introduce un número entre 1 y 100.")
                continue

            intentos += 1

            # Comprobar si acertó
            if numero == numero_secreto:
                print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
            elif numero < numero_secreto:
                print("📈 El número secreto es mayor.")
            else:
                print("📉 El número secreto es menor.")

        except ValueError:
            print("⚠️ Entrada inválida. Debes escribir un número entero o 'e' para salir.")

# Ejecutar el juego
if __name__ == "__main__":
    adivina_el_numero()
