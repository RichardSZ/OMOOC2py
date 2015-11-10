import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''s.sendto('r', localhost,8250)
log,serveraddress = s.recvfrom(4096)
print log
'''
hostaddress = ('localhost', 8250)
while True:
    typein = raw_input('>>>')
    s.sendto(typein, hostaddress)

s.close()

