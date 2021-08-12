import speech_recognition as sr
import threading
from pygame import mixer
from gtts import gTTS

from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

def draw_text(text, x, y, color="white"):
	with canvas(device) as draw:
		if len(text) >= 20:
			res = '\n'.join(text[i:i + 20] for i in range(0, len(text), 20))
			draw.text((y, x), res, fill=color)
		else:
			draw.text((y, x), text, fill=color)

mixer.init()
os.system("jack_control start")
os.system("arecord -l")

def speak(audioString):
    mixer.music.unload()
    print("Loading audio")
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    print("SAVED")
    #os.system("mpg321 audio.mp3")
    mixer.music.load('audio.mp3')
    mixer.music.play()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(sr.Microphone())
        print(sr.Recognizer())
        print("Say something!")
        audio = r.listen(source)
        print("Heard")
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

