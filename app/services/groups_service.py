from app.clients.endpoints.groups_client import GroupsClient

class GroupsService:
    def __init__(self, client: GroupsClient):
        self.client = client

    def get_groups(self):
        return self.client.get_groups()

    def get_group_by_id(self, group_id: int):
        return self.client.get_group(group_id)

    def create_group(self, group_data: dict):
        return self.client.create_group(group_data)
