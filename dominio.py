import socket

try:
    ip = socket.gethostbyname('google.com')
except socket.gaierror:
    print('Domínio não existe')