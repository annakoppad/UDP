import socket
import sys

#create a UDP echo client

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 5000)
message = "This is the first message via UDP"

try:
    #send data
    print >>sys.stderr, "sending %s" % message
    sent =sock.sendto(message, server_address)

    #receive data
    print >>sys.stderr, "waiting to receive"
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, "received %s" %data

finally:
    print >>sys.stderr, "closing socket"
    sock.close()
