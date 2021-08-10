import speech_recognition as sr
from time import ctime
import time
import threading
import cv2
import sys
import logging as log
import datetime as dt
import os
import pyjokes
import wikipedia
import requests
from pygame import mixer
from gtts import gTTS

mixer.init()
os.system("jack_control start")
os.system("arecord -l")

def speak(audioString):
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

def weather():
  def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=8de0c1d186a15c6c44a58c73ca31e976&units=metric');
    return res.json();
  def print_weather(result,city):
    w1 = ("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    w2 = ("Wind speed: {} meters per second".format(result['wind']['speed']))
    w3 = ("Weather description: {}".format(result['weather'][0]['description']))
    w = w1 + w2 + w3 

    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    speak(w)
  def main():
    city="Toronto"
    print()
    try:
      query='q='+city;
      w_data=weather_data(query);
      print_weather(w_data, city)
      print()
    except:
      print('City name not found...')

  if __name__=='__main__':
    main()


def jarvis(data):

    if "tell me a joke" in data:
        joke = pyjokes.get_joke()
        speak(joke)

    if "tell me the weather" in data:
        weather()

    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Mr.Tahbahtah, I will show you where " + location + " is.")
        os.system("start https://www.google.nl/maps/place/" + location + "/&amp;")

    if "look up" in data:
        try:
            data = data.split(" ")
            query = data[2]
            speak("Hold on Mr.Tahbahtah, I'll look up " + query)
            wiki_res = wikipedia.summary(query, sentences=2)
            speak(wiki_res)
        except wikipedia.exceptions.PageError:
            print("An error occured, coudn't find anything on: " + query)
            speak("An error occured, coudn't find anything on: " + query)
        
        except requests.exceptions.ConnectionError:
            print("A connection error occured, coudn't find anything on: " + query)
            speak("A connection error occured, coudn't find anything on: " + query)


def EdithEyes():
  import real_time_object_detection
#   cascPath = "haarcascade_frontalface_default.xml"
#   faceCascade = cv2.CascadeClassifier(cascPath)
#   log.basicConfig(filename='webcam.log',level=log.INFO)

#   video_capture = cv2.VideoCapture(0)
#   anterior = 0

#   while True:
#       if not video_capture.isOpened():
#           print('Unable to load camera.')
#           time.sleep(5)
#           pass

#       # Capture frame-by-frame
#       ret, frame = video_capture.read()

#       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#       faces = faceCascade.detectMultiScale(
#           gray,
#           scaleFactor=1.1,
#           minNeighbors=5,
#           minSize=(30, 30)
#       )

#       # Draw a rectangle around the faces
#       for (x, y, w, h) in faces:
#           cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#       if anterior != len(faces):
#           anterior = len(faces)
#           if len(faces) == 0:
#               log.info("faces: 0"+" at "+str(dt.datetime.now()))
#           else:
#               #print ("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
#               log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


#       # Display the resulting frame
#       cv2.imshow('Video', frame)


#       if cv2.waitKey(1) & 0xFF == ord('q'):
#           break

#       # Display the resulting frame
#       cv2.imshow('Video', frame)

#   # When everything is done, release the capture
#   video_capture.release()
#   cv2.destroyAllWindows()

E = threading.Thread(target=EdithEyes)

E.start()

# initialization
time.sleep(2)
speak("Hello Mr.Tahbahtah, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
