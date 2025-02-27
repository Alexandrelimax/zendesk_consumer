from app.clients.zendesk_client import ZendeskClient

class GroupsClient(ZendeskClient):
    def get_groups(self):
        return self.request("GET", "/api/v2/groups.json")

    def get_group(self, group_id: int):
        return self.request("GET", f"/api/v2/groups/{group_id}.json")

    def create_group(self, group_data: dict):
        return self.request("POST", "/api/v2/groups.json", data=group_data)
