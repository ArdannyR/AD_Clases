import xmlrpc.client  

cliente = xmlrpc.client.ServerProxy("http://localhost:5000/") # http://172.31.115.135:5000/

operacion = str(input("Ingresa °C para pasar a °F o °F para pasar a °C: "))
temp = float(input("Ingresa una temperatura: "))

if operacion == "C":
    res_en_C = cliente.C(temp)
    print(f"Temperatura en °C: {res_en_C}")
elif operacion == "F":
    res_en_F = cliente.F(temp)
    print(f"Temperatura en °F: {res_en_F}")
else:
    print(f"Erro en tus datos")


