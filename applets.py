import threading

# All "applets" must have a start function, a stop function, and a isRunning function
import EdithEyes
# Add more applets


thread = None

def appRunning() :
    if thread == None : return False
    if thread.isAlive() : return True

    if (thread.name == "edith eyes") :
        return EdithEyes.isRunning()
    # Check more apps

    return True

def getNameOfRunningApplet() :
    return thread.name

def startApplet(appletName) :
    # Only one app should be running at once
    if appRunning() : return "failed"

    appletName = appletName.lower()

    global thread
    if (appletName == "edith eyes") :
        thread = threading.Thread(target=EdithEyes.start, name=appletName)    
    # Check more applets


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

    return "succeeded" if (stoppedSomething) else "failed"

