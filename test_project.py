# Make sure the page is loading
def test_home(client):
    response = client.get("/")
    print(response.data)
    assert b"<title>Pizza Shop!</title>" in response.data

#### TEST TOPPINGS #####

# Test adding a valid topping
def test_valid_topping_addition(client):
    response = client.post("/add-topping", data={"topping-name" : "Pepperoni"})
    assert response.status_code == 200
    # Remove added topping from the database
    client.post("/remove-topping", data={"topping-name" : "Pepperoni"})

# Test adding a duplicate topping
def test_duplicate_topping_addition(client):
    client.post("/add-topping", data={"topping-name" : "Mushrooms"})
    response = client.post("/add-topping", data={"topping-name" : "Mushrooms"})
    assert response.status_code == 400
    # Remove added topping from the database
    client.post("/remove-topping", data={"topping-name" : "Mushrooms"})

# Test removing a valid topping
def test_valid_topping_removal(client):
    client.post("/add-topping", data={"topping-name" : "Olives"})
    response = client.post("/remove-topping", data={"topping-name" : "Olives"})
    assert response.status_code == 200

# Test removing a nonexistent topping
def test_nonexistent_topping_removal(client):
    response = client.post("/remove-topping", data={"topping-name" : "Black Olives"})
    assert response.status_code == 400

# Test valid update of a topping
def test_valid_topping_update(client):
    #Add a topping
    response = client.post("/add-topping", data={"topping-name" : "Double Cheese"})
    assert response.status_code == 200
    #Update the added topping
    response = client.post("/update-topping", data={"old-topping-name" : "Double Cheese", "new-topping-name" : "Triple Cheese"})
    assert response.status_code == 200
    #Remove added topping from DB
    client.post("/remove-topping", data={"topping-name" : "Triple Cheese"})

# Test updating nonexisting topping
def test_nonexistent_topping_update(client):
    response = client.post("/update-topping", data={"old-topping-name" : "Xtra Cheese", "new-topping-name" : "Triple Cheese"})
    assert response.status_code == 400

# Test updating duplicate topping
def test_duplicate_topping_update(client):
    #add a topping
    client.post("/add-topping", data={"topping-name" : "Quadrouple Cheese"})
    #update to existing topping 
    response = client.post("/update-topping", data={"old-topping-name" : "Quadrouple Cheese", "new-topping-name" : "Quadrouple Cheese"})
    assert response.status_code == 400
    #Remove added topping from DB
    client.post("/remove-topping", data={"topping-name" : "Quadrouple Cheese"})

#### TEST PIZZAS #####

# Test adding a valid pizza
def test_valid_pizza_addition(client):
    #add a topping for the pizza
    client.post("/add-topping", data={"topping-name" : "Anchovies"})
    #add a valid pizza
    response = client.post("/add-pizza", data={"pizza-name" : "Anchovie Pizza", "toppings" : ["Anchovies"]})
    assert response.status_code == 200
    #remove the pizza and toppings
    client.post("/remove-pizza", data={"pizza-name" : "Anchovie Pizza"})
    client.post("/remove-topping", data={"topping-name" : "Anchovies"})

# Test adding a duplicate pizza
def test_duplicate_duplicate_addition(client):
    #add a topping for the pizza
    client.post("/add-topping", data={"topping-name" : "Pineapple"})
    #add a valid pizza
    client.post("/add-pizza", data={"pizza-name" : "Pineapple Pizza", "toppings" : ["Pineapple"]})
    #add duplicate pizza
    response = client.post("/add-pizza", data={"pizza-name" : "Pineapple Pizza", "toppings" : []})
    assert response.status_code == 400
    #remove the pizza and toppings
    client.post("/remove-pizza", data={"pizza-name" : "Pineapple Pizza"})
    client.post("/remove-topping", data={"topping-name" : "Pineapple"})

