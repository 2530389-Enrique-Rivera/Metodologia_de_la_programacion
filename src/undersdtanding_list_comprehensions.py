"""
  squares=[]
  for value in range (0,11)
  squares = value**2
  squares.append(squares)
  print(squares)
"""

""""
una list comprehension combien el ciclo for 
y la crecion de nuevos elemntos en una sola 
linea y automaticamente agrega cada nuevo element
a la lista, es decir, sin utilizar el metodo append
"""

squares = [value**2 for value in range(0,11)]
print(squares)

#Para generar una lista de numeros pares entre el 0 y el 100
squares_range = [value for value in range(0,101,2)]
print(squares_range)

evens_if = [value for value in range(0,101) if value % 2 == 0]
print(evens_if)