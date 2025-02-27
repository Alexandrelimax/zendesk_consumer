class ZendeskAPIException(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        self.detail = response.json().get("error", "Erro desconhecido")
        super().__init__(f"Erro {self.status_code}: {self.detail}")
