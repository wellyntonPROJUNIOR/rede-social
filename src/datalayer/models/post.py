import secrets
from tortoise.models import Model
from tortoise import fields
from src.datalayer.models.base import ModelBase

# configurações da db (para posts)
class PostModel(ModelBase):
    user = fields.ForeignKeyField('models.UserModel', related_name='posts')
    message = fields.TextField()
    