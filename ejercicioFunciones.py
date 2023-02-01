from re import X


def maximo(x, y ,z):
    if(x > y ) and (x > z):
        return x, print(" x es el mayor numero:" ,x )
    elif(y > x) and (y > z):
        return y,print("y  es el mayor numero:" ,y) 
    elif(y == x) and (x > z):
        return y, x,print("x, y  son iguales:" ,x, y) 
    else:
        return z, print( "z es el mayor numero:", z )  

maximo(10,10,11)