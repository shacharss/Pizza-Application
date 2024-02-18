from flask import Flask, render_template, request, jsonify
from database import DataBase
from constants import *



app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

col = DataBase()

@app.route("/")
def index():
    pizzas = col.findPizzas()
    toppings = col.findToppings()
    return render_template('index.html', pizza_list_from_database=pizzas, topping_list_from_database=toppings)

@app.route("/submit", methods=['POST'])
def submit():
    
    toppingName = request.form.get('topping-name')
    
    # Case where topping already exists
    if col.insertTopping(toppingName) == NAME_ALREADY_EXISTS:
        return 'This topping already exists!', 400 
    return "Topping added successfully!", 200

@app.route("/submitp", methods=['POST'])
def submitP():
    pizzaName = request.form.get('pizza-name')
    res = col.insertPizza(pizzaName, ["Hope", "Pope", "Cope"])
    # Case where topping already exists
    if res == NAME_ALREADY_EXISTS:
        return 'This pizza already exists!', 400
    elif res == TOPPINGS_ALREADY_EXIST:
        return 'That topping combination is already a pizza!', 400
    return "Pizza added successfully!", 200

@app.route("/get-updated-pizza-list")
def get_updated_pizza_list():
    return jsonify(col.findPizzas())

@app.route("/get-updated-topping-list")
def get_updated_topping_list():
    return jsonify(col.findToppings())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)