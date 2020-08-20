saldo = 3000

print(" .:Menu:.")
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Consultar dinero en la cuenta")
print("4. Salir, gracias por usar nuestros cajeros autmaticos")

opcion=int(input("digite una opcion para continuar:-> "))

if opcion==1:
    extra=float(input("digite cuanto dinero desea ingresar a la cuenta:-> "))
    saldo += extra
    print(f"el nuevo saldo disponible que queda en la cuenta es de {saldo}")

elif opcion==2:
    retiro=float(input("cuanto dinero desea retirar de la cuenta:-> "))
    if retiro>saldo:
        print("no posees suficiente saldo para realizar dicha operacion")
    saldo-=retiro
    print(f"el nuevo saldo disponible es de {saldo}")
elif opcion==3:
    print(f"el saldo actual es de {saldo}")

elif opcion==4:
    print("gracias por usar nuestros cajeros automaticos")
else:
    print("la opcion elegida no esta contemplada")

contador=1

while(contador==1):
    opcion = int(input("digite una opcion para continuar:-> "))

    if opcion == 1:
        extra = float(input("digite cuanto dinero desea ingresar a la cuenta:-> "))
        saldo += extra
        print(f"el nuevo saldo disponible que queda en la cuenta es de {saldo}")

    elif opcion == 2:
        retiro = float(input("cuanto dinero desea retirar de la cuenta:-> "))
        if retiro > saldo:
            print("no posees suficiente saldo para realizar dicha operacion")
        saldo -= retiro
        print(f"el nuevo saldo disponible es de {saldo}")
    elif opcion == 3:
        print(f"el saldo actual es de {saldo}")

    elif opcion == 4:
        print("gracias por usar nuestros cajeros automaticos")
    else:
        print("la opcion elegida no esta contemplada")