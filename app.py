from flask import Flask, render_template

app = Flask(__name__)

fruits = [
    {"name": "Apple", "price": 120, "image": "https://cdn-icons-png.flaticon.com/512/415/415733.png"},
    {"name": "Banana", "price": 40, "image": "https://cdn-icons-png.flaticon.com/512/590/590685.png"},
    {"name": "Orange", "price": 80, "image": "https://cdn-icons-png.flaticon.com/512/415/415682.png"},
    {"name": "Mango", "price": 150, "image": "https://cdn-icons-png.flaticon.com/512/590/590696.png"},
    {"name": "Grapes", "price": 90, "image": "https://cdn-icons-png.flaticon.com/512/590/590681.png"},
    {"name": "Watermelon", "price": 200, "image": "https://cdn-icons-png.flaticon.com/512/590/590694.png"},
]

@app.route("/")
def home():
    return render_template("index.html", fruits=fruits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

