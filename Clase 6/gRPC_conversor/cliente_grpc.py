import grpc
import conversor_pb2
import conversor_pb2_grpc

canal = grpc.insecure_channel('localhost:5000') # 172.31.115.135 o localhost

stub = conversor_pb2_grpc.ConversorStub(canal)

def C_a_F(temp):
    return stub.C_a_F(conversor_pb2.parametros(temp_1=temp))

def F_a_C(temp):
    return stub.F_a_C(conversor_pb2.parametros(temp_1=temp))


operacion = str(input("Ingresa °C para pasar a °F o °F para pasar a °C: "))
temp = float(input("Ingresa una temperatura: "))

if operacion == "C":
    print(f"La respuesta en °F es: {C_a_F(temp).conversion}")
elif operacion == "F":
    print(f"La respuesta en °C es: {F_a_C(temp).conversion}")
else:
    print(f"Error en tus datos")
