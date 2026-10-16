#Operaciones basicas con dos numeros
print("Ingrese dos numeros para realizar operaciones basicas")
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))

#Seleccionar operación
op=input("Seleccione la operación que desea realizar: \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n")

if op=="1":
    resultado=num1+num2
    print(f"Suma: {resultado}")
elif op=="2":
    resultado=num1-num2
    print(f"Resta: {resultado}")
elif op=="3":
    resultado=num1*num2
    print(f"Multip: {resultado}")
else:
    resultado=num1/num2
    print(f"División: {resultado}")
#Fin