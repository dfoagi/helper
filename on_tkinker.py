import threading
import tkinter as tk
import pyaudio
from vosk import Model, KaldiRecognizer


class VoiceRecorder:

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.button = tk.Button(text="mic", font=("Arial", 120, "bold"),
                                command=self.click_handler)
        self.button.pack()
        self.label = tk.Label(text="00:00:00")
        self.label.pack()
        self.recording = False
        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.button.config(fg="black")
        else:
            self.recording = True
            self.button.config(fg="red")
            threading.Thread(target=self.record).start()

    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000,
                            input=True, frames_per_buffer=8192)

        parts = []

        while self.recording:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                parts.append(text[14:-3])

        stream.stop_stream()
        stream.close()
        audio.terminate()

        print(' '.join(parts))


model = Model("vosk-model-small-ru-0.22")
recognizer = KaldiRecognizer(model, 16000)

VoiceRecorder()
