import sys
import pyjokes
import requests
import wikipedia
import os
import systemFunctions
from applets import appRunning, startApplet, getNameOfRunningApplet, turnOffRunningApplet
from time import ctime
from random import randint
from weatherApp import weather

import time

# Returns none if command isn't to be found
def getCommandParameters(rawSpeech, commandToFind, maxParameterWordLength = 2) :
    try :
        commandParametersAndGibberish = rawSpeech.split(commandToFind)[1].strip().split(' ')
        parameter = ' '.join(commandParametersAndGibberish[0 : maxParameterWordLength])
        return parameter if parameter else None
    
    except IndexError :
        return None

def askJarvis(rawQuery):
    rawQuery = rawQuery.lower()

    if "tell me a joke" in rawQuery :
        joke = pyjokes.get_joke()
        systemFunctions.draw_text(joke, 0, 0)
        systemFunctions.speak(joke)
        return
    
    if "tell me the weather" in rawQuery :
        weather()
        return

    if "how are you" in rawQuery:
        answer = ['I am fine', 'I am great!', 'I am in a crippling deppression.'][randint (0, 2)]
        systemFunctions.draw_text(answer)
        systemFunctions.speak(answer)
        return

    if "what time is it" in rawQuery:
        systemFunctions.draw_text(str(ctime()), 0, 0)
        systemFunctions.speak(ctime())
        return
    
    query = getCommandParameters(rawQuery, "start", 2)
    if query != None :
        if appRunning() :
            systemFunctions.speak("Applet already running")
            return
        response = startApplet(query)
        if (response == "failed") :
            systemFunctions.speak('Could not find applet')
            return
        systemFunctions.speak('Starting {}'.format(query))


    query = getCommandParameters(rawQuery, "stop running", 2)
    if query != None :
        response = turnOffRunningApplet(query)
        if (response == "failed") :
            systemFunctions.speak('Could not close applet {}'.format(query))
            return
        systemFunctions.speak('Terminated applet')

    query = getCommandParameters(rawQuery, "where is", 2)
    if query != None:
        location = query
        systemFunctions.speak("Hold on Sir, I will show you where " + location + " is.")
        os.system("start https://www.google.nl/maps/place/" + location + "/&amp;")
        return

    query = getCommandParameters(rawQuery, "look up", 2)
    if query != None:
        try:
            systemFunctions.speak("Hold on Sir, I'll look up " + query)
            query = '+'.join(query.split())
            wiki_res = wikipedia.summary(query, sentences=2)
            systemFunctions.draw_text(wikipedia.summary(query, sentences=1), 0, 0)
            systemFunctions.speak(wiki_res)
        except wikipedia.exceptions.PageError:
            print("An error occured, coudn't find anything on: " + query)
            systemFunctions.speak("An error occured, coudn't find anything on: " + query)
        except requests.exceptions.ConnectionError:
            print("A connection error occured, coudn't find anything on: " + query)
            systemFunctions.speak("A connection error occured, coudn't find anything on: " + query)
        except wikipedia.exceptions.DisambiguationError:
            print("Please specify. \"{}\" may refer to many things.".format(query.capitalize()))
            systemFunctions.speak("Please specify. \"{}\" may refer to many things.".format(query.capitalize()))

    


