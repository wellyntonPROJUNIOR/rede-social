from fastapi import HTTPException

# Declaração de status code e erros para erros 
def login_wrong_exception(): # Caso haja algum email ou senha incorretos
    raise HTTPException(status_code=404, detail="Method Not Allowed: email ou senha incorretos")

# Caso algum email já exista
def email_already_exists():
    raise HTTPException(status_code=409, detail="Conflict: Usuário já existe")