
try:
    age = int(input("Please enter your age: "))
except:
 age=-1
 print("Error,ingesaste un caracter no valido")
 
if age >= 100:
        print("Tinenes mas de un siglo")
elif age >= 18 and age <100:
    print("Eres mayor de edad")
elif age >= 0 and age <19:
    print("Eres menor de edad")
else:
    print("Error pusiste un caracter no valido")

print("Holi charly")

#Actividad
"""Hacer un programa que pregunte al usuario por su edad y
determine si es un niño (0-4) para la entrada gratis,
o algiuen menor o igual a 18 para la entrada de 200 pesos,
un adulto para la entrada de 400 pesos,"""


try:
    age = int(input("Introdusca su edad: "))
except:
 age=-1
 print("Error,ingesaste un caracter no valido")
if age >= 0 and age <= 4:
    print("Tu entrada es gratis")
elif age <= 18:
    print("Tu entrada cuesta 200 pesos")
elif age > 18 and age < 65:
    print("Tu entrada cuesta 400 pesos")

guisos = ["deshebrada", "pacadillo", "asado", "salsa verde"]
if "deshebrada" in guisos:
    print("Tenemos deshebrada")
else:
    print("No tenemos asado")
if "asado" in guisos:
    print("Tenemos asado")
else:
    print("No tenemos tamales")
if "salsa verde" in guisos:
    print("Tenemos salsa verde")    
else:
    print("No tenemos salsa verde")
if "pacadillo" in guisos:
    print("Tenemos picadillo")
else:
    print("No tenemos picadillo")

#Lista vacia de guisos
guisos = []
if guisos:
    print("hay guisos ")


#Guisos disponibles
guisos_disponibles = ["deshebrada", "pacadillo", "mole"]
guisos_solicitados = ["deshebrada", "caldo de iguana"]

print("guisos a ordenar:")
for guiso in guisos_solicitados:
    if guiso in guisos_disponibles:
        print(f"Agregando {guiso} a tu orden")
    else:
        print(f"Lo siento, no tenemos {guiso} disponible")
