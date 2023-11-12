import random
import string

def generar_contrasena(longitud, min_minusculas, min_mayusculas, min_numeros):
    caracteres = string.ascii_letters + string.digits

    if longitud < min_minusculas + min_mayusculas + min_numeros:
        print("Longitud mínima de contraseña no válida.")
        return None

    contrasena = (
        ''.join(random.choice(string.ascii_lowercase) for i in range(min_minusculas)) +
        ''.join(random.choice(string.ascii_uppercase) for i in range(min_mayusculas)) +
        ''.join(random.choice(string.digits) for i in range(min_numeros)) +
        ''.join(random.choice(caracteres) for i in range(longitud - min_minusculas - min_mayusculas - min_numeros))
    )

    contrasena = ''.join(random.sample(contrasena, len(contrasena)))

    return contrasena

def main():
    while True:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        min_minusculas = int(input("Ingrese el número mínimo de letras minúsculas: "))
        min_mayusculas = int(input("Ingrese el número mínimo de letras mayúsculas: "))
        min_numeros = int(input("Ingrese el número mínimo de caracteres numéricos: "))

        contrasena = generar_contrasena(longitud, min_minusculas, min_mayusculas, min_numeros)

        if contrasena:
            print(f"Su contraseña es: {contrasena}")

        continuar = input("¿Desea generar otra contraseña? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
