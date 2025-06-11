from voice.recorder import grabar_audio
from voice.transcriptor import transcribir_audio
from symtoms.extractor import extraer_datos
import json
import os
import sys

# === Nombre de archivo incremental ===
#base = "audio"
#ext = ".wav"
#i = 1
#while os.path.exists(f"{base}{i}{ext}"):
#    i += 1
#AUDIO_FILE = f"{base}{i}{ext}"

# Paso 1: Grabar (NO usa espera por 'detener', solo graba)
#grabar_audio(AUDIO_FILE)

# === Paso 1: Definir archivo de entrada ===
AUDIO_FILE = sys.argv[1] if len(sys.argv) > 1 else "audio.wav"

if not os.path.exists(AUDIO_FILE):
    print(f"❌ Archivo de audio no encontrado: {AUDIO_FILE}")
    exit(1)

# Paso 2: Transcribir
texto = transcribir_audio(AUDIO_FILE)

# Validar si la transcripción fue razonable
if len(texto.split()) < 5:
    print("❌ Transcripción muy corta o inválida. Intenta grabar nuevamente.")
    exit()

# Paso 3: Extraer datos
historia_clinica = extraer_datos(texto)

# Paso 4: Mostrar resultado
print("\n📋 Historia clínica generada:")
print(json.dumps(historia_clinica, indent=2, ensure_ascii=False))
