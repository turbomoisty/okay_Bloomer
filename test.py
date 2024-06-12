from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    return "Hi"


if __name__ == "__Main__":
    app.run()
