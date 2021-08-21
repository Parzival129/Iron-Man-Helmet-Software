import sys
import pyjokes
import requests
import wikipedia
import os
import systemFunctions
import datetime
from applets import appRunning, startApplet, getNameOfRunningApplet, turnOffRunningApplet
from time import ctime, localtime, sleep
from random import randint
from weatherApp import weather
from systemHistogram import runHistogram

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
    if "turn off screen" in rawQuery or "clear screen" in rawQuery:
        systemFunctions.hide()

    if "turn on screen" in rawQuery or "start screen" in rawQuery:
        systemFunctions.show()

    if "tell me a joke" in rawQuery:
        joke = pyjokes.get_joke()
        systemFunctions.draw_text(joke, 0, 0)
        systemFunctions.speak(joke)
        return

    if "tell me the weather" in rawQuery or "whats the weather" in rawQuery or "whats the weather like" in rawQuery or "how is the weather" in rawQuery:
        weather()
        return

    if "show system histogram" in rawQuery or "run system histogram" in rawQuery:
        runHistogram()
        return

    if "how are you" in rawQuery or "how are you doing" in rawQuery or "are you doing well" in rawQuery:
        answer = ['I am fine', 'I am great!', 'I am in a crippling deppression.'][randint (0, 2)]
        systemFunctions.draw_text(answer)
        systemFunctions.speak(answer)
        return

    if "what time is it" in rawQuery or "tell me the time" in rawQuery or "whats the time" in rawQuery:
        systemFunctions.draw_text(str(ctime()), 0, 0)
        
        todayTime = f"{localtime()[3] % 12} o {localtime()[4]} {['AM', 'PM'][localtime()[3] // 12]}"
        date = datetime.date.today().strftime("%B %m %Y")

        systemFunctions.speak(f"{todayTime}, {date}")
        return
    
    if "check running applet" in rawQuery or "is a applet running" in rawQuery:
        appletName = getNameOfRunningApplet()
        systemFunctions.speak("{} is currently running".format( appletName if appletName else "No applet" ))
        return
    
    query = getCommandParameters(rawQuery, "start", 2)
    if query != None:
        if appRunning() :
            systemFunctions.speak("Applet already running")
            return
        response = startApplet(query)
        if (response == "failed") :
            systemFunctions.speak('Could not find applet')
            return
        systemFunctions.speak('Starting {}'.format(query))

    query = getCommandParameters(rawQuery, "stop running", 2)
    if query != None:
        response = turnOffRunningApplet(query)
        if (response == "failed") :
            systemFunctions.speak('Could not close applet {}'.format(query))
            sleep(2)
            return
        systemFunctions.speak('No applets are currently running')
        sleep(2)
        systemFunctions.turnOnJarvis()

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
            systemFunctions.draw_text("Looking up: " + query)
            sleep(2)
            query = '+'.join(query.split())
            wiki_res = wikipedia.summary(query, sentences=2)
            systemFunctions.draw_text(wikipedia.summary(query, sentences=1), 0, 0)
            systemFunctions.speak(wiki_res)
        except wikipedia.exceptions.PageError:
            print("An error occured, coudn't find anything on: " + query)
            systemFunctions.speak("An error occured, coudn't find anything on: " + query)
            systemFunctions.draw_text("couldn't find anything on " + query)
        except requests.exceptions.ConnectionError:
            print("A connection error occured, coudn't find anything on: " + query)
            systemFunctions.speak("A connection error occured, coudn't find anything on: " + query)
            systemFunctions.draw_text("connection error!")
        except wikipedia.exceptions.DisambiguationError:
            print("Please specify. \"{}\" may refer to many things.".format(query.capitalize()))
            systemFunctions.speak("Please specify. \"{}\" may refer to many things.".format(query.capitalize()))
            systemFunctions.draw_text(query + " refers to many different things")



