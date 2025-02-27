from app.clients.zendesk_client import ZendeskClient

class OrganizationsClient(ZendeskClient):
    def get_organizations(self):
        return self.request("GET", "/api/v2/organizations.json")

    def get_organization(self, org_id: int):
        return self.request("GET", f"/api/v2/organizations/{org_id}.json")

    def create_organization(self, organization_data: dict):
        return self.request("POST", "/api/v2/organizations.json", data=organization_data)
