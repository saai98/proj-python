from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_my_ip():
    return "The server's public IP is: 35.154.122.195"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
