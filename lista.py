dias = ["lunes", "martes","miercoles", "jueves","viernes" ]
print(dias[:])
print(dias[1])
print(dias[-1])
print(dias[0:3])
print(dias[2:])

#agregar elemento a la lista
dias.append("sabado")

#agregar elemento y posicion
dias.insert(0,"domingo")

#agregar mas de un elemento a la lista
dias.extend(["sabado","domingo"])
print(dias)

#posicion de un elemento de la lista
print(dias.index("miercoles"))

#saber si hay un elemento de la lista - devuelve TRUE - FALSE
print("jueves" in dias)

#remover un elemento de la lista
dias.remove("lunes")

#remover el ultimo elemento de la lista
dias.pop()

#imprimo una lista la cantidad de veces que quiera
print(dias * 3)

lista1 =[10,20,30, "hola"]
lista2=[100,200,300,"hola2"]
suma = lista1 + lista2

print(suma)