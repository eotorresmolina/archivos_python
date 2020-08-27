#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Torres Molina Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.2"


import csv


def ej1():
    print("Cuenta caracteres.\n\n")
    cantidad_letras = 0
    cantidad_lineas = 0
    nombre_archivo = 'texto.txt'

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    with open(nombre_archivo, 'r') as fi:
        for line in fi:
            cantidad_lineas += 1
            print('La Cantidad de Caracteres que Tiene la Línea {} es: {} '.format(cantidad_lineas, len(line)))
            cantidad_letras += len(line)

    cantidad_letras += (cantidad_lineas-1)   
    print('\nLa Cantidad de Caracteres que Tiene el Archivo "{}" es: {}\n\n'.format(nombre_archivo, cantidad_letras))


def ej2():
    print("Transcribir!\n\n")
    cantidad_letras = 0
    nombre_archivo = 'transcribir.txt'
    texto_ingresado = None

    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''

    fo = open(nombre_archivo, 'w')

    print('A Continuación Deberá Ingresar un Texto o Presionar Enter para Salir.\n')
    while ((texto_ingresado == None) or (texto_ingresado != '')):
        texto_ingresado = str(input('Ingrese el Texto que Desee: '))
        cantidad_letras += len(texto_ingresado)
        fo.write(texto_ingresado + '\n')

    fo.close()

    print('\nLa Cantidad de Caracteres que se Ingresaron en Total es: {}\n\n'.format(cantidad_letras))


