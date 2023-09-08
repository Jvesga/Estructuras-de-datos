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

def metodo_burbuja(arr): ## El método burbuja es el encargado de organizar los numeros numero por numero intercambiandolos de posición
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