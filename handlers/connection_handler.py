from models.playlist import Playlist
from models.song import Song

def handle_client_connection(server_socket, client_socket, client_address, playlists, playlist_id_increment):
    try:
        while True:
            # Receive the choice from the client
            choice = client_socket.recv(1024).decode()
        
            response = ""
            
            # Handling the client's choice
            if choice == "1":
                # Check if there are playlists available
                if len(playlists) == 0:
                    # Send response indicating no playlists created yet
                    response = "400::No playlist created yet"
                elif len(playlists) > 0:
                    # Send response with list of all playlists
                    response = "200::List of all playlist\n"
                    
                    for playlist in playlists:
                        response += f"\n{playlist}\n"
                        
            elif choice == "2":
                
                # Receive playlist details from the client
                playlist_name, playlist_style, playlist_description = client_socket.recv(1024).decode().split(":")
                
                # Generate unique playlist ID based on client's address and port
                playlist_id = f"{client_address[0]}-{client_address[1]}-{playlist_id_increment}"
                
                # Create a new playlist instance and append it to the playlists list
                playlist = Playlist(playlist_id, playlist_name, playlist_style, playlist_description)
                playlists.append(playlist)
                
                # Increment the playlist ID counter
                playlist_id_increment += 1
                
                # Send response indicating playlist creation
                response = f"300::Playlist '{playlist_name}' created" 
            
            elif choice == "3":
                
                if len(playlists) == 0:
                    # Send response indicating no playlists created yet
                    response = "400::No playlist created yet"
                    client_socket.send(response.encode())
                    continue    

                elif len(playlists) > 0:
                    # Send response with list of all playlists
                    response = "200::List of all playlist\n"
                    for playlist in playlists:
                        response += f"{playlist}\n"
                    client_socket.send(response.encode())
                    
                    # Receive playlist ID from the client
                    playlist_id = client_socket.recv(1024).decode()
                    
                    # Check if the received playlist ID is valid
                    playlist_ids = []
                    for playlist in playlists:
                        playlist_ids.append(str(playlist.pid))
                    
                    if playlist_id not in playlist_ids:
                        # Send response indicating invalid playlist number
                        response = "401::Invalid playlist number"
                    
                    elif playlist_id in playlist_ids:
                        # Send response indicating playlist found
                        client_socket.send("201::Playlist found".encode())
                        
                        # Receive song details from the client
                        song_name, song_artist = client_socket.recv(1024).decode().split(":")
                        
                        # Create a new song instance
                        newSong = Song(song_name, song_artist)
                        
                        # Add the new song to the corresponding playlist
                        for playlist in playlists:
                            if playlist.pid == playlist_id:
                                current_playlist = playlist
                                
                        current_playlist.add_song(newSong)
                        
                        # Send response indicating song added to playlist
                        response = "301::" + f"Song '{newSong.name}' added to playlist '{current_playlist.name}'"

            elif choice == "4":
                # Send response indicating session closed
                response = "500::Session closed"
                client_socket.send(response.encode())
                print(f"Connection closed with {client_address}")
                # Close the client socket and exit the loop
                client_socket.close()
                break
            
            # Send the response to the client
            client_socket.send(response.encode())
            
    except KeyboardInterrupt:
        # Handle keyboard interrupt (SIGINT) gracefully
        print("\n\nServer interrupted. Closing...")
        server_socket.close()