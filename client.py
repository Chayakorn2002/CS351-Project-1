import socket 

# Server address and port
SERVER_ADDRESS = ''
SERVER_PORT = 12000

# Splitting, printing status code and status phase
def print_status(response):
    # Split the response into status code and status phase
    statusCode, statusPhase = response.split('::')
    print(statusCode + "::" + statusPhase)
    
# Send data to the server and print the response
def send_and_print_response(data):
    clientSocket.send(data.encode())
    response = clientSocket.recv(1024).decode()
    print_status(response)
    return response

# Handle the user's choice
def choice_handling(choice):
    if choice == "1":
        response = send_and_print_response(choice)

    elif choice == "2":
        clientSocket.send(choice.encode())
        
        # Get playlist details from the user
        playlistName = input("Enter your playlist name: ")
        playlistStyle = input("Enter your playlist style: ")
        playlistDescription = input("Enter your playlist description: ")
        
        response = send_and_print_response(f"{playlistName}:{playlistStyle}:{playlistDescription}")
        
    elif choice == "3":
        response = send_and_print_response(choice)
        
        # If no playlists are available, return
        if response.startswith("400"):
            return
        
        # If playlists are available, continue with adding song
        elif response.startswith("200"): 
            # Get playlist number from the user
            playlistNumber = input("Enter your playlist number: ")

            response = send_and_print_response(playlistNumber)
            
            # If the playlist number is invalid, return
            if response.startswith("401"):
                return
            
            # If the playlist number is valid, continue with adding song
            elif response.startswith("201"):
                # Get song details from the user
                songName = input("Enter your song name: ")
                songArtist = input("Enter your song artist: ")
                
                response = send_and_print_response(f"{songName}:{songArtist}")
        
    elif choice == "4":
        response = send_and_print_response(choice)
        clientSocket.close()
        exit()

# Create socket with TCP connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect((SERVER_ADDRESS, SERVER_PORT))

# Available choices
available_choices = (
    "Available Choices\n"
    "1 : List all the current playlist\n"
    "2 : Create the new playlist\n"
    "3 : Add the song to the playlist\n"
    "4 : Exit"
)
print(available_choices)

while True:
    # Get user's choice
    choice = input("\nEnter your choice: ")
    # Check if the choice is valid
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        continue
    
    # Handle the user's choice
    choice_handling(choice)