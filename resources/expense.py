from flask_smorest import Blueprint , abort
from flask import request
from flask.views import MethodView
from db import expenses
from uuid import uuid4
from schemas import ExpensesSchema , ExpensesUpdateSchema

blp = Blueprint("Expense" , __name__ , description="Operations on Expense")

@blp.route("/expenses")
class ExpenseListResource(MethodView):
    @blp.response(200,ExpensesSchema(many=True))
    def get(self):
        return { "expenses" : list(expenses.values())} , 200

    @blp.arguments(ExpensesSchema)
    @blp.response(201, ExpensesSchema)
    def post(self , request_data):

        expenses_id = uuid4().hex

        new_expenses = {**request_data ,"expenses_id": expenses_id}
        expenses[expenses_id] = new_expenses

        return {"expenses" : expenses[expenses_id]} , 201


@blp.route("/expenses/<string:expenses_id>")
class ExpenseResource(MethodView):
    @blp.response(200)
    def delete(self ,expenses_id):
        if expenses_id not in expenses:
            abort(400, message="Expenses Id not found")
        del expenses[expenses_id]

        return {"message" : "Expenses deleted successfully"} , 200

    @blp.arguments(ExpensesUpdateSchema)
    @blp.response(200, ExpensesSchema )
    def put(self,request_data, expenses_id):

        if expenses_id not in expenses:
            return {"error" : "Expenses Id not found"} , 404
                    
        expenses[expenses_id].update(request_data)

        return {"expenses" : expenses[expenses_id]} , 200
        


    @blp.response(200 , ExpensesSchema)
    def get(self ,expenses_id):
        if expenses_id not in expenses:
            return {"message" : "Expenses id not found"} , 404
        return {"expenses" : expenses[expenses_id]} , 200