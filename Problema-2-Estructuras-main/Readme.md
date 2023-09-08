# _Problema 2_
## _Clase 2_

_Para una cantidad de 4000 numeros almacenados en un vector, ordenar el vector ascendentemente usando el metodo burbuja de acuerdo con los siguientes conceptos:_

_1. Generar los numeros randomicos entre 1 y 2000_
 
_2. Generar en 5 ciclos diferentes cada uno de 800 numeros los valores entre 1 y 400, 4001 y 800, 801 y 1200, 1201 y 1600, 1601 a 2000_

_3. Generar en 5 ciclos diferentes cada uno de entre 1601 a 2000, 1201 y 1600, 801 y 1200, 401 y 800, 1 a 400_
 
### _Codigo_
    import random
    import time

    n = int(input("Digite n: "))
    x = int(n/5)
    vector = []

    inicioTiempo = time.time()

    for i in range(x):
        vector.append(random.randint(1,400))
    for i in range(x):
        vector.append(random.randint(401, 800))
    for i in range(x):
        vector.append(random.randint(801, 1200))
    for i in range(x):
        vector.append(random.randint(1201, 1600))
    for i in range(x):
        vector.append(random.randint(1601, 2000))

    def metodo_burbuja(arr): ## El método burbuja es el encargado de organizar  los numeros numero por numero intercambiandolos de posición
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    metodo_burbuja(vector)
    print(vector)

    finalTiempo = time.time()
    tiempoEjecucion = finalTiempo - inicioTiempo
    print(f"El programa se tardó: {tiempoEjecucion:.4f} segundos.")


_Construir la grafica de f(n) del tiempo promedio de generacion para los siguientes valores de 4000, 8000, 12000, 1600 este valor debe ser ingresado al algoritmo para su ejecucion propia._