def ej3():
    print("\n\nEscrutinio de los Alquileres de Capital Federal:\n\n")
    cantidad_ambientes = None
    precios = []

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''

    cantidad_ambientes = int(input('Ingrese la Cantidad de Ambientes de los Alquileres: '))

    with open('propiedades.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

        for row in range(len(data)):
            if data[row].get('ambientes') == str(cantidad_ambientes):
                if data[row].get('moneda') == 'ARS':
                    precios.append(float(data[row].get('precio')))
  
    try:
        promedio = sum(precios) / len(precios)
        max_valor = max(precios)
        min_valor = min(precios)

        print('\n1-La Cantidad de Alquileres de Departamentos de {} Ambientes Disponibles es: {}.'.format(cantidad_ambientes, len(precios)))
        print('2-El Promedio del Valor de los Alquileres en Pesos ($) es: {}'.format(promedio))
        print('3-El Máximo Valor de Alquileres en Pesos ($) es: {}'.format(max_valor))
        print('4-El Mínimo Valor de Alquileres en Pesos ($) es: {}\n\n'.format(min_valor))

    except ZeroDivisionError:
        print('\n1-La Cantidad de Alquileres de Departamentos de {} Ambientes Disponibles es: {}.'.format(cantidad_ambientes, len(precios)))


def ejercicio_extra():
    print("Ahora sí! buena suerte :)\n\n")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
    nombre_archivo = '2019 Ironman World Championship Results.csv'

    # Tiempos para la División MPRO:
    times_swim_mpro = []
    times_bike_mpro = []
    times_run_mpro = []

    # Tiempos para la División M45-49:
    times_swim_m4549 = []
    times_bike_m4549 = []
    times_run_m4549 = []

    # Tiempos para la División M25-29:
    times_swim_m2529 = []
    times_bike_m2529 = []
    times_run_m2529 = []

    # Tiempos para la División M18-24:
    times_swim_m1824 = []
    times_bike_m1824 = []
    times_run_m1824 = []

    with open(nombre_archivo, 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
        
        for row in range(len(data)):

            # División MPRO:
            if data[row].get('Division') == 'MPRO':
                time = data[row].get('Swim').split(sep=':')     # DEPORTE: Swim
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_swim_mpro.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Bike').split(sep=':')     # DEPORTE: Bike
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_bike_mpro.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Run').split(sep=':')      # DEPORTE: Run
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_run_mpro.append(cant_seconds)
                except ValueError:
                    pass


            # División M45-49
            elif data[row].get('Division') == 'M45-49':
                time = data[row].get('Swim').split(sep=':')     # DEPORTE: Swim
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_swim_m4549.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Bike').split(sep=':')     # DEPORTE: Bike
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_bike_m4549.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Run').split(sep=':')      # DEPORTE: Run
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_run_m4549.append(cant_seconds)
                except ValueError:
                    pass


            # División: M25-29
            elif data[row].get('Division') == 'M25-29': 
                time = data[row].get('Swim').split(sep=':')     # DEPORTE: Swim
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_swim_m2529.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Bike').split(sep=':')     # DEPORTE: Bike
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_bike_m2529.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Run').split(sep=':')      # DEPORTE: Run
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_run_m2529.append(cant_seconds)
                except ValueError:
                    pass

            
            # División: M18-24
            elif data[row].get('Division') == 'M18-24':
                time = data[row].get('Swim').split(sep=':')     # DEPORTE: Swim
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_swim_m1824.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Bike').split(sep=':')     # DEPORTE: Bike
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_bike_m1824.append(cant_seconds)
                except ValueError:
                    pass

                time = data[row].get('Run').split(sep=':')      # DEPORTE: Run
                try:
                    cant_seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
                    times_run_m1824.append(cant_seconds)
                except ValueError:
                    pass

    # División: MPRO:
    promedio_tiempo_swim = sum(times_swim_mpro) / len(times_swim_mpro)
    promedio_tiempo_bike = sum(times_swim_mpro) / len(times_swim_mpro)
    promedio_tiempo_run = sum(times_swim_mpro) / len(times_swim_mpro)

    print('División: "MPRO":\n')
    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(max(times_swim_mpro)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(min(times_swim_mpro)))
    print('3-El Tiempo Promedio en la Categoría "Swim" es: {} segundos.\n'.format(promedio_tiempo_swim))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(max(times_bike_mpro)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(min(times_bike_mpro)))
    print('3-El Tiempo Promedio en la Categoría "Bike" es: {} segundos.\n'.format(promedio_tiempo_bike))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(max(times_run_mpro)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(min(times_run_mpro)))
    print('3-El Tiempo Promedio en la Categoría "Run" es: {} segundos.\n'.format(promedio_tiempo_run))

    # División: M45-49:
    promedio_tiempo_swim = sum(times_swim_m4549) / len(times_swim_m4549)
    promedio_tiempo_bike = sum(times_swim_m4549) / len(times_swim_m4549)
    promedio_tiempo_run = sum(times_swim_m4549) / len(times_swim_m4549)

    print('División: "M45-49":\n')
    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(max(times_swim_m4549)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(min(times_swim_m4549)))
    print('3-El Tiempo Promedio en la Categoría "Swim" es: {} segundos.\n'.format(promedio_tiempo_swim))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(max(times_bike_m4549)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(min(times_bike_m4549)))
    print('3-El Tiempo Promedio en la Categoría "Bike" es: {} segundos.\n'.format(promedio_tiempo_bike))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(max(times_run_m4549)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(min(times_run_m4549)))
    print('3-El Tiempo Promedio en la Categoría "Run" es: {} segundos.\n'.format(promedio_tiempo_run))

    # División: M25-29:
    promedio_tiempo_swim = sum(times_swim_m2529) / len(times_swim_m2529)
    promedio_tiempo_bike = sum(times_swim_m2529) / len(times_swim_m2529)
    promedio_tiempo_run = sum(times_swim_m2529) / len(times_swim_m2529)

    print('División: "M2524":\n')
    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(max(times_swim_m2529)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(min(times_swim_m2529)))
    print('3-El Tiempo Promedio en la Categoría "Swim" es: {} segundos.\n'.format(promedio_tiempo_swim))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(max(times_bike_m2529)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(min(times_bike_m2529)))
    print('3-El Tiempo Promedio en la Categoría "Bike" es: {} segundos.\n'.format(promedio_tiempo_bike))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(max(times_run_m2529)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(min(times_run_m2529)))
    print('3-El Tiempo Promedio en la Categoría "Run" es: {} segundos.\n'.format(promedio_tiempo_run))

    # División: M18-24:
    promedio_tiempo_swim = sum(times_swim_m1824) / len(times_swim_m1824)
    promedio_tiempo_bike = sum(times_swim_m1824) / len(times_swim_m1824)
    promedio_tiempo_run = sum(times_swim_m1824) / len(times_swim_m1824)

    print('División: "M18-24":\n')
    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(max(times_swim_m1824)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Swim" es: {} segundos.'.format(min(times_swim_m1824)))
    print('3-El Tiempo Promedio en la Categoría "Swim" es: {} segundos.\n'.format(promedio_tiempo_swim))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(max(times_bike_m1824)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Bike" es: {} segundos.'.format(min(times_bike_m1824)))
    print('3-El Tiempo Promedio en la Categoría "Bike" es: {} segundos.\n'.format(promedio_tiempo_bike))

    print('1-El Tiempo Máximo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(max(times_run_m1824)))
    print('2-El Tiempo Mínimo Hecho por un Competidor en la Categoría "Run" es: {} segundos.'.format(min(times_run_m1824)))
    print('3-El Tiempo Promedio en la Categoría "Run" es: {} segundos.\n\n\n'.format(promedio_tiempo_run))


if __name__ == '__main__':
    print("\n\nEjercicios de práctica:\n\n")
    ej1()
    ej2()
    ej3()
    ejercicio_extra()
