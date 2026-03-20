

def verpedido(pedido):

 if not pedido:
  print("No hay pedido") # Check if there are no orders
  return pedido
 
 try:
    id_pedido= int(input("Ingrese el ID del pedido: ")) # Ask for the order ID

    if id_pedido not in pedido:
      print("Pedido no existente") # Check if the order exists
      return pedido
    
    info=pedido[id_pedido] 

    print(f"\nPedido #{id_pedido}") # Display order ID
    print(f"Cliente: {info['clientes']}") # Display client name
    print(f"Producto: {info['producto']}") # Display product name
    print(f"Cantidad: {info['cantidad']}") # Display quantity
    print(f"Total: ${info['total']}") # Display total price

 except ValueError: 
   print("Debe ingresar un numero")

 return pedido 