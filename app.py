from flask import Flask, request
from db import expenses
from uuid import uuid4

app = Flask(__name__)

@app.get("/expenses")
def getAllExpense():
    return { "expenses" : list(expenses.values())} , 200


@app.get("/expenses/<expenses_id>")
def get_one_expense(expenses_id):
    if expenses_id not in expenses:
        return {"message" : "Expenses id not found"} , 400
    return {"expenses" : expenses[expenses_id]} , 200



@app.post("/expenses")
def create_one_expense():
    request_data = request.get_json()
    expenses_id = uuid4().hex

    allowed_list = ["amount" , "category" , "description"]

    for key in allowed_list:
        if key not in request_data:
            return {"error": f"{key} is required."}, 400

    for key in request_data:
        if key not in allowed_list:
            return {"error" : f"The {key} key is not allowed"} , 400

    new_expenses = {**request_data ,"expenses_id": expenses_id}
    expenses[expenses_id] = new_expenses

    return {"expenses" : expenses[expenses_id]} , 201


@app.delete("/expenses/<expenses_id>")
def delete_one_expenses(expenses_id):
    if expenses_id not in expenses:
        return {"error" : "Expenses id not found"} , 400
    del expenses[expenses_id]

    return {"message" : "Expenses deleted successfully"} , 200


@app.put("/expenses/<expenses_id>")
def edit_one_expenses(expenses_id):
    request_data = request.get_json()

    if expenses_id not in expenses:
        return {"error" : "Expenses Id not found"} , 400
    
    allowed_list = ["amount" , "category" , "description"]

    for key in request_data:
        if key not in allowed_list:
            return {"error" : f"The {key} key is not allowed"} , 400
        
    expenses[expenses_id].update(request_data)

    return {"expenses" : expenses[expenses_id]} , 200
    












