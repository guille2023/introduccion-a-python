# listas , arrays
dias = ["lunes", "martes","miercoles", "jueves","viernes" ]
for i in dias:
    print("dia: ",i)

dia1= "lunes"
dia2 = "martes"
dia3 = "miercoles"
dias = [dia1,dia2,dia3]    

for i in dias:
    print("dias: ",i)

# inicio fin interacion de 3 en 3
for i in range (3, 33, 3):
    print ("mi repeticion: ",i)    

# break
for i in range(10, 25):
    if i>18:
        break
    print("mi repeticion: ",i)

# continue
for i in range(15, 25):
    if i == 18:
        continue
    print("mi repeticion: ",i)        


for i in range(15, 24):
    if i > 18 and i <21:
        continue
    print("mi repeticion: ",i)      


for i in range(15, 25):
    if i == 14:
        continue
    if i ==18:
        break
    print("mi repeticion: ",i)    
