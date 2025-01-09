import socket
import threading
from flask import Flask, render_template_string

app = Flask(__name__)

picks = []  # Global list to store picks from both clients
results = []  # Global list to store results of each round

# Function to handle each client connection
def handle_client(conn, addr, client_index):
    print(f"Client {client_index + 1} connected from {addr}")
    client_picks = []

    try:
        for _ in range(10):  # Expect 10 rounds of picks
            pick = conn.recv(1024).decode().strip()
            if not pick:
                break
            print(f"Client {client_index + 1} pick: {pick}")
            client_picks.append(pick)

        if len(client_picks) == 10:
            picks.append(client_picks)
        else:
            print(f"Error: Client {client_index + 1} did not send 10 picks.")
    except Exception as e:
        print(f"Error while handling Client {client_index + 1}: {e}")
    finally:
        conn.close()
        print(f"Client {client_index + 1} disconnected.")

# Function to determine winners for 10 rounds
def determine_winners():
    print(f"Determining winners. Picks: {picks}")
    if len(picks) == 2:  # Ensure both clients' picks are received
        for i in range(10):
            if picks[0][i] == picks[1][i]:
                results.append("Draw")
            elif (picks[0][i], picks[1][i]) in [('R', 'S'), ('P', 'R'), ('S', 'P')]:
                results.append("Client 1 wins")
            else:
                results.append("Client 2 wins")
    print(f"Results: {results}")

# Flask route for displaying results
@app.route("/")
def show_results():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Rock Paper Scissors Results</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 2em; }
                h1 { color: #333; }
                .results { margin-top: 1em; }
                .results p { font-size: 1.2em; margin: 0.5em 0; }
            </style>
        </head>
        <body>
            <h1>Rock Paper Scissors Results</h1>
            <div class="results">
                {% for result in results %}
                    <p>Round {{ loop.index }}: {{ result }}</p>
                {% endfor %}
            </div>
        </body>
        </html>
    """, results=results)

# Main function to set up the server
def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 5002))  # Socket server on port 5001
        server.listen(2)  # Listen for up to 2 clients
        print("Server is ready to accept connections...")

        threads = []
        for client_index in range(2):
            conn, addr = server.accept()
            print(f"Accepted connection from {addr}")
            thread = threading.Thread(target=handle_client, args=(conn, addr, client_index))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if len(picks) == 2 and all(len(client_picks) == 10 for client_picks in picks):
            determine_winners()
            print("Winners determined successfully.")
        else:
            print("Error: Insufficient picks to determine winners.")

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server.close()
        print("Server has shut down.")

    # Start Flask app to display results
    app.run(host='0.0.0.0', port=5002, debug=True)

if __name__ == "__main__":
    main()
