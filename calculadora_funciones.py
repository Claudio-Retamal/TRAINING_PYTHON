a = 6
def menu ():
    seleccion = int(input('INGRESE OPERACIÓN A REALIZAR \n 1-SUMAR \n 2-RESTAR \n 3-MULTIPLICAR \n 4-DIVIDIR \n 0-SALIR \n '))
    return seleccion
def suma():
    num_1 = int(input('INGRESE NUMERO 1 '))
    num_2 = int(input('INGRESE NUMERO 2 '))
    print(num_1+num_2)
   
def resta():
    num_1 = int(input('INGRESE NUMERO 1 '))
    num_2 = int(input('INGRESE NUMERO 2 '))
    print(num_1-num_2)

def mult():
    num_1 = int(input('INGRESE NUMERO 1 '))
    num_2 = int(input('INGRESE NUMERO 2 '))
    print(num_1*num_2)

def div():
    num_1 = int(input('INGRESE NUMERO 1 '))
    num_2 = int(input('INGRESE NUMERO 2 '))
    print(num_1/num_2)

while a != 7:
    seleccion = menu()
    if (seleccion > 4 or seleccion < 0):
        print ('mal')
    if seleccion == 1:
        suma()
    if seleccion == 2:
        resta()
    if seleccion == 3:
        mult()
    if seleccion == 4:
        div()   
    if(seleccion == 0):
        a = 7
    
    