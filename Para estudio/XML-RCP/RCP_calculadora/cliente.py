import xmlrpc.client  

cliente = xmlrpc.client.ServerProxy("http://localhost:5000/") # http://172.31.115.135:5000/

operacion = str(input("Ingresa +, -, * o /: "))
num_a = int(input("Ingresa un entero: "))
num_b = int(input("Ingresa un entero: "))

if operacion == "+":
    res_suma = cliente.sumar(num_a,num_b)
    print(f"Respuesta de suma: {res_suma}")
elif operacion == "-":
    res_resta = cliente.restar(num_a,num_b)
    print(f"Respuesta de suma: {res_resta}")
elif operacion == "*":
    res_multi = cliente.multiplicar(num_a,num_b)
    print(f"Respuesta de suma: {res_multi}")
elif operacion == "/":
    res_divi = cliente.dividir(num_a,num_b)
    print(f"Respuesta de suma: {res_divi}")
else:
    print(f"Erro en tus datos")
