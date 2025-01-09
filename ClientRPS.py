import socket
import random
import time

choices = ['R', 'P', 'S']  # Rock, Paper, Scissors

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Attempting to connect to the server...")
        client.connect(('localhost', 5002))  # Connect to server
        print("Connected to the server successfully!")

        for _ in range(10):  # Play 10 rounds
            pick = random.choice(choices)  # Randomly pick R, P, or S
            client.send(pick.encode())  # Send pick to server
            print(f"Sent pick: {pick}")  # Debugging: Confirm each pick is sent
            time.sleep(0.1)  # Add a short delay to ensure server processes picks one by one

        print("All picks sent. Closing connection.")
    except ConnectionRefusedError:
        print("Connection failed: Is the server running and reachable?")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()
        print("Client has disconnected.")

if __name__ == "__main__":
    main()
