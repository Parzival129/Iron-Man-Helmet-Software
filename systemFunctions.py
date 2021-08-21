import speech_recognition as sr
import threading
import os
from pygame import mixer
from gtts import gTTS

# FOR OLED
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306

# FOR LED
import RPi.GPIO as GPIO
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

mixer.init()
os.system("jack_control start")
os.system("arecord -l")

_activateJarvis = True

def jarvisActivated () :
    return _activateJarvis

def draw_text(text, x=0, y=0, color="white"):
    print(text)
    with canvas(device) as draw:
                if len(text) >= 20:
                        res = '\n'.join(text[i:i + 20] for i in range(0, len(text), 20))
                        draw.text((y, x), res, fill=color)

                else:
                        draw.text((y, x), text, fill=color)
def hide():
    device.hide()

def show():
    device.show()

def speak(audioString):
    # Unloads any audio before speaking
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

        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)

        #draw_text(">")
        audio = r.listen(source)

        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.4)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.8)

        print("Heard")
        #draw_text("Recieved")
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        
        data = r.recognize_google(audio)
        print("You said: " + data)
        #draw_text("Recieved: {}".format(data))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

def turnOffJarvis() :
    global _activateJarvis
    _activateJarvis = False
    speak("Jarvis deactivated")

def turnOnJarvis() :
    global _activateJarvis
    _activateJarvis = True
    speak("Jarvis activated")

