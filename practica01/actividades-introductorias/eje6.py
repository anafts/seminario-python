# Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas: una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al finalizar.

multiplos = []
restos = []

num = int(input("Ingrese un número: "))

for i in range(1, num + 1): 
    if i % 5 == 0:
        multiplos.append(i)
    else:
        restos.append(i)

print(f"Múltiplos de 5: {multiplos}, resto de los números: {restos}") 
