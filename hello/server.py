from concurrent import futures
import grpc
import hello_service_pb2
import hello_service_pb2_grpc

# Service implementation
class Greeter(hello_service_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        response = f"Hello {request.name}!"
        return hello_service_pb2.HelloResponse(message=response)

# Server setup
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()