import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Servidor escutando na porta 12345...")

try:
    while True:
        conn, addr = server_socket.accept()
        print(f"Conectado por {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Desconexão detectada para {addr}")
                break
            print(f"Mensagem recebida de {addr}: {data.decode()}")
            response = "Mensagem recebida pelo servidor"
            conn.sendall(response.encode())
        conn.close()
except Exception as e:
    print(f"Erro no servidor: {e}")
finally:
    server_socket.close()
