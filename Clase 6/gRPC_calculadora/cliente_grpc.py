import grpc
import calculadora_pb2
import calculadora_pb2_grpc

canal = grpc.insecure_channel('localhost:5000') # 172.31.115.135 o localhost

stub = calculadora_pb2_grpc.CalculadoraStub(canal)

def sumar(num_a, num_b):
    return stub.Sumar(calculadora_pb2.parametros(a=num_a, b=num_b))

def restar(num_a, num_b):
    return stub.Restar(calculadora_pb2.parametros(a=num_a, b=num_b))

def multiplicar(num_a, num_b):
    return stub.Multiplicar(calculadora_pb2.parametros(a=num_a, b=num_b))

def dividir(num_a, num_b):
    return stub.Dividir(calculadora_pb2.parametros(a=num_a, b=num_b))

operacion = str(input("Ingresa +, -, * o /: "))
num_a = int(input("Ingresa un entero: "))
num_b = int(input("Ingresa un entero: "))

if operacion == "+":
    print(f"La respuesta de sumar es: {sumar(num_a, num_b).r}")
elif operacion == "-":
    print(f"La respuesta de restar es: {restar(num_a, num_b).r}")
elif operacion == "-":
    print(f"La respuesta de multiplicar es: {multiplicar(num_a, num_b).r}")
elif operacion == "-":
    print(f"La respuesta de dividir es: {dividir(num_a, num_b).r}")
else:
    print(f"Erro en tus datos")
