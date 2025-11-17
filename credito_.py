import pandas as pd
import requests

# 1. Configuración
url = "https://www.presupuestoabierto.gob.ar/api/v1/credito"
headers = {
    "Content-Type": "application/json",
    "Authorization": "9c5f3fce-8224-4224-ad04-c2c7cfaa9eb6" 
}
data = {
    "title": "Credito vigente por jurisdiccion",
    "columns": [
        "jurisdiccion_id",
        "jurisdiccion_desc",
        "credito_vigente"
    ]
}

# 2. Solicitud y descarga
print("Consultando API...")
response = requests.post(url, headers=headers, json=data)
response.encoding = 'utf-8-sig'

print("Código de estado:", response.status_code)
print("Contenido recibido:", response.text)

# 3. Procesamiento
if response.status_code == 200: # Verificamos que la respuesta fue exitosa
    resultado = response.json()
    df = pd.DataFrame(resultado)
    
    # 4. Guardado
    archivo = "presupuesto_credito.csv"
    df.to_csv(archivo, index=False) # index=False evita guardar el número de fila
    print(f"¡Éxito! Datos guardados en {archivo}")
    print(df.head())
else:
    print("Hubo un error:", response.status_code)