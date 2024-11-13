from pywebio.input import input, TEXT
from pywebio.output import put_text
from pywebio.platform.flask import webio_view
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    name = input("What's your name?", type=TEXT)
    put_text(f"Hello, {name}!")
    return "Web page is running"

if __name__ == '__main__':
    app.run()