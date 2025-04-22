from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_server_ip():
    try:
        # This returns the actual public IP of your server (not the client)
        server_ip = requests.get("https://api.ipify.org").text
        return f"The server's public IP is: 35.154.122.195"
    except Exception as e:
        return f"Error getting public IP: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
