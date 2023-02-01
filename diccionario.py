midiccionario = {"key1":"value1", "key2":"value2"}
print(midiccionario["key2"])
print(midiccionario)

paises ={ "peru":"lima","ecuador":"quito"}
print(paises["ecuador"])

#modificacion en el valor de otra clave
paises["ecuador"] = "otracapital"

#eliminacion del par llave y valor
del paises["peru"]
print(paises)

#otros usos del diccionario
ronaldo ={"Cristiano":7 , "Portugal":"Lisboa", "edad":37}

#paso de lista a diccionario
milista3 = ["Espana", "Francia"]
midiccionario2 ={milista3[0]:"madrid", milista3[1]:"paris"}
print(midiccionario2)

#otra formade usar el diccionario
Mundial = {"Argentina":"Campeonatos", "años":["1978","1986"]}
print(Mundial)
print(Mundial["años"])