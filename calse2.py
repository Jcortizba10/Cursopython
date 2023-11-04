"""
Solicitar de 5 estudiantes el nombre
y pedir 3 materias mate, lit, quimica
sacar el promedio,
sacar el promedio mayor y menor
notas de 0 a 10
"""
nombres_estudiantes = []  # Guardar en una list
promedio = []

# Pedir informacion de 5 estudiantes
for est in range(5):
    nombre_estudiante = input(f"Ingrese el nombre del estudiante {est + 1}: ")
    nombres_estudiantes.append(nombre_estudiante)  # Agregar el nombre a la lista
    
# Pedir las calificaciones para las 3 materias
    calificacion_matematicas = float(input(f"Ingrese la calificación de matemáticas para {nombre_estudiante}: "))
    calificacion_literatura = float(input(f"Ingrese la calificación de literatura para {nombre_estudiante}: "))
    calificacion_quimica = float(input(f"Ingrese la calificación de química para {nombre_estudiante}: "))
    
# Calcular el promedio para el estudiante
    promedio_estudiante = (calificacion_matematicas + calificacion_literatura + calificacion_quimica) / 3
    promedio.append(promedio_estudiante)
    
# Encontrar el promedio máximo y mínimo
promedio_maximo = max(promedio)
promedio_minimo = min(promedio)

# Imprimir resultados
print("Resultados:")
for est in range(5):
    print(f"Estudiante: {nombres_estudiantes[est]}, Promedio: {promedio[est]:.2f}")

print(f'El promedio más alto es: {promedio_maximo:.2f}')
print(f'El promedio más bajo es: {promedio_minimo:.2f}')
