# Primer paso
- gcloud init

# Segundo paso
- gcloud auth application-default login

# Tercer paso
- Verificamos si tenemos activa la API de Vertex AI
- Verificamos si tenemos activa la API de Gemini

# Cuarto paso: Especificamente para este proyecto
- Verificamos si tenemos activa la API de BigQuery

# Quinto paso: Instalamos las librerias o dependencias para este proyecto
- pip install -r requirements.txt

# Sexto paso: Modificamos lo necesario en el módulo "run_sql_query"
- La línea 10 tiene el ID del proyecto de Google.

# Septimo paso: Modificamos el .env
- Cambiar el ID del proyecto de Google.

# Tercer paso: Habilitamos el API de VertexAI
- Lanzamos en la terminal: "adk web --host 0.0.0.0"





# Comandos opcionales.
## Si no te activa la API de VertexAI
- gcloud services enable aiplatform.googleapis.com --project=project-mlops-10-streamlit

## Cuando quiero hacer la parte de Frontend o Desplegar (Deployar) la aplicación
adk api_server --host 0.0.0.0 --port 8000

