from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class OrganizationsRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("name", "STRING"),
            SchemaField("domain_names", "STRING", mode="REPEATED"),
            SchemaField("created_at", "TIMESTAMP"),
        ]
        super().__init__("organizations", schema)

    def save_organizations(self, df):
        """Salva organizações no BigQuery."""
        self.save_dataframe(df)
