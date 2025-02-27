from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class UsersRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("name", "STRING"),
            SchemaField("email", "STRING"),
            SchemaField("role", "STRING"),
            SchemaField("created_at", "TIMESTAMP"),
        ]
        super().__init__("users", schema)

    def save_users(self, df):
        """Salva usuários no BigQuery."""
        self.save_dataframe(df)
