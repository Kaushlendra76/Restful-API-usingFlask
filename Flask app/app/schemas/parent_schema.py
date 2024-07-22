from marshmallow import Schema, fields

class ParentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    parent_type = fields.Str(required=True)