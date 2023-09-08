import random
import time


tiempo_inicio = time.time()

def ordenar_rapido(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return ordenar_rapido(izquierda) + medio + ordenar_rapido(derecha)

def generar_arreglo_aleatorio(n):
    return [random.randint(1, 200) for _ in range(n)]

num_elementos = int(input("Ingresa el número del vector: "))

arreglo = generar_arreglo_aleatorio(num_elementos)
print("Vector original:", arreglo)


arreglo_ordenado = ordenar_rapido(arreglo)


print("Vector ordenado:", arreglo_ordenado)
tiempo_fin = time.time()
print(f"Tiempo de ejecución: {tiempo_fin - tiempo_inicio:.6f} segundos")