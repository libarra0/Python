#def imprimir_mensaje():
#    print("Mensaje especial")
#    print("Estoy aprendiendo a usar unciones")

#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

def conversasion(mensaje):
    print("Hola")
    print("Cómo estás")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opción (1, 2, 3)"))
if opcion == 1:
    conversasion("Elegiste la opción 1")
elif opcion == 2:
    conversasion("Elegiste la opción 2")
elif opcion == 3:
    conversasion("Elegiste la opción 1")
else:
    print("Escribe la opción correcta")
