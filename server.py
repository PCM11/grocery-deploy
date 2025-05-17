from flask import Flask

app = Flask(__name__)

#  curl "http://127.0.0.1:5000"
@app.route('/')
def index():
    return "Welcome to pythonanywhere"

if __name__ == '__main__':
    app.run(debug=True)