# Test adding a pizza with existing toppings
def test_existing_toppings_pizza(client):
    #add a topping for the pizza
    client.post("/add-topping", data={"topping-name" : "Italian Sausage"})
    #add a valid pizza
    client.post("/add-pizza", data={"pizza-name" : "Italian Pizza", "toppings" : ["Italian Sausage"]})
    #add pizza with different name and same toppings
    response = client.post("/add-pizza", data={"pizza-name" : "Italian Sausage Pizza", "toppings" : ["Italian Sausage"]})
    assert response.status_code == 400
    #remove the pizza and toppings
    client.post("/remove-pizza", data={"pizza-name" : "Italian Pizza"})
    client.post("/remove-topping", data={"topping-name" : "Italian Sausage"})

# Test remove a valid pizza
def test_valid_pizza_removal(client):
    #add a valid pizza
    client.post("/add-pizza", data={"pizza-name" : "Cheese Pizza", "toppings" : []})
    #remove the pizza
    response = client.post("/remove-pizza", data={"pizza-name" : "Cheese Pizza"})
    assert response.status_code == 200

# Test remove nonexistent pizza
def test_nonexistent_pizza_removal(client):
    #remove invalid pizza
    response = client.post("/remove-pizza", data={"pizza-name" : "Nonexistent Pizza"})
    assert response.status_code == 400

# Test valid update of pizza name
def test_valid_pizza_name_update(client):
    #Add a topping and pizza
    client.post("/add-topping", data={"topping-name" : "Ham"})
    client.post("/add-pizza", data={"pizza-name" : "Hamm Pizza", "toppings" : ["Ham"]})
    #Perform update
    response = client.post("/update-pizza-name", data={"old-pizza-name" : "Hamm Pizza", "new-pizza-name" : "Ham Pizza"})
    assert response.status_code == 200
    #Remove topping and pizza
    client.post("/remove-pizza", data={"pizza-name" : "Ham Pizza"})
    client.post("/remove-topping", data={"topping-name" : "Ham"})

# Test updating name of nonexistent pizza
def test_nonexistent_pizza_name_update(client):
    #Perform update
    response = client.post("/update-pizza-name", data={"old-pizza-name" : "Nonexistent Pizza", "new-pizza-name" : ""})
    assert response.status_code == 400

# Test updating name to existing pizza name
def test_duplicate_pizza_name_update(client):
    #Add a pizza
    client.post("/add-pizza", data={"pizza-name" : "Existing Pizza", "toppings" : []})
    #Update the pizza to an existing one
    response = client.post("/update-pizza-name", data={"old-pizza-name" : "Existing Pizza", "new-pizza-name" : "Existing Pizza"})
    assert response.status_code == 400
    #Remove the pizza
    client.post("/remove-pizza", data={"pizza-name" : "Existing Pizza"})

# Test valid pizza topping update
def test_valid_pizza_topping_update(client):
    #Add a topping and pizza
    client.post("/add-topping", data={"topping-name" : "Spicy Pepperoni"})
    client.post("/add-pizza", data={"pizza-name" : "Spicy Pepperoni Pizza", "toppings" : []})
    #Update the pizza toppings
    response = client.post("/update-pizza-toppings", data={"pizza-name" : "Spicy Pepperoni Pizza", "toppings" : ["Spicy Pepperoni"]})
    assert response.status_code == 200
    #Remove the pizza and topping
    client.post("/remove-pizza", data={"pizza-name" : "Spicy Pepperoni Pizza"})
    client.post("/remove-topping", data={"topping-name" : "Spicy Pepperoni"})

# Test nonexistent pizza topping update
def test_nonexistent_pizza_topping_update(client):
    #Perform update
    response = client.post("/update-pizza-name", data={"pizza-name" : "Nonexistent Pizza", "toppings" : []})
    assert response.status_code == 400

# Test duplicate pizza topping update
def test_duplicate_pizza_topping_update(client):
    # Add a topping and pizza
    client.post("/add-topping", data={"topping-name" : "Onions"})
    client.post("/add-pizza", data={"pizza-name" : "Onion Pizza", "toppings" : ["Onions"]})
    # Update the pizza toppings
    response = client.post("/update-pizza-toppings", data={"pizza-name" : "Onion Pizza", "toppings" : ["Onions"]})
    assert response.status_code == 400
    #Remove the pizza and topping
    client.post("/remove-pizza", data={"pizza-name" : "Onion Pizza"})
    client.post("/remove-topping", data={"topping-name" : "Onions"})