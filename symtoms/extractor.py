import pandas as pd
import numpy as np
import difflib
from predictor import PredictDiagnostico

def cargar_columnas_sintomas(csv_path):
    df = pd.read_csv(csv_path)
    columnas = list(df.columns)
    columnas.remove("prognosis")
    return columnas

# Cargar diccionario de traducción {sintoma_en: sintoma_es}
def cargar_diccionario_traduccion(path_csv):
    df = pd.read_csv(path_csv)
    return dict(zip(df["sintoma_en"], df["sintoma_es"]))

import difflib

def extraer_vector_sintomas(texto, columnas, diccionario_traduccion):
    vector = np.zeros(len(columnas))
    sintomas_detectados = []

    texto = texto.lower()
    palabras = texto.split()
    sintomas_es = [diccionario_traduccion.get(s, s).lower() for s in columnas]

    # Recorremos el texto con ventanas deslizantes de 2 a 4 palabras
    for n in range(1, 5):
        for i in range(len(palabras) - n + 1):
            fragmento = " ".join(palabras[i:i+n])

            for j, sintoma_es in enumerate(sintomas_es):
                score = difflib.SequenceMatcher(None, fragmento, sintoma_es).ratio()
                if score > 0.8:  # umbral ajustable
                    vector[j] = 1
                    if sintoma_es not in sintomas_detectados:
                        sintomas_detectados.append(sintoma_es)

    return vector.reshape(1, -1), sintomas_detectados


def extraer_datos(texto):
    columnas = cargar_columnas_sintomas("model/dataset_completo_super_fusionado.csv")

    df_trad = pd.read_csv("model/sintomas_traducidos.csv")
    diccionario_traduccion = dict(zip(df_trad['sintoma_en'], df_trad['sintoma_es']))

    vector, sintomas_es = extraer_vector_sintomas(texto, columnas, diccionario_traduccion)

    modelo = PredictDiagnostico(
        "model/modelo_diagnostico_tf.h5",
        "model/clases_diagnostico.npy",
        "model/recomendaciones_completas.csv"
    )

    diagnostico, tratamiento = modelo.predecir(vector)

    return {
        "sintomas": ", ".join(sintomas_es) if sintomas_es else texto.strip(),
        "diagnostico": diagnostico,
        "tratamiento": tratamiento
    }
