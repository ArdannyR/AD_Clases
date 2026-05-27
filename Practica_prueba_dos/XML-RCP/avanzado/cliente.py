import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000")

def menu():
    print("\n1. Registrar | 2. Login")
    opcion = input("Seleccione: ")
    user = input("Usuario: ")
    pssword = input("Password: ")

    if opcion == "1":
        if proxy.registrar(user, pssword):
            print("Registrado!")
        else:
            print("Usuario ya existe.")
    elif opcion == "2":
        if proxy.login(user, pssword):
            print("Login exitoso!")
            p = "Te gusta Docker?"
            r = input(f"{p} (si/no): ")
            print(proxy.guardar_encuesta(user, p, r))
        else:
            print("Credenciales incorrectas.")

menu()