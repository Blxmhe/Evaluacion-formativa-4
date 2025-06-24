
diccionario = {}


def menu():
    print('===MENÚ PRINCIPAL===')
    print('1.-Comprar entrada')
    print('2.-Consultar comprador')
    print('3.-Cancelar compra')
    print('4.-Salir')
    opcion = input('Ingresa una opción: ')
    return opcion

def comprar_entrada(diccionario):
    
    while True:
        nombre_comprador = input('Nombre de quien compra: ').strip()
        if nombre_comprador in diccionario:
            print('ERROR: El comprador ya existe. Prueba con otro nombre')
        else:
            break
    
    while True:
        tipo_entrada = input('Ingresa el tipo de entrada [G: General | V: VIP]: ').strip().upper()
        if tipo_entrada == 'G' or tipo_entrada == 'V':
            break
        else:
            print('El tipo de entrada es inválido. Revisa las opciones e intenta otra vez')
    

    while True:
        codigo_confirmacion = input('Ingresa un código de confirmación\nREGLAS:\n-El mínimo del largo de tu código debe ser de 6 dígitos\n-Debe tener al menos una letra mayúscula\n-Dene tener al menos un número\n-No puede tener espacios en blanco\nCódigo: ')
        
        largo_codigo = False
        tiene_mayus = False
        tiene_num = False
        sin_espacios = True

        if len(codigo_confirmacion) >= 6:
            largo_codigo = True
        for c in codigo_confirmacion:
            if c.isupper():
                tiene_mayus = True
            if c.isdigit():
                tiene_num = True
            if c == ' ':
                sin_espacios = False
        
        if all([largo_codigo,tiene_mayus,tiene_num,sin_espacios]):
            break
        else:
            print('ERROR: Revisa las reglas e intenta otra vez')
        
    print('¡La compra de la entrada fue exitosa!')
    diccionario[nombre_comprador] = [tipo_entrada,codigo_confirmacion]
    print(diccionario)
    return diccionario

def consultar_comprador(diccionario):
    buscar_comprador = input('Ingresa el nombre del comprador que deseas buscar: ').strip()

    if buscar_comprador in diccionario:

        print(f'Comprador: {buscar_comprador}\nTipo de entrada: {diccionario[buscar_comprador][0]}\nCódigo de confirmación: {diccionario[buscar_comprador][1]}')
    else:
        print('El comprador no se encuentra')

def cancelar_compra(diccionario):
    nombre_comprador = input('Ingresa el nombre del dueño de la compra que deseas cancelar: ').strip()

    if nombre_comprador in diccionario:
        del diccionario[nombre_comprador]
        print(f'¡La compra a nombre de {nombre_comprador} fue cancelada!')
    else:
        print(f'No se puede encontrar la compra de {nombre_comprador}')

    return diccionario

def salir():
    print('Programa terminado...')



while True:
    opcion = menu()

    if opcion == '1':
        print('='*20)
        comprar_entrada(diccionario)
    elif opcion == '2':
        print('='*20)
        consultar_comprador(diccionario)
    elif opcion == '3':
        print('='*20)
        cancelar_compra(diccionario)
    elif opcion == '4':
        print('='*20)
        salir()
        break
    else:
        print('='*20)
        print('ERROR: INGRESA UNA OPCIÓN VÁLIDA')





