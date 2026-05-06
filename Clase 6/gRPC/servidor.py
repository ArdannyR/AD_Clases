import grpc
from concurrent import futures

import calculadora_pb2
import calculadora_pb2_grpc

class Calculadora_servidor(
    calculadora_pb2_grpc.CalculadoraServicer
):
    def Sumar(request):
        res = request.a + request.b
        return calculadora_pb2.resultado(r = res)
    
    def Restar(request):
        res = request.a - request.b
        return calculadora_pb2.resultado(r = res)
    
    def Multiplicar(request):
        res = request.a * request.b
        return calculadora_pb2.resultado(r = res)
    
    def Dividir(request):
        res = request.a / request.b
        return calculadora_pb2.resultado(r = res)
    

servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
    Calculadora_servidor(),
    servidor
)





