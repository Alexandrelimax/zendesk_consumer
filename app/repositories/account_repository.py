from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class AccountRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("name", "STRING"),
            SchemaField("subdomain", "STRING"),
            SchemaField("created_at", "TIMESTAMP"),
        ]
        super().__init__("account", schema)

    def save_account_info(self, df):
        """Salva dados da conta no BigQuery."""
        self.save_dataframe(df)
