# Jojo174code-Rock-Paper-Scissors-Server-Connection-Game


The uploaded files consist of two Python scripts: ClientRPS.py and ServerRPS.py. These scripts implement a simple game of "Rock, Paper, Scissors" (RPS) played between two clients, with the server determining the winner and displaying the results through a web interface.

Explanation of the Code:
1. ClientRPS.py (Client)

-Purpose: This script simulates a client that randomly selects a move (Rock, Paper, or Scissors) for 10 rounds and sends it to the server.

-How It Works:

  --It connects to a server running on localhost at port 5002.

  --The client randomly picks a move (R, P, or S) 10 times and sends each pick to the server.

  --There is a slight delay (time.sleep(0.1)) between each pick to ensure the server processes the moves correctly.

  --After sending all 10 moves, the client closes the connection.

-How to Use:

  1) Run the ServerRPS.py script first (instructions below).
   
  2) Then, run the ClientRPS.py script.
   
  3) The client will automatically send 10 moves to the server, which will then process the game.
   
2. ServerRPS.py (Server)

-Purpose: This script acts as the server for the Rock, Paper, Scissors game. It listens for two clients to connect, receives their moves, determines the winner of each round, and displays the results on a web page.

-How It Works:

  --The server creates a socket and listens for two clients to connect on localhost:5002.

  --Each client sends its moves (10 rounds), which are stored in the picks list.

  --After both clients have sent their moves, the server compares their moves round by round to determine the winner (Client 1, Client 2, or Draw).

  --The results are stored in the results list.

  --After processing all rounds, a Flask web app is launched to display the results on a web page.

  --The Flask app listens on localhost:5002 and renders the game results in a simple HTML format.

  -- Or you can view the results in your terminal 

How to Use:

1) Start the Server: Run the ServerRPS.py script.
python ServerRPS.py

  --This will start the server and the Flask web application.
  
2) Start the Client: Run the ClientRPS.py script on the same or a different machine.
python ClientRPS.py

  --The client will send 10 moves to the server.
  
-View Results: After both clients have played 10 rounds, the server will display the results on a webpage hosted at http://localhost:5002.
