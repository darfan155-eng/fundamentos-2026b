#Conversión de unidades
op=input("Seleccione la conversión que quiere usar \n 1. Temperatura \n 2. Distancia \n 3. Peso \n 4. Moneda \n")

if op=="1":
    Celsius=float(input("Ingrese el valor de celsius: "))
    Kelvin= Celsius + 273.15
    Fahrenheit = (Celsius * 1.8) + 32
    print(f"Los Kelvin son: {Kelvin}")
    print(f"Los Fahrenheit son: {Fahrenheit}")
elif op=="2":
    Kilometros= float(input("Ingrese el valor de Kilometros: "))
    Millas= Kilometros * 0.621371
    print(f"Las millas son: {Millas} ")
elif op=="3":
    Kilogramos= float(input("Ingrese el valor de Kilogramos: "))
    Libras= Kilogramos * 2.20462
    print(f"Las libras son: {Libras}")
else:
   Dolares= float(input("Ingrese el valor de Dolares: ")) 
   Peso_Colombianos= 3,207.67
   print(f"Los pesos Colombianos son: {Peso_Colombianos} ")

#Fin