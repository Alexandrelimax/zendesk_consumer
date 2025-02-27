from app.services.tickets_service import TicketsService
from app.services.users_service import UsersService
from app.services.organizations_service import OrganizationsService
from app.services.groups_service import GroupsService
from app.services.conversations_service import ConversationsService
from app.services.satisfaction_ratings_service import SatisfactionRatingsService
from app.services.calls_service import CallsService
from app.services.messages_service import MessagesService
from app.services.attachments_service import AttachmentsService
from app.services.account_service import AccountService
from app.dependencies.clients_instancies import (
    get_tickets_client, get_users_client, get_organizations_client,
    get_groups_client, get_conversations_client, get_satisfaction_ratings_client,
    get_calls_client, get_messages_client, get_attachments_client, get_account_client
)

# Criando instâncias dos services
tickets_service = TicketsService(get_tickets_client())
users_service = UsersService(get_users_client())
organizations_service = OrganizationsService(get_organizations_client())
groups_service = GroupsService(get_groups_client())
conversations_service = ConversationsService(get_conversations_client())
satisfaction_ratings_service = SatisfactionRatingsService(get_satisfaction_ratings_client())
calls_service = CallsService(get_calls_client())
messages_service = MessagesService(get_messages_client())
attachments_service = AttachmentsService(get_attachments_client())
account_service = AccountService(get_account_client())

# Funções de injeção para serviços
def get_tickets_service():
    return tickets_service

def get_users_service():
    return users_service

def get_organizations_service():
    return organizations_service

def get_groups_service():
    return groups_service

def get_conversations_service():
    return conversations_service

def get_satisfaction_ratings_service():
    return satisfaction_ratings_service

def get_calls_service():
    return calls_service

def get_messages_service():
    return messages_service

def get_attachments_service():
    return attachments_service

def get_account_service():
    return account_service
