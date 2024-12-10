import zmq
import random

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("CLIENTEEEEEE")

for request in range(10):
    print("Sending request %s …" % request)
    # socket.send(b"Hello")
    numero = random.randint(1, 15)
    print(numero)
    socket.send(int.to_bytes(numero, byteorder='big'))

    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))