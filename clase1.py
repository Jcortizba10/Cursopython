""""
Funcion para validar una IP
Entradas : cadena de texto
Salida : Validar un dato booleano 
1. solicitar ip 
2. separar por octetos
3. verificar si lo octetos son correctos
4. Retornar si es correcto o no.
ip = input("Ingrese su IP : ")
if len(ip)!= 4:
print(ip.split(sep="."))
"""
def is_valid_ip(ip):
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if not (0 <= int(octet) <= 255):
            return False
    return True

while True:
    user_input = input("Ingrese una dirección IP: ")

    if is_valid_ip(user_input):
        confirm = input(f"Ha ingresado la dirección IP: {user_input}. Es correcta ")
        break

    else:
        print("La entrada no es una dirección IP válida. Inténtalo de nuevo.")
