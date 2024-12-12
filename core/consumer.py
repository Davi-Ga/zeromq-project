import zmq
import random

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("CLIENTE")

for request in range(10):
    print("Sending request %s …" % request)
    
    # numero = random.randint(1, 1000)
    
    numero = 1000
    
    socket.send(numero.to_bytes(100, byteorder='big'))

    message = socket.recv()
    
    print("Para: " + str(numero) + " Fibonacci: " + str(int.from_bytes(message, byteorder='big')))