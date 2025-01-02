import whisper
import time

model = whisper.load_model(name = "small", download_root = "./models")
time.sleep(5)
result = model.transcribe("ola-mundo.mp3")
time.sleep(5)
print(result)