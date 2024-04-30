nombre = input("Ingrese nombre de la persona:")
edad = int(input("Ingrese la edad de persona:"))
sueldo = float(input("Ingrese el sueldo de la persona:"))

mesajeFinal= "Nombre:%s\nEdad:%d\nSueldo:%.2f\n" % (nombre,edad,sueldo)
print(mesajeFinal)