#speech to text module

from vosk import Model, KaldiRecognizer
import pyaudio
import keyboard

model = Model("vosk-model-small-ru-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)

# while True:
#     question = []
#     while keyboard.read_key() == "q":
#         data = stream.read(4096, exception_on_overflow=False)
#         if recognizer.AcceptWaveform(data):
#             text = recognizer.Result()
#             question.append(text[14:-3])
#             print(question)
#     if question:
#         print(' '.join(question))
#         question = []