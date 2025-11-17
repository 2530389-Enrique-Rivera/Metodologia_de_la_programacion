# Whitespaces
"""
 un whitespce es cualquier espacio en blanco que se encuentra en una cadena de texto, como espacios, tabulaciones o saltos de línea.
 Estos caracteres no son visibles, pero pueden afectar la forma en que se muestra o procesa una cadena de texto.
"""

print("Whitespaces Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")

print("Whitespaces salto de linea")
print("lenguajes de programacion:\nPython\nJava\nC++\nJavaScript")

#Eliminacion de espacios en blanco
programcion_lenguajes = "                                python                             "
print(programcion_lenguajes)
print(programcion_lenguajes.lstrip())  # Elimina espacios en blanco a la izquierda
print(programcion_lenguajes.rstrip())  # Elimina espacios en blanco a la derecha
print(programcion_lenguajes.strip())   # Elimina espacios en blanco a ambos lados

#syntax error con strings
menssaje = "una fortaleza de python es su comunidad"
print(menssaje)

#f-strings
famouse_person = "jose torres el rey del alto mado"
menssaje = f"{famouse_person} una vez dijo llego la pizza"
print(menssaje)


"""
Ejercicio: elije el nombre de una persona famosa 
elige una cita famosa de esa persona
iguala ambos strings en una variable

1)realiza la concatenacion utlizando el signo +
2)realiza la concatenacion utilizando f-strings

"""
# Concatenacion utilizando el signo +
famous_person = "albert einstein"
palabra = "la imaginacion es mas importante que el conocimiento"
message = famous_person + ' una vez dijo: "' + palabra + '"'     
print(message)

# Concatenacion utilizando f-strings
 
f_string_message = f'{famous_person} una vez dijo: "{palabra}"'
print(f_string_message)