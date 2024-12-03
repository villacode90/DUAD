#Cree un algoritmo que le pida 2 números al usuario, los guarde en dos varibles distintas(´primero´ y ´segundo´ y los ordene de menor a mayor en dichas variables).
A = 0
B = 0
primero = int(input("Por Favor, ingrese el primer número: "))
segundo = int(input("Por Favor, ingrese el segundo número: "))

if(primero < segundo):
    A = primero
    B = segundo
    primero = A
    segundo = B
    print(f"{primero},{segundo}")
else: 
    A = primero
    B = segundo
    primero = B
    segundo = A
    print(f"{segundo},{primero}")