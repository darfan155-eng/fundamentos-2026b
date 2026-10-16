#Figuras geometricas 
op=input("Seleccione la figura que quiere usar \n 1. Cuadrado \n 2. Rectangulo \n 3. Triangulo \n 4. Circunferencia \n")

if op=="1":
    Lado=float(input("Ingrese valor del lado: "))
    Area=Lado*Lado
    Perimetro=Lado*4
    print(f"El area del cuadrado es: {Area}")
    print(f"El perimetro del cuadrado es: {Perimetro}")
elif op=="2":
    Base=float(input("Ingrese el valor de la base: "))
    Altura=float(input("Ingrese el valor de la altura: "))
    Area=Base*Altura
    Perimetro=2*(Base+Altura)
    print(f"El area del rectangulo es: {Area}")
    print(f"El perimetro del rectangulo es: {Perimetro}")
elif op=="3":
    Base=float(input("Ingrese el valor de la base: "))
    Altura=float(input("Ingrese el valor de la altura: "))
    Lado1=float(input("Ingrese el valor del primer lado: "))
    Lado2=float(input("Ingrese el valor del segundo lado: "))
    Lado3=float(input("Ingrese el valor del tercer lado: "))
    Area=(Base*Altura)/2
    Perimetro=Lado1+Lado2+Lado3
    print(f"El area del triangulo es: {Area}")
    print(f"El perimetro del triangulo es: {Perimetro}")
else:
    Pi=3.14
    Radio=float(input("Ingrese el valor del radio: "))
    Area=Pi*Radio^2
    Perimetro=2*Pi*Radio
    print(f"El area de la circunferencia es: {Area}")
    print(f"El perimetro de la cicunferencia es: {Perimetro}")
#Fin