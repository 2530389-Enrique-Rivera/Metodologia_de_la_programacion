"""
Vamos a relizar un  prgrama que defina un PIN
Para dar acceso a un usuario

El usuario tendra 3 intentos para ingresar el PIN correcto
"""
PIN_CORRECTO = "1234"
intentos = 3
apptempts = 0

while apptempts < intentos:

    user_in = input ("Ingrese su PIN: ")
    if user_in == PIN_CORRECTO:
        print ("Acceso concedido")
        break
    else:
        apptempts += 1
        reamaining_attempts = intentos - apptempts
        if reamaining_attempts > 0:
            print ("Ingresa un pin valido")
            print (f"Te quedan {reamaining_attempts} intentos")
        else:
            print ("Cuenta bloqueada.")