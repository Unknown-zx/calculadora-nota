import time

notas = []

continuar = True

print()
texto = "Iniciando menú..."
for letra in texto:
    print(letra, end=(""), flush=True)
    time.sleep(0.15)

time.sleep(3)
print()

def ingresar_nota():
    print()
    time.sleep(1.40)
    nota = float(input("Ingrese la nota (0-100): "))
    if nota < 0 or nota > 100:
        print()
        print("Nota fuera del rango. Debe estar entre 0 y 100.")
    else:
        print()
        print(f"¡Nota ingresada!: {nota}")
        notas.append(nota)

def calcular_promedio():
    if len(notas) == 0:
        return None
    else:
        return sum(notas) / len(notas)

def notas_extremas():
    if len(notas) < 2:
        print()
        print("Se necesitan al menos 2 notas para determinar las extremas.")
    else:
        nota_maxima = max(notas)
        nota_minima = min(notas)
        print()
        print(f"La nota más alta es: {nota_maxima}")
        print()
        print(f"Mientras que la nota más baja es: {nota_minima}")

def verificar_aprobado():
    promedio = calcular_promedio()
    if promedio is None:
        print()
        print("No se han ingresado notas aún.")
    elif promedio >= 70:
        print()
        print(f"¡Felicidades!, Has aprobado con un promedio de {promedio:.2f}.")
    else:
        print()
        print(f"Lo siento, has reprobado con un promedio de {promedio:.2f}.")

def salir():
    global continuar
    continuar = False
    print()
    print("Saliendo del programa...")
    time.sleep(2)
    print()
    print("¡Hasta luego!")
    print()
    time.sleep(1.5)

while continuar:
    print()
    print("MENÚ DE OPCIONES:")
    print()
    time.sleep(1.4)
    print("1. Ingresar nota.")
    time.sleep(1.8)
    print("2. Mostrar promedio de notas.")
    time.sleep(2)
    print("3. Ver nota más alta y más baja.")
    time.sleep(2)
    print("4. Resultados.")
    time.sleep(1.7)
    print("5. Salir.")

    time.sleep(1.6)
    print()
    opcion = input("Seleccione una opción. (1-5): ")

    if opcion == "1":
        time.sleep(1.5)
        ingresar_nota()
        time.sleep(2.2)

    elif opcion == "2":
        time.sleep(1.5)
        promedio = calcular_promedio()
        if promedio is None:
            print()
            print("No se han ingresado notas aún.")
        else:
            print()
            print(f"El promedio de las notas es: {promedio:.2f}")
        time.sleep(2.2)

    elif opcion == "3":
        time.sleep(1.5)
        notas_extremas()
        time.sleep(2.2)

    elif opcion == "4":
        time.sleep(1.5)
        verificar_aprobado()
        time.sleep(2.2)

    elif opcion == "5":
        time.sleep(1.5)
        salir()
        time.sleep(2.2)

    else:
        print()
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
        time.sleep(2.2)