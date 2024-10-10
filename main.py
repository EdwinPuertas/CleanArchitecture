# main.py

import typer
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from infrastructure.repositories.user_repository import InMemoryUserRepository
from use_cases.create_user import CreateUserUseCase
from use_cases.update_user import UpdateUserUseCase
from domain.value_objects.email import Email
from interfaces.console import run_console

# Configurar la app de FastAPI
app = FastAPI()

# Configurar Typer para la consola
cli = typer.Typer()

# Configurar repositorios y casos de uso
user_repository = InMemoryUserRepository()
create_user_use_case = CreateUserUseCase(user_repository)
update_user_use_case = UpdateUserUseCase(user_repository)

# Modelos de Pydantic para la API
class CreateUserRequest(BaseModel):
    user_id: int
    name: str
    email: str

class UpdateUserRequest(BaseModel):
    new_email: str

# Rutas de la API
@app.post("/users")
def create_user(request: CreateUserRequest):
    try:
        user = create_user_use_case.execute(
            user_id=request.user_id,
            name=request.name,
            email=request.email
        )
        return {"user_id": user.user_id, "name": user.name, "email": user.email.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/users/{user_id}")
def update_user(user_id: int, request: UpdateUserRequest):
    try:
        updated_user = update_user_use_case.execute(user_id=user_id, new_email=request.new_email)
        return {"user_id": updated_user.user_id, "name": updated_user.name, "email": updated_user.email.email}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_repository.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.user_id, "name": user.name, "email": user.email.email}

# Comando de consola para crear un usuario
@cli.command()
def create_user_console(user_id: int, name: str, email: str):
    try:
        user = create_user_use_case.execute(user_id=user_id, name=name, email=email)
        typer.echo(f"User created: ID={user.user_id}, Name={user.name}, Email={user.email.email}")
    except ValueError as e:
        typer.echo(f"Error: {e}")

# Comando de consola para actualizar el email de un usuario
@cli.command()
def update_user_console(user_id: int, new_email: str):
    try:
        updated_user = update_user_use_case.execute(user_id=user_id, new_email=new_email)
        typer.echo(f"User updated: ID={updated_user.user_id}, New Email={updated_user.email.email}")
    except ValueError as e:
        typer.echo(f"Error: {e}")

if __name__ == "__main__":
    # Iniciar la consola o el servidor API dependiendo del contexto
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "console":
        cli()  # Ejecuta los comandos de la consola
    else:
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
