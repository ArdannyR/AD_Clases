import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc

class Calculadora_servidor(calculadora_pb2_grpc.CalculadoraServicer):
    
    def Sumar(self, request, context):
        res = request.a + request.b
        return calculadora_pb2.resultado(r = res)
    
    def Restar(self, request, context):
        res = request.a - request.b
        return calculadora_pb2.resultado(r = res)
    
    def Multiplicar(self, request, context):
        res = request.a * request.b
        return calculadora_pb2.resultado(r = res)
    
    def Dividir(self, request, context):
        if request.b == 0:
            return calculadora_pb2.resultado(r = 0)
        else:
            res = int(request.a / request.b) 
            return calculadora_pb2.resultado(r = res)
    

servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
    Calculadora_servidor(),
    servidor
)
puerto = '5000'
servidor.add_insecure_port(f'[::]:{puerto}')
print(f"Servidor gRPC escuchando en el puerto {puerto}...")

servidor.start()
servidor.wait_for_termination()