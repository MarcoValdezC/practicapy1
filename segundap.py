

nombre=  input ("Introduce tu nombre: ")
print(f"Hola {nombre}")

#entero
edad=23

#flotante
altura= 1.63

edstri=str(edad)
print(type(edad))
print(type(edstri))

ed=input("Introduce tu edad:")
ed=int(ed)

if ed >18 and ed<100:
    print("Eres mayor de edad ")
elif ed >=100 :
    print("¿Eres inmortal?")
elif ed<=0:
    print("No existes")
else:
    print("Eres menor de edad")

for i in range(0,10):
    print(i)

#Estructura de control switsh
dia= input("Introduce un día")
dia=int(dia)



    