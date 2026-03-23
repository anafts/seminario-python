# Escribe un programa que simule una caja registradora: el usuario ingresa precios de productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total acumulado. Nota: utilizá la sentencia break cuando haga falta

total = 0

precio = float(input("Ingrese el precio de un producto: "))

while precio != 0:
    total += precio
    precio = float(input("Ingrese el precio de un producto: "))

print(f"El total acumulado es: {total}")

"""No entendí bien si es obligatorio usar break, pero en este caso yo pensé que no era necesario porque el ciclo 
se detiene automáticamente cuando el usuario ingresa 0. Por las dudas, también lo hice con break:""" 
while True:
    precio = float(input("Ingrese el precio de un producto: "))
    if precio == 0:
        break
    total += precio

print(f"El total acumulado es: {total}")