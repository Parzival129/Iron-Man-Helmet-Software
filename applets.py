from real_time_object_detection import isRunning
import threading

# All "applets" must have a start function, a stop function, and a isRunning function
import EdithEyes
# Add more applets
import hangman
import cryptoTicker

thread = None

def appRunning() :
    if thread == None : return False
    return thread.isAlive()

def getNameOfRunningApplet() :
    if (thread == None) : return None
    return thread.name

def startApplet(appletName) :
    # Only one app should be running at once
    if appRunning() : return "failed"

    global thread
    thread = None

    appletName = appletName.lower()

    if (appletName == "edith eyes") :
        thread = threading.Thread(target=EdithEyes.start, name=appletName)    
    # Check more applets
    if (appletName == "hangman") :
        thread = threading.Thread(target=hangman.start, name=appletName)  

    if (appletName == "crypto ticker") :
        thread = threading.Thread(target=cryptoTicker.start, name=appletName)

    if (thread == None) :
        return "failed"

    # Start thread
    thread.setDaemon(True)
    thread.start()
    return "succeeded"

def turnOffRunningApplet() :
    if appRunning() == False : return "succeeded"

    stoppedSomething = False
    if (EdithEyes.isRunning()) :
        EdithEyes.stop()
        stoppedSomething = True

    # Check more applets
    if (hangman.isRunning()) :
        hangman.stop()
        stoppedSomething = True

    if (cryptoTicker.isRunning()) :
        cryptoTicker.stop()
        stoppedSomething = True

    if stoppedSomething :
        global thread
        thread = None
        return "succeeded"
    return "failed"

