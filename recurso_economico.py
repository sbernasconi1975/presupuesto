# Obtener los recursos según el clasificador económico de 8 dígitos percibido mediante una API de presupuesto abierto
# Detalle de campos del dataset::
    #impacto_presupuestario_anio | impacto_presupuestario_mes | clasificador_economico_8_digitos_id	| clasificador_economico_8_digitos_desc | recurso_ingresado_percibido

curl -X POST \
  ://www.presupuestoabierto.gob.ar/api/v1/recurso \
  -H 'Authorization: 9c5f3fce-8224-4224-ad04-c2c7cfaa9eb6' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Recurso Clasificación económica",
    "columns": [
        "impacto_presupuestario_anio",
        "impacto_presupuestario_mes",
        "clasificador_economico_8_digitos_id",
        "clasificador_economico_8_digitos_desc",
        "recurso_ingresado_percibido"
    ]
}'\
    -o recurso_economico.json
import json
import pandas as pd
from pathlib import Path
from typing import Dict, Any
def load_recurso_economico(file_path: str) -> pd.DataFrame:
    """
    Carga el recurso económico desde un archivo JSON y lo convierte en un DataFrame de pandas.

    :param file_path: Ruta al archivo JSON que contiene los datos del recurso económico.
    :return: DataFrame de pandas con los datos del recurso económico.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    return df



