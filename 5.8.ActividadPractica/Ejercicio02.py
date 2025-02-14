import math
# Actividad: ¡Funciones!

# 1. Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
# 🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura

# 2. Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
# Calcula el área de un círculo de 5 de radio
# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. 
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.
def area_circulo(radio):
    return math.pi * radio ** 2

# 3. Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
    # Si el primer número es mayor que el segundo, debe devolver 1.
    # Si el primer número es menor que el segundo, debe devolver -1.
    # Si ambos números son iguales, debe devolver un 0.
    # Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

# 4. Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:
# 🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
# Comprueba el punto intermedio entre -12 y 24
def intermedio(num1, num2):
    return (num1 + num2) / 2

# 5. Realiza una función llamada recortar() que reciba tres parámetros. 
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
    # Devolver el límite inferior si el número es menor que éste
    # Devolver el límite superior si el número es mayor que éste. 
    # Devolver el número sin cambios si no se supera ningún límite.
    # Comprueba el resultado de recortar 15 entre los límites 0 y 10
def recortar(numero, limite_inferior, limite_superior):
    return max(limite_inferior, min(numero, limite_superior))
 
def main():
    # Area del rectangulo
    base = 15
    altura = 10
    print(f"El área del rectángulo con base {base} y altura {altura} es: {area_rectangulo(base, altura)}")

    # Area del circulo
    radio = 5
    print(f"El área del círculo con radio {radio} es: {area_circulo(radio)}")

    # Relacion
    print(f"Relación entre 5 y 10: {relacion(5, 10)}")
    print(f"Relación entre 10 y 5: {relacion(10, 5)}")
    print(f"Relación entre 5 y 5: {relacion(5, 5)}")

    # Intermedio
    print(f"El punto intermedio entre -12 y 24 es: {intermedio(-12, 24)}")

    # Recortar
    print(f"El resultado de recortar 15 entre los límites 0 y 10 es: {recortar(15, 0, 10)}")
main()