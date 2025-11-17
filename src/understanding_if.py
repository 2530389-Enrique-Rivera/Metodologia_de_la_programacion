cars = ["audi" , "bmw" , "chevrolet" , "corvette" , "tesla"]


for car in cars:
    if car == "bmw" or car=="tesla":
        print(car.upper())
    else:
        print(car.title())

    
    #condicionales: El condicional es el corazon de un if


# condicional True o false
car ="bmw"
print(car == "bmw") #True

car_2 ="Audi"
print(car_2 == "audi") #False

car_2 ="Audi"
print(car_2.lower() == "audi") #True

# conddicional != para desigualdad
requested_topping = "mushrooms"
if requested_topping != "anchovies":  #True
    print("Hold the anchovies!")

   
 #comparaciones numericas
age = 18
print(age == 18) #True

answer = 17
if  answer != 42: #True
    print("That is not the correct answer. Please try again!")

    age = 19
    print(age < 21) #True
    print(age <= 21) #True
    print(age > 21) #False
    print(age >= 21) #False

#Multiples condiciones
age_0 = 22
age_1 = 18  

print("Multiple Conditions:")
print("Operacion or - psint (0)")
print(age_0 >= 21 or age_1 >= 21) #True
print(age_0 >= 23 or age_1 >= 21) #False

age_0 = 22
age_1 = 18  
print("Multiple Conditions:")
print("Operacion and - psint (0)")
print(age_0 >= 21 and age_1 >= 21) #False
print(age_0 >= 21 and age_1 >= 18) #True

#Verificar si un elemento esta en una lista
requested_toppings = ["mushrooms" , "onions" , "pineapple"]
print("mushrooms" in requested_toppings) #True
print("pepperoni" in requested_toppings) #False 

#Verificar si un elemento no esta en una lista
banned_users = ["gabriel" , "Max" , "Andrik" , "quevedo" , "chris" , "angel"]
user = "pedro"
print(user not in banned_users) #True

#variables de tipos booleanas

game_active = True
can_edit = False


"""
    if statement

    if condition:
      do something

    if condition 
        do something (true)
    else:
        do something (false)    

"""

#preguntar la edad del usario y decirle
#si tiene la edad para votar
#imput("")

age = input("Please enter your age: ")
print(f"tu edad es: {age}")

if int(age) >= 18:
    print("tienes la edad para votar")
else:
    print("no tienes la edad para votar")
