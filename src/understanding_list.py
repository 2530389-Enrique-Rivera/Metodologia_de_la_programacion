#List
"""
  Las listas nos permiten almacenar inbformacion en un lugarnla 
  la cantidad de indormcaicon que tengas y sean pocos o muchos
  se recomienda usar una variable de tipo lista
  en plural en python los corcheres [] definen una lista  
  sus elementos van separados por comas ,
  las listas son elementos mutables, es decir que se pueden modificar
  """
my_list = ['trek' , 'conondale' , 'redline' , 'specialized' , 'giant']
print(my_list) 
print(my_list [0] .title())


print(my_list [4] .title())

print(my_list [-1] .title())
print(my_list [-2] .title())
print(my_list [-5] .title())

# utilizando valores de la lista
message = "Mi bicicleta favorita es una " + my_list[0].title() + "."
print(message)

message_f = "Mi bicicleta favorita es una " + my_list[3].title() + "."
print(message_f)

#agregar elementos a una lista
print("\n")
motos = ['honda' , 'yamaha' , 'suzuki']
print(motos)

"""eliminar elementos de una lista
  del elimina un elemento de una lista en una posicion especifica"""

del motos[0]
print(motos)

"""eliminar un elemto con el metodo pop
  pop remueve el ultimo elemento de una lista"""

print("\n")
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(cars)
pop_cars = cars.pop()
print(cars)

#organizar una lista permanentemente 
"""
sort(): organiza una lista de forma permanente en orden alfabetico
"""

print("\n")
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.sort()
print(cars)
print("\n")
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.sort(reverse=True) 
print(cars)