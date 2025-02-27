# Usar uma imagem base leve do Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código da aplicação
COPY . .

# Expor a porta da API
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
