from tortoise.models import Model
from tortoise import fields

# model para data de criação de postagem
class ModelBase(Model):
    id = fields.IntField(primary_key=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True) 