from fastapi import HTTPException, Header # Importação do FastAPI para colocar status code e mensagens de erro 
from src.datalayer.models.user import UserModel # Importação do UserModel (db)

# função que verifica o token único gerado e, faz validação para o frontEnd
async def verify_token(token: str = Header("Authorization")):
    user = await get_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized token.")
    return user

# função que resgata/define o usuário pelo token e mostra erro se falha
async def get_user_by_token(token):
    try:
        user = await UserModel.get(token=token)
        return user
    except Exception as e:
        print('Fail token_is_valid', e)
        return False