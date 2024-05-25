import grpc
import hello_service_pb2
import hello_service_pb2_grpc

def run():
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_service_pb2_grpc.GreeterStub(channel)
        # Create a request object
        response = stub.SayHello(hello_service_pb2.HelloRequest(name="Alice"))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()