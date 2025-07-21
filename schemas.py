from marshmallow import Schema , fields


class ExpensesSchema(Schema):
    amount = fields.Float(required=True)
    category = fields.String(required=True)
    description = fields.String(required=False)


class ExpensesUpdateSchema(Schema):
    amount = fields.Float(required=False)
    category = fields.String(required=False)
    description = fields.String(required=False)
