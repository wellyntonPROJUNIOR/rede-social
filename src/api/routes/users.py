from fastapi import APIRouter, Depends
from typing import Annotated
from src.api.dtos.users import UserRegistration, UserLogin
from src.datalayer.models.user import UserModel 
from src.services.user import UserService

# configuração do FastAPI docs
router = APIRouter(
    prefix="/users",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

# rota para registrar usuário com validação caso já exista algum usuário com aquele email
@router.post("/register")
async def register(
   body: UserRegistration, 
   service: Annotated[UserService, Depends(UserService)]
):

   response = await service.register(body.name, body.email, body.password)
   return {'created': response}


# rota para registrar usuário com validação de senha e email no banco de dados
@router.post("/login")
async def login(
   body: UserLogin, 
   service: Annotated[UserService, Depends(UserService)]
):

   response = await service.login(email=body.email, password=body.password)

   return response
# rota para mostrar os usuários no banco de dados
@router.get("/get_all_users")
async def get_all_users(service: Annotated[UserService, Depends(UserService)]):
   return await service.get_all_users()