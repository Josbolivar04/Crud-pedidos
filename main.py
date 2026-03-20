from Clientes import registro_cliente
from Producto import registro_producto
from Pedido import crearpedido
from totaldia import calcular_ingresos
from Visualizarpedido import verpedido
from reporte import reporte_final

clientes={}
productos={}
pedido={}

while True:

    print("\n------MENÚ PRINCIPAL------")
    print("1.Registrar cliente")
    print("2.Registrar producto")
    print("3.Crear pedido")
    print("4.Ver pedidos")
    print("5.Ver ingresos del dia")
    print("6.Ver reporte final")
    print("7.Salir")

    opcion= input("Seleccione una opcion: ")

    if opcion== "1":
        clientes=registro_cliente(clientes)
        print ("Cliente registrado correctamente, estado: OK")

    elif opcion== "2":
        productos=registro_producto(productos)
    
    elif opcion== "3":
        pedido=crearpedido(clientes,productos,pedido)
    
    elif opcion== "4":
        pedido=verpedido(pedido)
    

    elif opcion== "5":
        totaldia=calcular_ingresos(pedido)
        print (totaldia)

    elif opcion== "6":
        reporte_final(pedido,clientes)
        

    elif opcion== "7":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion invalida")
        

