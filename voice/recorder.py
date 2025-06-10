import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

SAMPLERATE = 16000
DURACION = 20  # Puedes cambiarlo

def grabar_audio(nombre_archivo="audio.wav"):
    print(f"🎙️ Grabando durante {DURACION} segundos...")
    audio = sd.rec(int(DURACION * SAMPLERATE), samplerate=SAMPLERATE, channels=1)
    sd.wait()
    write(nombre_archivo, SAMPLERATE, audio.astype(np.float32))
    print(f"💾 Audio guardado como {nombre_archivo}")
