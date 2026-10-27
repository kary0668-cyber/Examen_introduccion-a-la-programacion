"""
-El programa inicia con un saldo inicial de $1000.
-Mostrar un menú con las siguientes opciones:
a.Consultar saldo
b.Depositar dinero
c.Retirar dinero
d.Salir
-El menú debe repetirse hasta que el usuario seleccione "Salir" o 0 (Cero).
-Utilizar funciones separadas para cada operación (ConsultarSaldo(), Depositar(), Retirar()).
-Validar lo siguiente:
-Que el monto a depositar o retirar sea mayor que cero.
-Que no se pueda retirar más dinero del disponible.
-Utilizar condicionales dentro de las funciones para realizar validaciones.
-Mostrar mensajes claros para el usuario en cada operación.
"""

saldo = 1000

def Consultar_saldo():
    print("Tu saldo actual es:", saldo)
    
def depositar():
    global saldo
    monto = float(input("Cuanto dinero desea depositar: "))
    if monto > 0:
        saldo = saldo + monto
        print("deposito exitoso")
        print("Tu nuevo saldo es:", saldo)
    else:
        print("El monto debe ser mayor que cero")
    
def retirar():
    global saldo
    monto = float(input("Cuanto deseas retirar: "))
    if monto <= 0:
        print("El monto dede ser mayor que cero")
    elif monto > saldo:
        print("Saldo insuficiente")
    else:
        saldo = saldo - monto
        print("Retiro exitoso")
        print("Tu saldo es:", saldo)
        
while True:
    print("\n--- CAJERO AUTOMATICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("0. Salir")
    
    opcion = input("Seleccionar la opcion: ")
    
    if opcion == "1":
        Consultar_saldo()
    elif opcion == "2":
        depositar()
    elif opcion == "3":
        retirar()
    elif opcion == "0":
        print("Gracias por utilizar el cajero")
        break
    else:
        print(" Opcion no valida")
