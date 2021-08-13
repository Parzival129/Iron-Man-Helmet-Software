# EdithEyes "applet"

import real_time_object_detection

def start() :
    real_time_object_detection.start()

def stop() :
    real_time_object_detection.stop()

def isRunning() :
    return real_time_object_detection.isRunning()
