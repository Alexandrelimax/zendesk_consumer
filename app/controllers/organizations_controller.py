from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.organizations_service import OrganizationsService
from app.models.organizations_model import Organization
from typing import List

class OrganizationsController(BaseController):
    def __init__(self, service: OrganizationsService):
        self.service = service
        super().__init__(prefix="/organizations")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_organizations, methods=["GET"], response_model=List[Organization])
        self.router.add_api_route("/{org_id}", self.get_organization, methods=["GET"], response_model=Organization)
        self.router.add_api_route("/", self.create_organization, methods=["POST"], response_model=Organization)

    def get_organizations(self) -> List[Organization]:
        return self.service.get_organizations()

    def get_organization(self, org_id: int) -> Organization:
        org = self.service.get_organization_by_id(org_id)
        if not org:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organização não encontrada")
        return org

    def create_organization(self, organization: Organization) -> Organization:
        return self.service.create_organization(organization)
