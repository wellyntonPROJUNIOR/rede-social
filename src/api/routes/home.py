from fastapi import APIRouter
from src.datalayer.models.user import UserModel 
from typing import Annotated
from fastapi import Depends
from src.api.authentication import verify_token


# configuração do fastAPI (no Docs)
router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

# token (wellyntonjoaomartins@gmail.com): vcRx1hsRggfKyr-zRwz0scrbIhU

# rota...
@router.post("/")
async def informations(current_user: Annotated[UserModel, Depends(verify_token)]):
   # obter informações do usuário logado ou redirecionar para o login
   return {'Logado': current_user}
