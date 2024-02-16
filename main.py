from flask import current_app, g
from flask import Flask
from database import DataBase



app = Flask(__name__)

col = DataBase()

@app.route("/")
def index():
    print(col.insertPizza("Pepperoni", ["Ham"]))
    return col.updatePizzaToppings("Pepperoni", ["Ham", "Pepperoni"])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)