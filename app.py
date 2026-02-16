from flask import Flask, render_template

app = Flask(__name__)

fruits = [
    {"name": "Apple", "price": 120, "image": "https://cdn-icons-png.flaticon.com/512/415/415733.png"},
    {"name": "Banana", "price": 40, "image": "https://cdn-icons-png.flaticon.com/512/590/590685.png"},
    {"name": "Orange", "price": 80, "image": "https://cdn-icons-png.flaticon.com/512/415/415682.png"},
    {"name": "Watermelon", "price": 200, "image": "https://cdn-icons-png.flaticon.com/512/590/590694.png"},
    {"name": "Mango", "price": 150, "image": "https://cdn-icons-png.flaticon.com/512/415/415733.png"},
    {"name": "Grapes", "price": 90, "image": "https://cdn-icons-png.flaticon.com/512/415/415718.png"},
    {"name": "Pineapple", "price": 180, "image": "https://cdn-icons-png.flaticon.com/512/415/415710.png"},
    {"name": "Strawberry", "price": 120, "image": "https://cdn-icons-png.flaticon.com/512/415/415696.png"},
    {"name": "Papaya", "price": 130, "image": "https://cdn-icons-png.flaticon.com/512/415/415704.png"},
    {"name": "Kiwi", "price": 100, "image": "https://cdn-icons-png.flaticon.com/512/415/415713.png"},
    {"name": "Pomegranate", "price": 160, "image": "https://cdn-icons-png.flaticon.com/512/415/415708.png"},
    {"name": "Blueberry", "price": 140, "image": "https://cdn-icons-png.flaticon.com/512/415/415699.png"},
]

@app.route("/")
def home():
    return render_template("index.html", fruits=fruits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

