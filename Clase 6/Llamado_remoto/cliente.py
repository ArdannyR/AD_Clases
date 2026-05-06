import xmlrpc.client  

cliente = xmlrpc.client.ServerProxy("http://localhost:5000/") # http://172.31.115.135:5000/

res_suma = cliente.sumar(4,9)
print(f"Respuesta de suma: {res_suma}")

res_resta = cliente.restar(1,2)
print(f"Respuesta de suma: {res_resta}")

res_multi = cliente.multiplicar(-5,8)
print(f"Respuesta de suma: {res_multi}")

res_divi = cliente.dividir(8,2)
print(f"Respuesta de suma: {res_divi}")