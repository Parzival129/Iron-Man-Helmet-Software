import pyjokes
import requests
import wikipedia
import os
from time import ctime
from systemFunctions import speak, draw_text
from weatherApp import weather

# Returns none if command isn't to be found
def getCommandParameters(rawSpeech, commandToFind, maxParameterWordLength = 2) :
    try :
        commandParametersAndGibberish = rawSpeech.split(commandToFind)[1].strip().split(' ')
        parameter = ' '.join(commandParametersAndGibberish[0 : maxParameterWordLength])
        return parameter if parameter else None
    
    except IndexError :
        return None

def askJarvis(rawQuery):
    if "tell me a joke" in rawQuery :
        joke = pyjokes.get_joke()
        draw_text(joke, 0, 0)
        speak(joke)
        return
    
    if "tell me the weather" in rawQuery :
        weather()
        return

    if "how are you" in rawQuery:
        speak("I am fine")
        return

    if "what time is it" in rawQuery:
        draw_text(str(ctime()), 0, 0)
        speak(ctime())
        return
    
    query = getCommandParameters(rawQuery, "where is", 2)
    if query != None:
        location = query
        speak("Hold on Sir, I will show you where " + location + " is.")
        os.system("start https://www.google.nl/maps/place/" + location + "/&amp;")
        return
    
    query = getCommandParameters(rawQuery, "look up", 2)
    if query != None:
        try:
            speak("Hold on Sir, I'll look up " + query)
            wiki_res = wikipedia.summary(query, sentences=2)
            draw_text(wikipedia.summary(query, sentences=1), 0, 0)
            speak(wiki_res)
        except wikipedia.exceptions.PageError:
            print("An error occured, coudn't find anything on: " + query)
            speak("An error occured, coudn't find anything on: " + query)
        except requests.exceptions.ConnectionError:
            print("A connection error occured, coudn't find anything on: " + query)
            speak("A connection error occured, coudn't find anything on: " + query)


