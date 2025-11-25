from flask import Flask
from calculator import add

app = Flask(__name__)

@app.route("/")
def home():
    return f"Calculator App is running! 2 + 3 = {add(2, 3)}"

@app.route("/division_by_zero")
def division_by_zero():
    0 / 0

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)