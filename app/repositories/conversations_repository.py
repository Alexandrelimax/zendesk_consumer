from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class ConversationsRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("subject", "STRING"),
            SchemaField("created_at", "TIMESTAMP"),
            SchemaField("updated_at", "TIMESTAMP"),
            SchemaField("status", "STRING"),
            SchemaField("priority", "STRING"),
        ]
        super().__init__("conversations", schema)

    def save_conversations(self, df):
        """Salva conversas no BigQuery."""
        self.save_dataframe(df)
