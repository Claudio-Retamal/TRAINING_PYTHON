a = 6
while a != 5:
    seleccion = int(input('INGRESE OPERACIÓN A REALIZAR \n 1-SUMAR \n 2-RESTAR \n 3-MULTIPLICAR \n 4-DIVIDIR \n 0-SALIR \n '))
    print(seleccion)
    
    if seleccion != 1 or seleccion != 2  or  seleccion != 3 or seleccion != 4 or seleccion != 0:
        print('INGRESE UN DIGITO DE LA OPCIÓN') 
    if seleccion == 1:
        print('SELECCION DE SUMA')
        numero_1 = int(input('INGRESE NUMERO 1 \n'))
        numero_2 = int(input('INGRESE NUMERO 2 \n'))
        resultado = numero_1 + numero_2
        print('EL RESULTADO DE SU OPERACIÓN ES ' , resultado)
        
    if seleccion == 2:
        print('SELECCION DE RESTA')
        numero_1 = int(input('INGRESE NUMERO 1 \n'))
        numero_2 = int(input('INGRESE NUMERO 2 \n'))
        resultado = numero_1 - numero_2
        print('EL RESULTADO DE SU OPERACIÓN ES ' ,  resultado)
    if seleccion == 3:
        print('SELECCION DE MULTIPLICACION')
        numero_1 = int(input('INGRESE NUMERO 1 \n \n'))
        numero_2 = int(input('INGRESE NUMERO 2'))
        resultado = numero_1 * numero_2
        print('EL RESULTADO DE SU OPERACIÓN ES ', resultado)
    if seleccion == 4:
        print('SELECCION DE DIVISIÓN')
        numero_1 = int(input('INGRESE NUMERO 1 \n \n'))
        numero_2 = int(input('INGRESE NUMERO 2 \n \n '))
        resultado = numero_1 / numero_2
        print('EL RESULTADO DE SU OPERACIÓN ES ' , resultado)
        
    if seleccion == 0:
        seleccion = 5
 