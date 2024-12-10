
# imports externos
from fastapi import FastAPI
#imports internos
from src.api.configuration import (
    configure_db, 
    configure_routes

)

# inicializa
def create_app():
    app = FastAPI()
    
    # incluir rotas
    configure_routes(app)

    # inicializar db/tortoise (passa pelo configure_db)
    configure_db(app)

    # retorna esse app
    return app
# define app como essa variável
app = create_app()
