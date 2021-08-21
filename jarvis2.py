import threading
import systemFunctions
from time import sleep
from random import choice
from systemFunctions import draw_text
from jarvisCommands import askJarvis

draw_text("J.A.R.V.I.S Booted!", 0, 0)
sleep(3)
# initialization

greetings = ["Welcome back sir", "Hello sir, what can I do for you?", "Greetings sir"]
draw_text(choice(greetings))
systemFunctions.speak(choice(greetings))
sleep(3)
draw_text("")

while True:
    if (systemFunctions.jarvisActivated()) :
        data = systemFunctions.recordAudio()
        askJarvis(data)



