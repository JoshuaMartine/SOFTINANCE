import pyaudio
import numpy as np
import tkinter as tk

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def audio_visualizer():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    root = tk.Tk()
    root.geometry("400x300")  # Ajusta el tamaño de la ventana
    canvas = tk.Canvas(root, width=400, height=300, bg="black")  # Fondo negro
    canvas.pack()

    bars = []
    bar_height = 500  # Altura de las barras
    for i in range(6):
        bar = canvas.create_rectangle(50 + i * 60, 150, 80 + i * 60, 150, fill="white", outline="")
        bars.append(bar)

    def update_visualizer():
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        fft_data = np.fft.rfft(data)
        magnitude = np.abs(fft_data)[:len(bars)] * 2 / (32768 * CHUNK)
        
        for i, bar in enumerate(bars):
            canvas.coords(bar, 50 + i * 60, 150 - magnitude[i] * bar_height, 80 + i * 60, 150 + magnitude[i] * bar_height)

        root.after(10, update_visualizer)

    update_visualizer()
    root.mainloop()

audio_visualizer()
