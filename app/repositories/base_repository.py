from google.cloud import bigquery
from google.cloud.bigquery import SchemaField  # Importando diretamente

class BaseRepository:
    def __init__(self, table_name, schema):
        self.client = bigquery.Client()
        self.dataset = "zendesk_raw"
        self.table_name = table_name
        self.schema = schema  # O schema agora é um atributo da classe

    def save_dataframe(self, df):
        """Salva um DataFrame pandas no BigQuery com schema definido."""
        if df.empty:
            print(f"⚠️ Nenhum dado para salvar na tabela {self.table_name}")
            return

        table_id = f"{self.client.project}.{self.dataset}.{self.table_name}"

        # Configuração do job de carregamento
        job_config = bigquery.LoadJobConfig(
            schema=self.schema,
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  # Mantém os dados existentes
        )

        # Carrega os dados para o BigQuery
        job = self.client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result()

        print(f"✅ {len(df)} registros salvos na tabela {self.table_name} no BigQuery.")
