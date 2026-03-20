def registro_producto(productos):

 while True:
     try:
        Id_producto=int(input(f"Ingrese el numero de identificacion del producto: ")) # Ask for the product ID
        if Id_producto < 0: #Check for negative values
            print("El ID del producto no puede ser negativo")
        elif Id_producto in productos: #Check for registered products
            print("Error:Este producto ya se encuentra registrado")
        else:
            break
     except ValueError:
        print("Error:debe ingresar el ID del producto sin puntos ni comas")
 
 while True: 
    

    nombre_producto=str(input("Ingrese el nombre del producto: ")) #Ask for the client name
    if nombre_producto.replace(" ","").isalpha(): #Check for letters
        break
 
    else:
     print("Error: solo debe ingresar letras.")
    
    
 while True:
     try:
        precio_producto=int(input(f"Ingrese el precio del producto: ")) #Ask for the price of the product
        if precio_producto < 0: #Check for negative values
            print("El valor del producto no puede ser negativo")
        else:
            break
     except ValueError:
        print("Error:debe ingresar unicamente numeros")

 productos[Id_producto]=(nombre_producto, precio_producto)
 
 print("Producto ingresado satisfactoriamente, estado: OK")

 return productos