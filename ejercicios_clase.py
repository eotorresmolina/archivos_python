#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Emmanuel Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.2"

import csv
import re


def contar_lineas (nombre_archivo):

    cant_lineas = 0
    with open(nombre_archivo, 'r') as file:
        while file.readline() != '':   # Mientras la linea no esté vacía
            cant_lineas += 1

        # Otra Forma Sería:
        #for line in file:
        #    cant_lineas += 1

    return cant_lineas


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''

    nombre_archivo = 'texto.txt'
    cantidad_lineas = contar_lineas(nombre_archivo)
    print('La Cantidad de Líneas que Posee el Archivo "{}" es: {}\n\n'.format(nombre_archivo, cantidad_lineas))


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "notas.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    fi = open('notas.txt', 'r')
    fo = open('copia_notas.txt', 'w')

    for line in fi:
        fo.writelines(line)
        #fo.write(line)     # Otra Forma
        cantidad_lineas += 1

    fi.close()
    fo.close()
    print('La Cantidad de Lineas que se Copiaron es: {}\n\n'.format(cantidad_lineas))


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    cant_dpto_2ambientes = 0
    cant_dpto_3ambientes = 0
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrer dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''

    with open(archivo, 'r') as csvfile:
        data = list(csv.DictReader(csvfile)) # Guardo todas las filas como elementos de una lista.
        for row in range(len(data)):
            ambientes = data[row].get('ambientes')
            if ambientes == '2':
                cant_dpto_2ambientes += 1
            elif ambientes == '3':
                cant_dpto_3ambientes += 1

    print('\nHay {} de Departamentos que son de 2 Ambientes.'.format(cant_dpto_2ambientes))
    print('Hay {} de Departamentos que son de 3 Ambientes.\n\n'.format(cant_dpto_3ambientes))


def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}
    fruta_verdura = 'manzanas'
    stock = 0

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    '''

    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    while fruta_verdura != 'FIN':
        print('\n\nEl Inventario Hasta el Momento es: {}'.format(inventario))
        print('\n\nIngrese el Nombre de una Fruta/Verdura o Ingrese "FIN" para Salir del Programa:')
        fruta_verdura = str(input('Luego Presione Enter para Continuar: '))

        if fruta_verdura != 'FIN':          
            stock = int(input('Ingrese Ahora el Stock de "{}" y Presione Enter Para Continuar: '.format(fruta_verdura)))
            inventario[fruta_verdura] = stock
        else:
            print('\n\nUsted ha Salido del Programa.\n\n')


def ej5():
    # Ejercicios con archivos CSV
    inventario = {'Fruta Verdura': 'manzana', 'Cantidad': 10}
    gondola = {}
    nombre_archivo = 'inventario.csv'
    header = ['Fruta Verdura', 'Cantidad']
    fruta_verdura = ''

    '''
    Parecido al ejercicio anterior: genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.
    with open(nombre_archivo, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()

    with open(nombre_archivo, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

    # Bucle....
        while fruta_verdura != 'FIN':
            print('\n\nIngrese el Nombre de una Fruta/Verdura o Ingrese "FIN" para Salir del Programa.')
            fruta_verdura = str(input('Luego Presione Enter para Continuar: '))

            if fruta_verdura != 'FIN':          
                stock = int(input('Ingrese Ahora el Stock de "{}" y Presione Enter Para Continuar: '.format(fruta_verdura)))
                inventario[header[0]] = fruta_verdura
                inventario[header[1]] = stock
                writer.writerow(inventario)
                gondola[fruta_verdura] = stock
            else:
                print('\n\nUsted ha Salido del Programa.\n\n')

    print('\n\nLa Fruta y Stock Ingresado es: {}'.format(gondola))

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})


if __name__ == '__main__':
    print("\n\n\nBienvenidos a otra clase de Inove con Python:\n\n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
