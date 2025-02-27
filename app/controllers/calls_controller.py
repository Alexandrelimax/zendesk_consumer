from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.calls_service import CallsService
from app.models.calls_model import Call
from typing import List

class CallsController(BaseController):
    def __init__(self, service: CallsService):
        self.service = service
        super().__init__(prefix="/calls")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_calls, methods=["GET"], response_model=List[Call])
        self.router.add_api_route("/{call_id}", self.get_call, methods=["GET"], response_model=Call)
        self.router.add_api_route("/", self.create_call, methods=["POST"], response_model=Call)

    def get_calls(self) -> List[Call]:
        return self.service.get_calls()

    def get_call(self, call_id: int) -> Call:
        call = self.service.get_call_by_id(call_id)
        if not call:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chamada não encontrada")
        return call

    def create_call(self, call: Call) -> Call:
        return self.service.create_call(call)
