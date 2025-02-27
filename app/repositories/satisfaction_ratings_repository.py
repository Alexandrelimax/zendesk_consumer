from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class SatisfactionRatingsRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("score", "STRING"),
            SchemaField("comment", "STRING"),
            SchemaField("ticket_id", "INTEGER"),
            SchemaField("user_id", "INTEGER"),
            SchemaField("created_at", "TIMESTAMP"),
        ]
        super().__init__("satisfaction_ratings", schema)

    def save_ratings(self, df):
        """Salva avaliações de satisfação no BigQuery."""
        self.save_dataframe(df)
