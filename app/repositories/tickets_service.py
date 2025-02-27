from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField  # Importando diretamente

class TicketsRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("subject", "STRING"),
            SchemaField("description", "STRING"),
            SchemaField("status", "STRING"),
            SchemaField("priority", "STRING"),
            SchemaField("created_at", "TIMESTAMP"),
            SchemaField("updated_at", "TIMESTAMP"),
        ]
        super().__init__("tickets", schema)  # Passamos o nome da tabela e o schema

    def save_tickets(self, df):
        """Salva tickets no BigQuery."""
        self.save_dataframe(df)
