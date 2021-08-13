import threading

# All "applets" must have a start function, a stop function, and a isRunning function
import EdithEyes
# Add more applets
import hangman

thread = None

def appRunning() :
    if thread == None : return False
    if thread.isAlive() : return True

    if (thread.name == "edith eyes") :
        return EdithEyes.isRunning()
    # Check more apps
    if (thread.name == "hangman") :
        return hangman.isRunning()

    return True

def getNameOfRunningApplet() :
    if (thread == None) : return None
    return thread.name

def startApplet(appletName) :
    # Only one app should be running at once
    if appRunning() : return "failed"

    appletName = appletName.lower()

    global thread
    if (appletName == "edith eyes") :
        thread = threading.Thread(target=EdithEyes.start, name=appletName)    
    # Check more applets
    if (appletName == "hangman") :
        thread = threading.Thread(target=hangman.start, name=appletName)  


    if (thread == None) :
        return "failed"

    # Start thread
    thread.setDaemon(True)
    thread.start()
    return "succeeded"

def turnOffRunningApplet(appletName) :
    if appRunning() == False : return "succeeded"
    
    appletName = appletName.lower()

    print(appletName)

    stoppedSomething = False
    if (appletName == "edith eyes") :
        EdithEyes.stop()
        stoppedSomething = True
    # Check more applets
    if (appletName == "hangman") :
        hangman.stop()
        stoppedSomething = True

    return "succeeded" if (stoppedSomething) else "failed"

