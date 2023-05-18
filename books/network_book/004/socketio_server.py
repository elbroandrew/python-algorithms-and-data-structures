from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"
app.env="development"
io = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@io.on('message')
def handle_message(data):
    print("received message: " + data)
    io.send(data)

@io.on("hello")
def send_world(data):
    print(data)
    io.send("WORLD from SERVER")

if __name__ == '__main__':
    print("serving at port: ", "http://localhost:5000")
    io.run(app)
