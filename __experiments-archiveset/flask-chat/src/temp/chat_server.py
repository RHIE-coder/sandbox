from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Received: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    # 0.0.0.0: 외부에서 접속 가능하게
    socketio.run(app, host='0.0.0.0', port=5173)