#while
"""
    El while es un ciclo controlado/comandado
    por condicion
        la estructura basica del while es:
        while condicion:
            action 

"""
#while infinito
"""
    Programa sin el usario escribe un numero
    entre 25 y 50 entonces estar en el rango
    y salirme del while
"""
while True:
    try:
        numero=int(input("Escribe un numero: "))
  
        if numero <= 50 and numero >=25:
            print("El numero", numero, "esta en el rango")
            break
        else:
            print("El numero", numero, "no esta en el rango, intenta de nuevo")
    except ValueError:
        print("Eso no es un numero, intenta de nuevo")
