import uvicorn
from fastapi import FastAPI
from app.controllers.tickets_controller import TicketsController
from app.controllers.users_controller import UsersController
from app.controllers.organizations_controller import OrganizationsController
from app.controllers.groups_controller import GroupsController
from app.controllers.conversations_controller import ConversationsController
from app.controllers.satisfaction_ratings_controller import SatisfactionRatingsController
from app.controllers.calls_controller import CallsController
from app.controllers.messages_controller import MessagesController
from app.controllers.attachments_controller import AttachmentsController
from app.controllers.account_controller import AccountController
from app.dependencies.services_instancies import (
    get_tickets_service, get_users_service, get_organizations_service,
    get_groups_service, get_conversations_service, get_satisfaction_ratings_service,
    get_calls_service, get_messages_service, get_attachments_service, get_account_service
)

# Criar instância do FastAPI
app = FastAPI()

# Criar instâncias dos controllers usando as dependências injetadas
tickets_controller = TicketsController(get_tickets_service())
users_controller = UsersController(get_users_service())
organizations_controller = OrganizationsController(get_organizations_service())
groups_controller = GroupsController(get_groups_service())
conversations_controller = ConversationsController(get_conversations_service())
satisfaction_ratings_controller = SatisfactionRatingsController(get_satisfaction_ratings_service())
calls_controller = CallsController(get_calls_service())
messages_controller = MessagesController(get_messages_service())
attachments_controller = AttachmentsController(get_attachments_service())
account_controller = AccountController(get_account_service())

# Adicionar rotas
app.include_router(tickets_controller.router)
app.include_router(users_controller.router)
app.include_router(organizations_controller.router)
app.include_router(groups_controller.router)
app.include_router(conversations_controller.router)
app.include_router(satisfaction_ratings_controller.router)
app.include_router(calls_controller.router)
app.include_router(messages_controller.router)
app.include_router(attachments_controller.router)
app.include_router(account_controller.router)

# Rota de teste
@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Zendesk API is running!"}

# Executar o servidor
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
