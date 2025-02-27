from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.groups_service import GroupsService
from app.models.groups_model import Group
from typing import List

class GroupsController(BaseController):
    def __init__(self, service: GroupsService):
        self.service = service
        super().__init__(prefix="/groups")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_groups, methods=["GET"], response_model=List[Group])
        self.router.add_api_route("/{group_id}", self.get_group, methods=["GET"], response_model=Group)
        self.router.add_api_route("/", self.create_group, methods=["POST"], response_model=Group)

    def get_groups(self) -> List[Group]:
        return self.service.get_groups()

    def get_group(self, group_id: int) -> Group:
        group = self.service.get_group_by_id(group_id)
        if not group:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grupo não encontrado")
        return group

    def create_group(self, group: Group) -> Group:
        return self.service.create_group(group)
