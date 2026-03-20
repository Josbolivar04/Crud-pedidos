def calcular_ingresos(pedido):
   
   if not pedido:
      print("No hay pedidos") # Check if there are no orders
      return 0
   
   total_ingresos=0 

   for id_pedido in pedido:
      total_ingresos += pedido[id_pedido]["total"] # Add order's total to total income

   print(f"Total del dia. ${total_ingresos:,.2f}") #total income

   return 

   