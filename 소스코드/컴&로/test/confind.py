import sys
import socket
import argparse


def main():
    #   setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", type=str, required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    if host is None:
        host=''
    if port is None:
        port=0

    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print ("Error creating socket: ", e)
        sys.exit(1)

    # Second try-except block -- connect to given host/port
    try:
        s.connect((host,port))
    except socket.gaierror as e:
        print ("Address-related error connecting to server: ", e)
        sys.exit(1)
    except socket.error as e:
        print ("Connection error: ", e)
        sys.exit(1)

    # Third try-except block -- sending data
    try:
        s.sendall(str("GET " + str(filename) + " HTTP/1\r\n\r\n").encode())
    except socket.error as e:
        print ("Error sending data: ", e)
        sys.exit(1)

    while 1:
        # Fourth try-except block -- waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print ("Erro receiving data: ",  e)
            sys.exit(1)
        if not len(buf):
            break
        #write the received data
        sys.stdout.write(buf.decode())

if __name__ == '__main__':

    main()