import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

class PredictDiagnostico:
    def __init__(self, ruta_modelo, ruta_clases, ruta_recomendaciones):
        self.modelo = load_model(ruta_modelo)
        self.clases = np.load(ruta_clases, allow_pickle=True)
        self.recomendaciones = pd.read_csv(ruta_recomendaciones)
        self.traducciones = pd.read_csv("model/enfermedades_traducidas.csv")

    def predecir(self, vector_sintomas):
        pred = self.modelo.predict(vector_sintomas)
        indice = np.argmax(pred)
        diagnostico_ingles = self.clases[indice]

        # Buscar diagnóstico traducido usando la columna correcta: 'Unnamed: 0'
        traduccion = self.traducciones.loc[
            self.traducciones['Unnamed: 0'] == diagnostico_ingles, 'Enfermedad_español'
        ]
        diagnostico = traduccion.values[0] if not traduccion.empty else diagnostico_ingles

        try:
            recomendacion = self.recomendaciones.loc[
                self.recomendaciones['Unnamed: 0'] == diagnostico_ingles,
                'Recomendacion_español'
            ].values[0]
        except:
            recomendacion = "Sin recomendación disponible."

        return diagnostico, recomendacion


