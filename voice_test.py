import pyttsx3

def greet_func(the_greeting):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id) 
  engine.say(the_greeting)
  engine.setProperty('rate',120)  #120 words per minute
  engine.setProperty('volume',10) 
  engine.runAndWait()

greet_func("Hello")