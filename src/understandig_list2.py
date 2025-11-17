"""
    slicing a list
"""

players =['charles', 'martina', 'michael', 'florence', 'eli']
print("lista original:", players)

print("slice de lista original:", players[0:3])
print("slice de lista original:", players[1:4])
print("slice de lista original:", players[:4])
print("slice de lista original:", players[2:])
print("slice de lista original:", players[-3:])
print("slice de lista original:", players[5:2])
print("slice de lista original:", players[-3:-1])

"""
Slicing en un for
"""
players =['charles', 'martina', 'michael', 'florence', 'eli']
print("los primeros 3 jugadores:", players)
for players in players [0:3]:
    print(players.title())

    """
    copiando una lista
    """
    my_foood =["pizza", ]
    my_foood = my_foood 
    my_foood1 = my_foood[:]
    my_foood2 = my_foood.copy()
    my_foood3 = list(my_foood)