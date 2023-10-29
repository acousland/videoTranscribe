import whisper

from pydub import AudioSegment
import os

inputFile = "/Users/acousland/Downloads/input.mp4"

# Load the video file
video = AudioSegment.from_file(inputFile, format="mp4")
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
audio.export("audio.wav", format="wav")

#model = whisper.load_model("base")
model = whisper.load_model("large-v2")
result = model.transcribe("audio.wav")
print(result["text"])

with open('output.txt', 'w') as f:
    f.write(str(inputFile) + "/n /n")
    f.write(result["text"])