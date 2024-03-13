import random
bandas=[]
banda={}

#x
#eliminar
#numero aleatorio
#resolver variable
#

print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):
    print("1. Registrar Banda")
    print("2. Buscar informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una Banda")
    print("5. Salir")

    opcion = input("Digita una opcion:  ")
    if(opcion.isdigit()):
        opcion=int(opcion)

        if opcion==1:
            banda["id"] = random.randint(1,100)
            banda["nombre"] = input("Nombre de la banda: ")
            banda["genero"] = input("Género: ")
            banda["clasificacion"] = input("Clasificacion: ")
            banda["tiempo"]=int(input("Tiempo: "))
            banda["costo"]=int(input("Costo: $"))
            bandas.append(banda)
        elif opcion==2:

            #tarea transformar todo en minusculas
            bandaBuscada = input("Digite el nombre de la banda que estas buscando: ")
            for bandaAuxiliar in bandas:
                if bandaAuxiliar["nombre"] == bandaBuscada:
                    #como lo encontre nmuestro los datos de la banda auxiliar
                    print(f"id: {bandaAuxiliar[id]}---")
                else:
                    print("Parse siga buscando")


        elif opcion==3:
            print(bandas)
        elif opcion==4:
            pass
        elif opcion==5:
            pass
        else:
            pass

    else:
        print("No es una opcion válida...")
        print("")
        opcion = 100
    