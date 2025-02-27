from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class GroupsRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("name", "STRING"),
            SchemaField("description", "STRING"),
            SchemaField("created_at", "TIMESTAMP"),
            SchemaField("updated_at", "TIMESTAMP"),
        ]
        super().__init__("groups", schema)

    def save_groups(self, df):
        """Salva grupos no BigQuery."""
        self.save_dataframe(df)
