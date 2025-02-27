from app.clients.endpoints.organizations_client import OrganizationsClient

class OrganizationsService:
    def __init__(self, client: OrganizationsClient):
        self.client = client

    def get_organizations(self):
        return self.client.get_organizations()

    def get_organization_by_id(self, org_id: int):
        return self.client.get_organization(org_id)

    def create_organization(self, organization_data: dict):
        return self.client.create_organization(organization_data)
