from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.account_service import AccountService
from app.models.account_model import Account
from typing import List

class AccountController(BaseController):
    def __init__(self, service: AccountService):
        self.service = service
        super().__init__(prefix="/account")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_accounts, methods=["GET"], response_model=List[Account])
        self.router.add_api_route("/{account_id}", self.get_account, methods=["GET"], response_model=Account)
        self.router.add_api_route("/", self.create_account, methods=["POST"], response_model=Account)

    def get_accounts(self) -> List[Account]:
        return self.service.get_accounts()

    def get_account(self, account_id: int) -> Account:
        account = self.service.get_account_by_id(account_id)
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada")
        return account

    def create_account(self, account: Account) -> Account:
        return self.service.create_account(account)
