def reporte_final(pedido,clientes):

    if not pedido:
        print("No hay pedido registrado") # Check if there are no orders registered
        return
    
    total_ingresos=0 # Variable to store total income
    ventas_clientes={} # Dictionary to store sales per client

    for id_pedido in pedido:

        info=pedido[id_pedido] # Get order information
        total_ingresos +=info["total"] # Add order total to total income
        cliente=info["clientes"] # Get client name

        if cliente in ventas_clientes:
            ventas_clientes[cliente]+= info["total"] # Add to existing client total
        else:
            ventas_clientes[cliente]=info["total"] # Initialize client total

    print ("\n----REPORTE FINAL----") 

    print(f"\nTotal de pedidos: {len(pedido)}") # Show total number of orders
    print(f"Total de ingresos: ${total_ingresos:,.2f}") # Show total income formatted

    print("\n-----VENTAS POR CLIENTE----") 

    for cliente in ventas_clientes:
        print(f"{cliente}: ${ventas_clientes[cliente]:,.2f}") # Show total



    
