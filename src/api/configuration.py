from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.api.routes import users
from src.api.routes import home
from src.api.routes import post


# configuração para o FastAPI (rotas)
def configure_routes(app: FastAPI):
    app.include_router(users.router)
    app.include_router(home.router)
    app.include_router(post.router)

# recebe o app
def configure_db(app: FastAPI):
    register_tortoise(
        # passa o app no register_tortoise
        app=app,
        config={

            # inicializa as informações do banco de dados
            'connections': {
              # faz a conexão com o banco de dados  
                # 'default': 'postgres://postgres:qwerty123@localhost:5432/events'
                 'default': 'sqlite://db.sqlite3'
            },

            'apps': {
            'models': {
                'models': [
                    'src.datalayer.models.user',
                    'src.datalayer.models.post'
                ],
                'default_connection': 'default',
            }
        }

        },
        generate_schemas=True,
        add_exception_handlers=True,
    )
