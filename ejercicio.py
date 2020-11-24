print("\n***********************************")
print(" \ SISTEMA VACACIONAL DE EMPLEADOS \ ")
print("***********************************\n")

nombre_empleado = input("introdusca el  nombre de empleado: ")
clave_departamento = int(input("\n por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("\n por favor introduce los años lavorados del empleado: "))

if clave_departamento == 1:
    
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '6 dias'de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '14 dias' de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("el empleado ", nombre_empleado, " tiene derecho a '20 dias' de vacciones.")
    else:
        print("\n el empleado ",nombre_empleado, " aun no tiene derecho a vaciones ")
    
elif clave_departamento == 2:

    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '7 dias' de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '15 dias' de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '22 dias' de vacaciones.")
    else:
        print("\n el empleado ", nombre_empleado, " aun no tiene derecho a vacaciones.")

elif clave_departamento == 3:

    if antiguedad_empleado == 1 and antiguedad_empleado <2:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '10 dias' de vacaciones.")
    elif antiguedad_empleado >= 2 and  antiguedad_empleado <= 6:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '20 dias' de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("\n el empleado ", nombre_empleado, " tiene derecho a '30 dias' de vacaciones.")
    else:
        print("\n el empleado ", nombre_empleado, " aun no tiene derecho a vacaciones.")
else:
    print("\n--------------------------------------------------------")
    print("la clave del departamento no existe, vuelve a intentarlo")
    print("--------------------------------------------------------")

print("\n*********************")
print(' " muchas gracias " ')
print("*********************")


print("\n**************************************************")
print("programa que determina si un numero es par o impar")
print("**************************************************\n")

numero = int(input("por favor introduce un numero entero: "))

if numero % 2 == 0:
    print("el numero ", numero, " es par.")
elif numero % 2 == 1:
    print("el numero ", numero, " es impar.")
    
print("\n fin. \n")

print("-------------------")
print("que numero es mayor")
print("-------------------\n")

num_uno = int(input("introduce el primer valor: "))
num_dos = int(input("introduce el segundo valor: "))
num_tres = int(input("introduce el tercer valor: "))

if num_uno > num_dos and num_uno > num_tres:
    print("el numero ", num_uno, " es el mayor.")
else:
    if num_dos > num_tres:
        print("el numero ", num_dos, " es el mayor.")
    else:
        print("el numero ", num_tres, " es el mayor.")









