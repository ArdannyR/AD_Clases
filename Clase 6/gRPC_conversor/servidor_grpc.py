import grpc
from concurrent import futures
import conversor_pb2
import conversor_pb2_grpc

class Conversor_servidor(conversor_pb2_grpc.ConversorServicer):
    
    def C_a_F(self, request, context):
        res_F = (request.temp_1 * (9/5)) + 32
        return conversor_pb2.resultado(conversion = res_F)
    
    def F_a_C(self, request, context):
        res_C = (request.temp_1 - 32) / 1.8
        return conversor_pb2.resultado(conversion = res_C)
    

servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
conversor_pb2_grpc.add_ConversorServicer_to_server(
    Conversor_servidor(),
    servidor
)
puerto = '5000'
servidor.add_insecure_port(f'[::]:{puerto}')
print(f"Servidor gRPC escuchando en el puerto {puerto}...")

servidor.start()
servidor.wait_for_termination()