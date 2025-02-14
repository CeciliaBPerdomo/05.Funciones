def ingresar_notas(): 
    notas = []
    while True:
        entrada = input('Ingrese una nota (Escriba fin para terminar): ')
        if entrada == 'fin':
            break
        elif entrada == '': 
            print('No se ingreso ninguna nota')
            continue
        if entrada.isdecimal(): 
            nota = int(entrada)
            if nota < 0 or nota > 10: 
                print('La nota debe estar entre 0 y 10')
                continue
            notas.append(nota)
        else:
            print('La nota debe ser un numero')
    return notas

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mostrar_datos(promedio, notas):
    print("Las notas son las siguientes: ", notas)
    print("El promedio es: ", promedio)

def main():
    notas = ingresar_notas()
    promedio = calcular_promedio(notas)
    mostrar_datos(promedio, notas)

main()