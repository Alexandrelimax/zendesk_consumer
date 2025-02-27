from app.clients.endpoints.tickets_client import TicketsClient
from app.clients.endpoints.users_client import UsersClient
from app.clients.endpoints.organizations_client import OrganizationsClient
from app.clients.endpoints.groups_client import GroupsClient
from app.clients.endpoints.conversations_client import ConversationsClient
from app.clients.endpoints.satisfaction_ratings_client import SatisfactionRatingsClient
from app.clients.endpoints.calls_client import CallsClient
from app.clients.endpoints.messages_client import MessagesClient
from app.clients.endpoints.attachments_client import AttachmentsClient
from app.clients.endpoints.account_client import AccountClient

# Criando instâncias dos clients
tickets_client = TicketsClient()
users_client = UsersClient()
organizations_client = OrganizationsClient()
groups_client = GroupsClient()
conversations_client = ConversationsClient()
satisfaction_ratings_client = SatisfactionRatingsClient()
calls_client = CallsClient()
messages_client = MessagesClient()
attachments_client = AttachmentsClient()
account_client = AccountClient()

# Funções de injeção
def get_tickets_client():
    return tickets_client

def get_users_client():
    return users_client

def get_organizations_client():
    return organizations_client

def get_groups_client():
    return groups_client

def get_conversations_client():
    return conversations_client

def get_satisfaction_ratings_client():
    return satisfaction_ratings_client

def get_calls_client():
    return calls_client

def get_messages_client():
    return messages_client

def get_attachments_client():
    return attachments_client

def get_account_client():
    return account_client
