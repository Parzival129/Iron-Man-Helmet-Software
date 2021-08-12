import threading
import systemFunctions
from jarvisCommands import askJarvis

systemFunctions.draw_text("E.D.I.T.H booted", 40, 30, "white")
systemFunctions.draw_text("second test, alsdjaklshdahwkdhahdbkjawhdahskldjakwjdbnajklh", 0, 0)

def EdithEyes():
	import real_time_object_detection

# Start taking camera input for object detection
eyes = threading.Thread(target=EdithEyes)
eyes.start()

# initialization
systemFunctions.speak("Hello Sir, what can I do for you?")
while True:
    data = systemFunctions.recordAudio()
    askJarvis(data)
