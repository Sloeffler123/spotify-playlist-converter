import socket
import select

def make_socket(main_port, main_ip_address):
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address_port = (main_ip_address, int(main_port))
    listener_socket.bind(address_port)
    listener_socket.listen(1)
    while True:
        read_ready_sockets, _, _ = select.select(
            [listener_socket],
            [],
            [],
            0
        )
        if read_ready_sockets:
            for ready_socket in read_ready_sockets:
                client_socket, _ = ready_socket.accept()
                client_msg = client_socket.recv(1024)
                print(f"Client said: {client_msg.decode("utf-8")}")
                try:
                    client_socket.close()
                    return client_msg.decode("utf-8")
                except OSError:
                    pass

def parse_code(client_msg):
    equal_index = client_msg.index("=")
    and_index = client_msg.index("&")
    return client_msg[equal_index+1:and_index]
