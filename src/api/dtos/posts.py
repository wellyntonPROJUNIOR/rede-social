from pydantic import BaseModel

# configuração básica para registrar usuário
class PostCreation(BaseModel):
    message: str