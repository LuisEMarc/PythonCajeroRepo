'''
    Cajero made by
    Luis Enrique Marcos
'''

from datetime import datetime

saldo = 1000.00

def setDate():
    now = datetime.now()
    date = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}:{now.second}"

    return date


def opexitosa(saldo):
    while True:
        print("¿Qué desea hacer?")
        print("\n============================\n\n¿Qué desea hacer?\n[1] Volver al menú\n[2] "
              "Finalizar\n\n============================")
        opc2 = int(input("Introduzca opción: "))

        if opc2 == 1:

            menu(saldo)

        elif opc2 == 2:

            exit()


def menu(saldo):

    while True:

        print(
            f"¡Bienvenido! {user}\n============================\n\n[1] Consultar saldo\n[2] Retirar saldo\n[3] Histórico "
            "de Movimientos\n[0] Salir\n\n============================\n")
        opc = int(input("Seleccione opción: "))

        if opc == 1:

            print(" ##### Consultar saldo #####\n")
            print(f"Su saldo actual es de: ${saldo}")
            tupla_movimiento = [
                ("Consulta de saldo", setDate(), f"Saldo: {saldo}", f"Saldo Inicial: {saldo}")
            ]
            historico.append(tupla_movimiento)
            print("¿Qué otra operación desea realizar?\n")
            opexitosa(saldo)

        elif opc == 2:

            print(" ##### Retirar saldo #####\n")
            if saldo <= (0):
                print("¡Ups! Parece que no dispone de fondos suficientes para realizar un retiro")
                opexitosa(saldo)

            else:

                while True:

                    retirasaldo = float(input("Indique la cantidad a retirar: "))

                    if retirasaldo > saldo:

                        print("Lo siento, no dispones de saldo suficiente")

                    elif retirasaldo <= saldo:

                        print("\nRetirando saldo, espere.")
                        saldo = saldo - retirasaldo
                        tupla_movimiento = [
                            ("Retiro de saldo", setDate(), f"Saldo: {saldo}", f"Saldo anterior: {saldo + retirasaldo}")
                        ]
                        historico.append(tupla_movimiento)
                        print("Saldo retirado\n")
                        opexitosa(saldo)

        elif opc == 3:

            print(" ##### Histórico de Movimientos #####\n")
            print(f"{historico}")
            opexitosa(saldo)

        elif opc == 0:

            exit()


def comprobarpin():

    intentos = 3

    while intentos != 0:

        pin = int(input("Ingrese pin: "))

        if pin != 1235:

            intentos -= 1
            print(f"PIN incorrecto: Intente nuevamente...\n\nIntentos restantes: {intentos}")

        else:

            menu(saldo)


user = str(input("Ingrese su nombre: "))
historico = []

try:

    comprobarpin()

except ValueError:

    print("Introdujo un caracter no válido, favor de ingresar SOLO números válidos")
