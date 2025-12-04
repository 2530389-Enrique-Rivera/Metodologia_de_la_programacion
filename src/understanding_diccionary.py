# Diccionario
"""
Para definir un diccionario se utilizan las llaves {}

Ejemplo de un diccionario vacio
students = {"Name": "Gabriel"}

Los diccionarios son capaces de almacenar una gran cantidad de informacion
en pares de llave:valor
"""

student_0 = {"Name","Gabriel"}
student_1 = {"student","Cecya","age","18"}

# Empty Dictionary
homer_0 = {"color": "yellow", "bag": "maggie-bag", }
print(homer_0)
print(type(homer_0))

marge = {"color": "yellow", "bag": "homer-donut", "hair": "blue", "dress": "green", "mom": True}
gun_0 = {"scar": "yellow-orange", "headshot": 1.5}

## Add elements to a dictionary
homer_0["x-position"]=15
homer_0["y-position"]=25
homer_0["z-position"]=10
print(homer_0)

marge["x-position"]=15
marge["y-position"]=25
marge["z-position"]=10
print(marge)

covenant_grunt = { 
    "color": "green",
    "weapon": "plasma-gun",
    "armament": "plasma-granda"
    "health": 2,
}
covenant_elite = { 
    "color": "green",
    "weapon": "plasma-gun",
    "armament": "plasma-granda"
    "health": 7,
}
covenant_jakal = { 
    "color": "green",
    "weapon": "plasma-gun",
    "armament": "plasma-granda"
    "health": 7,
    }

#lista de diccionario
covenants =[covenant_grunt, covenant_elite, covenant_jakal]

for covenant in covenants:
    print("\n"covants)
    for key, value in covenant.items():
        print(key + value)
        print()

#lista en diccionarios
students = {
   "santiago": ["reprobado", "prepa1" "rebelde"],
   "jorge": ["aprobado", "cbtis271", "goleador"],
   "gabriel": ["aprobado", "119muerte", "crak-fornite"],
}

#Diccionario en diccionario

sensors = {
    "temperature": {
        "value": 25,
        "unit": "Celsius"
    },