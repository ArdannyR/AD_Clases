import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000")

menu = "\nMENU \n1. Ver lista de peliculas \n2. Agregar una pelicula \n3. Actulizar una pelicula \n4. Eliminar una pelicula \n5. Salir"

while True:
    print(menu)
    opcion = int(input("\nSeleccione una opcion: ")) 
    match opcion:
        case 1:
            print(proxy.obtener_peliculas())

        case 2:
            titulo = str(input("Ingrese titulo de la pelicula: "))
            genero = str(input("Ingrese genero de la pelicula: "))
            # proxy.agregar_pelicula(titulo, genero)
            print(proxy.agregar_pelicula(titulo, genero))

        case 3: 
            print(proxy.obtener_peliculas())
            objetivo = int(input("Ingrese el numero de la pelicula a actualizar: "))
            titulo = str(input("Ingrese el nuevo titulo de la pelicula: "))
            genero = str(input("Ingrese el nuevo genero de la pelicula: "))
            # proxy.actualizar_pelicula(objetivo, titulo, genero)
            print(proxy.actualizar_pelicula(objetivo, titulo, genero))
           
        case 4:
            print(proxy.obtener_peliculas())
            objetivo = int(input("Ingrese el numero de la pelicula a eliminar: "))
            # proxy.eliminar_pelicula(objetivo)
            print(proxy.eliminar_pelicula(objetivo))

        case 5:
            print("\nSaliendo...")
            break

        case _:
            print("\nOpcion no valida")