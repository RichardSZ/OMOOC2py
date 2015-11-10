import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8250)
s.bind(server_address)
'''
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('localhost', 8250)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
s.bind(server_address)

'''
dairy = open('dairy.txt','a+')
print dairy.read()

dairyinput, clientaddress = s.recvfrom(4096)
dairy = open('dairy.txt','a+')
dairy.write("%s\n"%dairyinput)
dairy.close()

s.close()
