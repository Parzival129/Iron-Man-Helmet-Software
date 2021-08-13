import threading
import systemFunctions
from jarvisCommands import askJarvis

systemFunctions.draw_text("E.D.I.T.H booted", 40, 30, "white")
systemFunctions.draw_text("second test, alsdjaklshdahwkdhahdbkjawhdahskldjakwjdbnajklh", 0, 0)

# initialization
systemFunctions.speak("Hello Sir, what can I do for you?")
while True:
    if (systemFunctions.jarvisActivated()) :
        data = systemFunctions.recordAudio()
        askJarvis(data)



