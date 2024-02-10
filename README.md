# Collaborative Playlist Creating Using Socket Programming

## Introduction
This project, completed as part of the **01418351 Computer Network** course, implements a collaborative playlist creating using socket programming. The system allows multiple users to connect to a central server and collaborate on creating playlists.

## Key Features
- **Server-client architecture**: Enables multiple users to connect simultaneously.
- **Playlist management**: Users can view existing playlists, create new playlists, and add songs to existing playlists.
- **Real-time display**: Playlists are managed centrally on the server, allowing real-time display for all connected clients.

## Project Structure
1. **Server-side implementation**:
   - Handles incoming connections from clients.
   - Manages the creation and the sharing of playlists.
   - Utilizes threading to handle multiple client connections concurrently.

2. **Client-side implementation**:
   - Connects to the server and interacts with it based on user input.

## Usage
1. Open a terminal window and navigate to the project directory.
2. Run the server script (`server.py`) to start the server.
3. Run the client script (`client.py`) to connect to the server and interact with the system.

Upon running the client script, you will be presented with the following choices:

1. List all the current playlist
2. Create the new playlist
3. Add the song to the playlist
4. Exit

Enter the number corresponding as desired to proceed.

## Contributors
- Chayakorn Chiensuwikarn : 6410450117

<br>

# Protocol defined as Collaborative Playlist Creating Protocol (CPCP)

## Status Codes
The following status codes are used in CPCP responses to indicate the outcome of client requests:

- **200**: List of all playlists
- **201**: Playlist found
- **300**: Playlist creation success
- **301**: Song added to playlist
- **400**: No playlist created yet
- **401**: Invalid playlist number
- **500**: Session closed

## Procedure of Working
1. **Connection Establishment**: Clients establish a TCP connection with the server at a specified address and port.
2. **Command Exchange**: Clients send commands to the server to perform actions such as listing playlists, creating new playlists, and adding songs.
3. **Response Handling**: Clients receive responses from the server indicating the outcome of their requests, including status codes and additional information.
4. **Error Handling**: Clients handle error scenarios such as invalid input, unavailable playlists, and connection interruptions.
5. **Session Termination**: Clients can terminate the session by sending an exit command, closing the connection with the server.

## Instructions
1. **List Playlists**: To list all current playlists, send the command `1` to the server.
2. **Create Playlist**: To create a new playlist, send the command `2` to the server, followed by the playlist name, style, and description separated by colons (`:`).
3. **Add Song to Playlist**: To add a song to a playlist, send the command `3` to the server. Select the playlist by its number and provide the song name and artist separated by colons (`:`).
4. **Exit**: To exit the session, send the command `4` to the server.
