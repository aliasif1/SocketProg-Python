import socket

s = socket.socket()
print('Successfully created a socket')

port = 12345

s.bind(('',port))

s.listen(5)

while True:
    c,addr = s.accept()
    print('Accepted a connection from {}'.format(addr))
    c.send('Thank you for the connection'.encode())
    c.close()
