# Actividad: Función año bisiesto
# Realizar una función llamada año_bisiesto:
        # Recibirá un año por parámetro
        # Imprimirá “El año año es bisiesto” si el año es bisiesto
        # Imprimirá “El año año no es bisiesto” si el año no es bisiesto
        # Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

# Información a tener en cuenta:
# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
# Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

def solicitar_year(): 
     while True:
        year = int(input("Ingrese un año: "))
        return year 

def year_bisieto(year): 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print( f"El año {year} es bisiesto.")  
    else:
        print( f"El año {year} no es bisiesto.")

def main():
    year = solicitar_year()
    year_bisieto(year)

main()