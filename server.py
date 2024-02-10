import socket
import threading
from handlers.connection_handler import handle_client_connection

# Server address and port
# SERVER_ADDRESS = ""
SERVER_PORT = 12000

# Empty list to store playlists
playlists = []

# Variable to increment playlist IDs
playlist_id_increment = 1

# Create socket with TCP connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', SERVER_PORT))
server_socket.listen(10)  # Max number of queued connections

print("Server is ready to receive... \n")

try:
    while True:
        # Accept connection from client
        client_socket, client_address = server_socket.accept()
        print("Connection accepted from:", client_address)
        
        # Start a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client_connection, args=(server_socket, client_socket, client_address, playlists, playlist_id_increment))
        client_thread.start()
            
except KeyboardInterrupt:
    print("\n\nServer interrupted. Closing...")
    server_socket.close()
