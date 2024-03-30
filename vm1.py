#Write the python code which runs on this machine and sends the Hello message to VM initiated in my machine
import socket
import sys
import time
import os

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('', 10000)
message = 'Hello'
try:
    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)
    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

# Path: vm2.py
