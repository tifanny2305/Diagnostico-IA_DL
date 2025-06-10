import threading
import pvporcupine
import whisper
import numpy as np
import sounddevice as sd
import queue
import struct

ACCESS_KEY = "+XOhplB3ti5VzaQujyTysINehby7kOQZY1p36VU+wLTwWzf5yoL5bA=="
KEYWORD_PATH = "voice/detener_es_windows_v3_0_0.ppn"
MODEL_PATH = "voice/porcupine_params_es.pv"
SAMPLERATE = 16000
FRAMES = 512

model = whisper.load_model("base")
audio_queue = queue.Queue()

def grabar_con_transcripcion():
    print("🎙️ Grabando... Diga 'detener' para finalizar.")
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[KEYWORD_PATH],
        model_path=MODEL_PATH
    )

    parar = threading.Event()
    audio_buffer = []

    def audio_callback(indata, frames, time, status):
        if status:
            print("⚠️", status)
        audio_queue.put(indata.copy())

    def detectar_comando():
        while not parar.is_set():
            audio = audio_queue.get()
            pcm = (audio * 32767).astype(np.int16).flatten()
            result = porcupine.process(pcm.tolist())
            if result >= 0:
                print("🛑 Comando 'detener' detectado.")
                parar.set()

    def acumular_audio():
        while not parar.is_set():
            try:
                chunk = audio_queue.get(timeout=1)
                audio_buffer.append(chunk)
            except queue.Empty:
                continue

    with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLERATE, blocksize=FRAMES):
        t1 = threading.Thread(target=detectar_comando)
        t2 = threading.Thread(target=acumular_audio)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    porcupine.delete()

    # Concatenar y guardar como archivo WAV temporal
    final_audio = np.concatenate(audio_buffer, axis=0)
    from scipy.io.wavfile import write
    write("audio.wav", SAMPLERATE, final_audio.astype(np.float32))

    # Transcribir con Whisper
    print("🔍 Transcribiendo...")
    result = model.transcribe("audio.wav", language="es")
    texto = result["text"].strip()
    print(f"📝 Texto transcrito: {texto}")
    return texto
