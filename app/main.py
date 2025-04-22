from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_server_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return f"The server's public IP is: {ip}"
    except Exception as e:
        return f"Could not fetch public IP. Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
