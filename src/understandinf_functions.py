### Funciones
#Las funciones son bloques de codigo para realizar
#una tarea wen específico

#cuando queremos realkixar la tarea que se ha definido
#en la función, tenemos que "llamar" a la función
#Fuincion que realiza la acciones

"""
    Sintaxis para definir una función
    def nombre_de_la_funcion():
    acciones

    Ejemplo:Vamos a definir una función que 
    salude a cristofer

"""

def saludar_a_cristofer():
    """
       Funcion para saludar a una persona
    """
    print("Hola cristofer")

saludar_a_cristofer()  #Llamada a la función    

# ==================================================

def create_Full_name(first_name, middle_name, last_name):
    full_name = f"{first_name.strip()} {middle_name.strip()} {last_name.strip()}".title()
    return full_name
input_first_name = input("Dame tu primrer nombre: ")
input_middle_name = input("Damw tu segundo nombre: ")
input_last_name = input("Dame tu apellido: ")

generated_full_name=create_Full_name(first_name=input_first_name, middle_name=input_middle_name, last_name=input_last_name)
print("Tu nombre completo es:", generated_full_name)
