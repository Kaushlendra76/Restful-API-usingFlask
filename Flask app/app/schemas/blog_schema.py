from marshmallow import Schema, fields

class BlogSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    age_group = fields.Str(required=True)
    gender = fields.Str(required=False)
    vlog_url = fields.Str(required=False)
    location = fields.Str(required=False)
    interest = fields.Str(required=False)  