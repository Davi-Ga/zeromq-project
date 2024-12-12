import zmq
import random

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("CLIENTE")

for request in range(10):
    print("Sending request %s …" % request)
    
    numero = random.randint(1, 50)
    
    socket.send(numero.to_bytes(20, byteorder='big'))

    message = socket.recv()
    
    print("Para: " + str(numero) + " Fibonacci: " + str(int.from_bytes(message, byteorder='big')))