#tuples 
"""
    Las tuplas son listas de elemntos  que no
    cambian de tamaño. Las tuplas son INMUTABLES.

    se utulizan los () para definir una tupla    
    
    
    """
rectangle_mesaurements = (200,50) #(largo,ancho)
print(rectangle_mesaurements[0])
print(rectangle_mesaurements[1])

for masure in rectangle_mesaurements:

    print(masure)

#print(dir(rectangle_mesaurements)) #bul-in dir

#regreso tantito a las lista
cars =["bwm", "porche" , "masda"]
print (cars)

cars[0]="bmw"
cars[1]= "porshe"
cars[2]= "mazda"
print(cars)

rectangle_mesaurements = (200, 50)

rectangle_mesaurements = (300, 150)