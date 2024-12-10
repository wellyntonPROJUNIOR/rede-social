from tortoise.models import Model
from tortoise import fields
import secrets
from src.datalayer.models.base import ModelBase

# função para gerar token (token é a session de tudo e, este, como é um token único não é muito bom utilizar, mas, é o que temos)
def generate_token():
    return secrets.token_urlsafe(20)

# configurações da db
class UserModel(ModelBase):
    name = fields.CharField(max_length=240)
    email = fields.CharField(max_length=240, unique=True)
    password = fields.TextField()
    token = fields.TextField(default=generate_token) # chama a função de gerar token único para cada usuário