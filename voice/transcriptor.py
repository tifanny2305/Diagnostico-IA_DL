import whisper

def transcribir_audio(archivo_wav):
    print("🔍 Transcribiendo...")

    # Ruta local del modelo guardado
    modelo_local = "model/medium.pt"

    # Cargar el modelo desde archivo directamente
    model = whisper.load_model(modelo_local)

    result = model.transcribe(archivo_wav, language="es")
    texto = result["text"].strip()
    print(f"📝 Texto transcrito: {texto}")
    return texto