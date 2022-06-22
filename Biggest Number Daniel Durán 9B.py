print()
print("Encuentre cuál número es más grande!")
print()
print("(Por Daniel Felipe Durán Martínez)")
print()
print("(Puede escribir valores negativos, positivos y/o decimales)")

x=input("Por favor ingrese un número:")
float(x)

y=input("Por favor ingrese otro número:")
float(y)
print()

if x<y: 
    print(y,"es mayor que",x,)
elif x>y: 
    print(y,"es menor que",x,)
else:
    print(x,"y",y,"son iguales.")
    

