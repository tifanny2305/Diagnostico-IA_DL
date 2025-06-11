## 🔗 Descarga de modelos

Antes de construir la imagen, debes descargar los siguientes archivos y colocarlos en la carpeta `model/`:

| Archivo                        | Descripción                         | Enlace                                       |
|-------------------------------|-------------------------------------|----------------------------------------------|
| `tiny.pt`                     | Modelo Whisper (ligero)             | [Descargar](https://drive.google.com/drive/folders/1_1_L3cu9cotw6FvmVezbvCoklIYdi1EB?usp=sharing)    |

| `modelo_diagnostico_tf.h5`    | Modelo de predicción de diagnóstico | [Descargar](https://drive.google.com/drive/folders/1_1_L3cu9cotw6FvmVezbvCoklIYdi1EB?usp=sharing)    |

| `clases_diagnostico.npy`      | Clases para decodificar resultado   | [Descargar](https://drive.google.com/drive/folders/1_1_L3cu9cotw6FvmVezbvCoklIYdi1EB?usp=sharing)    |

| `recomendaciones_completas.csv` | Texto del tratamiento sugerido    | [Descargar](https://drive.google.com/drive/folders/1_1_L3cu9cotw6FvmVezbvCoklIYdi1EB?usp=sharing)    |


Colócalos dentro del directorio `model/` antes de construir.

## 🐳 Construcción Docker

```bash
docker build -t diagnostico-ia .
