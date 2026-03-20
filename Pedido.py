
def crearpedido(clientes, productos, pedido):
    # Ask for the client ID
    id_cliente = int(input("Ingrese el ID del cliente: "))
    
    # Check if the client exists in the dictionary
    if id_cliente not in clientes:
        print("Cliente no existe")
        return pedido  

    # Ask for the product ID
    id_producto = int(input("Ingrese ID producto: "))
    
    # Check if the product exists in the dictionary
    if id_producto not in productos:
        print("Producto no existente")
        return pedido  

    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto seleccionado: "))
            
            # Validate that quantity is positive
            if cantidad <= 0:
                print("Debe ser un valor positivo")
            else:
                break  

        except ValueError:
           
            print("Debe ser un valor numerico")

    # Get product name and price from the products dictionary
    nombre_producto, precio_producto = productos[id_producto]

    # Calculate total price
    total = (precio_producto * cantidad)

    # Generate a new order ID
    id_pedido = len(pedido) + 1

    # Store the order information in the dictionary
    pedido[id_pedido] = {
        "clientes": clientes[id_cliente]["nombre"],  # Client name
        "producto": nombre_producto,                # Product name
        "cantidad": cantidad,                       # Quantity ordered
        "total": total                              # Total price
    }

    print(f"Pedido #{id_pedido} creado correctamente")

  
    return pedido

