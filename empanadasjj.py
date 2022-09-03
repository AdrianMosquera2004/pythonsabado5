from turtle import position


print("***Menu***")
print("1. Agregar 1 Empanada")
print("2. Mostrar Empanada")
print("3. Salir")
opcion=100
#DATOS EMPANADA
#SABOR
#INGREDIENTES (X3)
#PRECIO FABRICACION
#PRECIO VENTA

empanadas={}
ingredientes={}

while(opcion!=3):
    empanada={}
    opcion = int(input("Digite una opcion: "))
    if(opcion == 1):
        empanada ['Sabor'] = input("Digite su sabor: ")
        for i in range(2): 
            ingredientes.append(input(f"Agregue su ingrediente {i+1}: "))
        empanadas ['ingredientes'] = ingredientes
        empanadas ['precio fabricacion'] = input("Agrega precio fabricacion: ")
        empanadas ['precio venta'] = input("Agrega precio de venta: ")
        empanadas.append(empanadas)
        break;
    elif(opcion == 2):
        for index,posicion in empanada:
            print(index,posicion)
            break;
    elif(opcion == 3):
        break;
    else:
        print("Invalid Opcion");
else:
    print("Suerte");                        