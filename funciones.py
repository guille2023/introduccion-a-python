#funcion
def miFuncion():
    print("hola mundo")
    print("Estoy practicando")



miFuncion()



def aprobados():
    a= int(0)
    b= int(0)



def suma(num1, num2):
    print("tu suma es la siguiente: " ,num1 + num2)

suma(10,20)

suma(101,20)


#saludar (input("ingrese tu nombre : "))
# int(input("ingresa su edad: "))



def multiplicar(num1, num2):
    mul = num1 * num2
    return print(mul)


multiplicar(20, 4)    

def maximo(x, y ,z):
    if(x > y ) and (x > z):
        return x, print(" x es el mayor numero")
    elif(y > x) and (y > z):
        return y,print("y  es el mayor numero")
    else:
        return z, print( "z es el mayor numero")

maximo(5,9,3)