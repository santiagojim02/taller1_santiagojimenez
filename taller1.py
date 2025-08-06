ventas = []
menu= ["Crear Nueva Venta", "Listar ventas", "Buscar por ID", "Modificar", "Eliminar", "Calcular Totales", "Salir"]

def nueva_venta():
    id = input ("Ingrese el ID de si producto")
    producto = input ("Ingrese el nombre del producto")
    cantidad = int (input ("Ingrese la cantidad"))
    precio_unitario = int (input ("Ingrese el precio unitario"))

def listar_ventas():
    if ventas:
        for venta in ventas:
            print(ventas)
    else:
        print("no hay venta")

def buscar_por_id():
    id = input("Ingrese ID a buscar: ")
    for venta in ventas:
        if venta[0]==id:
            print("venta encontrada")
        else:
            print("no hay venta")

def modificar_venta():
    id=input("ingrese el id que quiera modificar")
    for i, venta in (ventas):
        if venta[0] == id:
            print("venta actual:", venta)
producto = input("nuevo producto: ")
cantidad = int(input("nueva cantidad: "))
precio_unitario = float(input("nuevo precio: "))
ventas[i] = [id, producto, cantidad, precio_unitario]
print("venta modificada")

def elminar_venta():
    id = input ("ingrese el Id de la venta")
    for i, venta in (ventas):
        if venta[0] == id:
            ventas.pop(i)
print("venta eliminada")

def calcular_totales():
    total = sum(cantidad * precio for _, _, cantidad, precio in ventas)
print("ingreso total: total")

def salir():
    print ("saliendo del programa")
