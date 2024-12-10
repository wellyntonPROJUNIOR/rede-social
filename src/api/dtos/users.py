from pydantic import BaseModel

# configuração básica para registrar usuário
class UserRegistration(BaseModel):
    name: str
    email: str
    password: str

# configuração básica para logar usuário
class UserLogin(BaseModel):
    email: str
    password: str