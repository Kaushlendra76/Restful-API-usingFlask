from marshmallow import Schema, fields

class ChildSchema(Schema):
    id = fields.Int(dump_only=True)
    parent_id = fields.Int(required=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)