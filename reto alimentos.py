https://replit.com/@Vania-ZoeZoe1/Examen-de-prueba

# Función para evaluar los alimentos
def evaluar_alimento(grasa, azucar, sodio):
    if grasa <= 5 and azucar <= 10:
        print("El alimento es bajo en grasa y azúcar")
    if sodio <= 100:
        print("El alimento es bajo en sodio")
    else:
        print("oh no, este alimento cuenta con demasiadas advertencias nutricionales")


grasa = float(input("Ingrese el contenido de grasa (g por porción): "))
azucar = float(input("Ingrese el contenido de azúcar (g por porción): "))
sodio = float(input("Ingrese el contenido de sodio (mg por porción): "))

resultado = evaluar_alimento(grasa, azucar, sodio)

print(resultado)
