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

@app.route("/add-topping", methods=['POST'])
def addTopping():
    toppingName = request.form.get('topping-name')
    
    # Case where topping already exists
    if col.insertTopping(toppingName) == NAME_ALREADY_EXISTS:
        return 'This topping already exists!', 400 
    return "Topping added successfully!", 200

@app.route('/remove-topping', methods=['POST'])
def removeTopping():
    toppingName = request.form.get('topping-name')

    # Case where topping isn't found
    if col.removeTopping(toppingName) == ITEM_NOT_FOUND:
        return 'The topping wasn\'t found!', 400 
    return "Topping removed successfully!", 200

@app.route('/update-topping', methods=['POST'])
def updateTopping():
    oldToppingName = request.form.get('old-topping-name')
    newToppingName = request.form.get('new-topping-name')
    res = col.updateToppingName(oldToppingName, newToppingName)
    # Case where topping isn't found
    if res == ITEM_NOT_FOUND:
        return 'The topping wasn\'t found!', 400 
    elif res == NAME_ALREADY_EXISTS:
        return 'This topping already exists!', 400
    return "Topping updated successfully!", 200

@app.route("/add-pizza", methods=['POST'])
def addPizza():
    pizzaName = request.form.get('pizza-name')
    selectedToppings = request.form.getlist('toppings')
    # Case where no toppings
    res = None
    if not selectedToppings:
        res = col.insertPizza(pizzaName, ['None'])
    else:
        res = col.insertPizza(pizzaName, selectedToppings)

    # Case where pizza name already exists
    if res == NAME_ALREADY_EXISTS:
        return 'This pizza already exists!', 400
    # Case where pizza toppings already exist
    elif res == TOPPINGS_ALREADY_EXIST:
        return 'That topping combination is already a pizza!', 400
    return "Pizza added successfully!", 200

@app.route("/remove-pizza", methods=['POST'])
def removePizza():
    pizzaName = request.form.get('pizza-name')
    # Case where pizza wasn't found
    if col.removePizza(pizzaName) == ITEM_NOT_FOUND:
        return 'The pizza wasn\'t found!', 400
    else:
        return 'Pizza removed successfully', 200
    
@app.route('/update-pizza-name', methods=['POST'])
def updatePizzaName():
    oldPizzaName = request.form.get('old-pizza-name')
    newPizzaName = request.form.get('new-pizza-name')
    res = col.updatePizzaName(oldPizzaName, newPizzaName)
    # Case where pizza wasn't found
    if res == ITEM_NOT_FOUND:
        return 'The pizza wasn\'t found!', 400
    # Case where pizza already exists
    elif res == NAME_ALREADY_EXISTS:
        return 'This pizza already exists!', 400
    return "Pizza updated successfully!", 200

@app.route('/update-pizza-toppings', methods=['POST'])
def updatePizzaToppings():
    pizzaName = request.form.get('pizza-name')
    selectedToppings = request.form.getlist('toppings')
    res = col.updatePizzaToppings(pizzaName, selectedToppings)
    # Case where pizza wasn't found
    if res == ITEM_NOT_FOUND:
        return 'The pizza wasn\'t found!', 400
    # Case where toppings already exist
    elif res == TOPPINGS_ALREADY_EXIST:
        return 'That topping combination is already a pizza!', 400
    return "Pizza toppings updated successfully!", 200


@app.route("/get-updated-pizza-list")
def get_updated_pizza_list():
    return jsonify(col.findPizzas())

@app.route("/get-updated-topping-list")
def get_updated_topping_list():
    return jsonify(col.findToppings())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)