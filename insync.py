from flask import Flask, render_template
from simplecrypt import encrypt, decrypt

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/<room>')
def client(room):
    return render_template('client.html', room=room)

@app.route('/host/<room_hash>')
def host(room_hash):
    return render_template('host.html', room=decrypt('password', room_hash))

if __name__ == "__main__":
    app.run()
