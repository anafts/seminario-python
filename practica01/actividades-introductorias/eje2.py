#  Escribe un programa que solicite al usuario una cantidad de segundos y muestre cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo

segundos_total = int(input("Ingrese una cantidad de segundos: "))

horas = segundos_total // 3600
minutos = segundos_total % 3600 // 60
segundos = segundos_total % 60

print(f"{segundos_total} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos.")