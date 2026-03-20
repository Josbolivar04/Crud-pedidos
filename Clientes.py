def registro_cliente(clientes):

 while True:
    try:
        Id_cliente=int(input(f"\nIngrese su numero de identificacion (Cedula): ")) #Request ID number
        if Id_cliente < 0: #Check for negatives values
            print("Su numero de identificacion no tiene ningun valor negativo")
        elif Id_cliente in clientes: #Check for duplicates users
            print("Error:Este cliente ya se encuentra registrado")
        else:
            break
    except ValueError:
        print("Error:debe ingresar su cedula sin puntos ni comas")

 while True: 
    nombre=str(input("Ingrese su nombre: ")) #Request client name
    if nombre.replace(" ","").isalpha(): #Check for letters only
     break
 
    else:
     print("Error: solo debe ingresar letras.") #Verificar que no ingresen valores numericos
    
    
 while True:

    correo=input("Ingrese su correo electronico: ") #Request email
    if "@" in correo and "." in correo: #Check that email is ok
     break
    else:  
     print ("Error:Correo invalido, verifique que tenga el @ y .(punto).")

 clientes[Id_cliente]= {
     "nombre":nombre,
     "correo":correo
    }
 
 return clientes