from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from constants import *

class DataBase:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://dbUser:isildur@cluster0.g5hx9yl.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
        self.pizzas = self.client["db"]["pizzas"]
        self.toppings = self.client["db"]["toppings"]

    def clearDB(self):
        self.pizzas.delete_many({})
        self.toppings.delete_many({})
        return SUCCESS

    ### PIZZAS ###
    def insertPizza(self, name, toppings):
        # Check for identical pizzas!
        for pizza in self.pizzas.find({}, {"_id": False}):
            # Check for identical pizza name
            if pizza["name"] == name:
                return NAME_ALREADY_EXISTS
            # Check for identical pizza toppings
            if len(pizza["toppings"]) == len(toppings) and len(set(pizza["toppings"]) & set(toppings))== len(toppings):
                return TOPPINGS_ALREADY_EXIST
        # Insert if no identical pizzas
        else:
            self.pizzas.insert_one({'name' : name, 'toppings' : toppings})
            return SUCCESS
    
    def findPizzas(self):
        # Retrieve list of pizzas
        return list(self.pizzas.find({}, {"_id": False}))

    def removePizza(self, name):
        # Remove pizza from database
        res = self.pizzas.delete_one({'name' : name})
        # Check if pizza not found
        if res.deleted_count == 0:
            return ITEM_NOT_FOUND
        return SUCCESS

    def updatePizzaName(self, oldName, newName):
        # Try to find old pizza
        oldQuery = self.pizzas.find_one({'name' : oldName})
        if not oldQuery:
            return ITEM_NOT_FOUND
        # Search if new name already exists
        for pizza in self.pizzas.find({}, {"_id": False}):
            if pizza["name"] == newName:
                return NAME_ALREADY_EXISTS
        # update pizza
        self.pizzas.update_one(oldQuery, { "$set" : {'name' : newName} })
        return SUCCESS     

    def updatePizzaToppings(self, name, newToppings):
        # Try to find old pizza
        oldQuery = self.pizzas.find_one({'name' : name})
        if not oldQuery:
            return ITEM_NOT_FOUND
        # Search if new toppings already exist
        for pizza in self.pizzas.find({}, {"_id": False}):
            if len(pizza["toppings"]) == len(newToppings) and len(set(pizza["toppings"]) & set(newToppings))== len(newToppings):
                return TOPPINGS_ALREADY_EXIST
        # update pizza
        self.pizzas.update_one(oldQuery, { "$set" : {'toppings' : newToppings} })
        return SUCCESS


    ### TOPPINGS ###
    def insertTopping(self, name):
        # Check for identical toppings
        for topping in self.toppings.find({}, {"_id": False}):
            if topping["name"] == name:
                return NAME_ALREADY_EXISTS
        # Insert if no identical toppigns
        else:
            self.toppings.insert_one({'name' : name})
            return SUCCESS
    
    def findToppings(self):
        # Retrieve list of toppings
        return list(self.toppings.find({}, {"_id": False}))
    
    def removeTopping(self, name):
        # Remove pizza from database
        res = self.toppings.delete_one({'name' : name})
        # Check if pizza not found
        if res.deleted_count == 0:
            return ITEM_NOT_FOUND
        return SUCCESS
    
    def updateToppingName(self, oldName, newName):
        # Try to find old topping
        oldQuery = self.toppings.find_one({'name' : oldName})
        if not oldQuery:
            return ITEM_NOT_FOUND
        # Search if new name already exists
        for topping in self.toppings.find({}, {"_id": False}):
            if topping["name"] == newName:
                return NAME_ALREADY_EXISTS
        # update topping
        self.toppings.update_one(oldQuery, { "$set" : {'name' : newName} })
        return SUCCESS