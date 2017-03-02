from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/<room>')
def client(room):
    return render_template('client.html', room=room)

@app.route('/host/<room>')
def host(room):
    return render_template('host.html', room=room)

if __name__ == "__main__":
    app.run()
