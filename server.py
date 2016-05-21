import socket
import sys

#create a socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind the socket
server_address = ("localhost", 5000)
print >>sys.stderr, "starting ip on %s port %s" %server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, "\nwaiting to receive message"
    data, address = sock.recvfrom(4096)

    print >>sys.stderr, "\nreceived %s data from %s" % (len(data), address)
    print >>sys.stderr, data

    if data:
        sent=sock.sendto(data, address)
        print >>sys.stderr, "sent %s bytes back to %s" %(sent, address)
