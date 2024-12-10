
from src.datalayer.models.user import UserModel 
from src.api.exceptions.user import email_already_exists, login_wrong_exception

class UserService:

    def _init_(self):
        pass

    async def register(self, name: str, email: str, password: str):

        email_exists = await UserModel.filter(email=email)
        if email_exists:
            raise email_already_exists()

        user = await UserModel.create(
            name = name,
            email = email,
            password = password
        )

        return user
    
    async def login(self, email: str, password: str):
        user =  None

        # fazer uma busca no banco de dados por email
        try:
            user = await UserModel.get(email=email)
        except Exception: # se o email não existe, retorna (email, senha incorreto)
            raise login_wrong_exception()
        
        # se existir, verificar se a senha é igual

        # se a senha estiver errada: retorna (email/senha incorreto)
        if user.password != password:
            raise login_wrong_exception()
        # se estiver certa, realiza o login
        return user
    
    async def get_all_users(self):
        return await UserModel.all()