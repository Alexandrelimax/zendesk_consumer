from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class CallsRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("user_id", "INTEGER"),
            SchemaField("duration_seconds", "INTEGER"),
            SchemaField("status", "STRING"),
            SchemaField("created_at", "TIMESTAMP"),
        ]
        super().__init__("calls", schema)

    def save_calls(self, df):
        """Salva chamadas no BigQuery."""
        self.save_dataframe(df)
