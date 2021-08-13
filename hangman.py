import random
from warnings import catch_warnings
from systemFunctions import speak, draw_text, turnOffJarvis, turnOnJarvis, recordAudio

_runGame = False

def isRunning() :
    return _runGame

# Play game
import os
from time import sleep
from random import randint

# Word class
class GameWord :
    def __init__(self, filename, topic):
        wordList = open(filename).read().split('\n')
        self.codeword = wordList[randint(0, len(wordList) - 1)]
        self.answer = self.codeword
        self.topic = topic
        
        for char in self.codeword :
            if (char != ' ') :
                self.answer = self.answer.replace(char, "_")



def getYesNo() :
    heardSomething = False
    isYes = False
    while heardSomething == False :
        userInput = recordAudio().lower().split(' ')

        for word in userInput :
            if word == "yes" :
                isYes = True
                heardSomething = True
                break
            if word == "no" :
                isYes = False
                heardSomething = True
                break
    
    return "yes" if isYes else "no"



def getGameWord() :
    topics = ["superheroes", "coding", "space", "music", "clothing", "sports"]
    chosenTopic = "random"
    foundFile = False

    speak("Please choose your topic")
    textToPrint = "Please choose your topic:\n" + "\n".join(topics) + "\nrandom topic"

    draw_text(textToPrint)

    while foundFile == False :
        userInput = recordAudio().split(' ')
        draw_text(textToPrint)
        for word in userInput :
            for topic in topics :
                if word == topic or word == "random" :
                    foundFile = True
                    chosenTopic = word
                    break
            
            if foundFile :
                break
    
    if chosenTopic == "random" :
        chosenTopic = topics[randint(0, len(chosenTopic) - 1)]
    
    speak("Your topic is {}".format(chosenTopic))

    return GameWord(f"HangmanData/{chosenTopic}.txt", chosenTopic)

def showStatus(gameword, lives, wrongGuesses) :
    speak("You have {} guesses left".format(lives))
    draw_text("Topic: {}\nGuesses left: {}\nWrong: {}\n\nProgress:\n{}".format(gameword.topic, lives, ' '.join(wrongGuesses), ' '.join(list(gameword.answer))))

def getLetter() :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    foundLetter = False
    inputedLetter = ''

    speak("Choose a letter or say a word that starts with this letter")
    while foundLetter == False :        
        userInput = recordAudio().lower().split(' ')

        for word in userInput :
            if not word : continue

            for letter in alphabet :
                if word[0] == letter :
                    foundLetter = True
                    inputedLetter = letter
            if foundLetter : break
    
    speak("Your letter is {}".format(inputedLetter))
    return inputedLetter


def playGame() :
    draw_text("Starting Hangman...")
    sleep(5)

    gameword = getGameWord()
    lives = 5

    speak("Welcome to Hangman!")
    draw_text("Welcome to Hangman!")
    sleep(3)

    wrongGuesses = []
    while (lives != 0 and gameword.answer != gameword.codeword and isRunning()) :
        showStatus(gameword, lives, wrongGuesses)
        letter = getLetter()
        

        if letter in wrongGuesses or letter in gameword.answer :
            speak("You have already guessed letter {}".format(letter))
            sleep(2)
            continue

        if letter in gameword.codeword :
            for i in range(len(gameword.codeword)) :
                if letter == gameword.codeword[i] :
                    letterList = list(gameword.answer)
                    letterList[i] = letter
                    gameword.answer = ''.join(letterList)
            continue
        else :
            speak("Guess is incorrect")
            wrongGuesses.append(letter)
            lives -= 1


    if (gameword.answer == gameword.codeword) :
        draw_text("You have won!\nPlay again?\nSay yes or no")
        speak("You have conquered Hangman! Would you like to play again?")

        response = getYesNo()
        
        if (response == "yes") :
            # Play game again
            playGame()
            return
        else :
            # Quit
            return
    
    if (lives == 0) :
        draw_text("HA! YOU LOST!\nPlay again?\nSay yes or no")
        speak("You have lost. Would you like to play again?")

        response = getYesNo()
        
        if (response == "yes") :
            # Play game again
            playGame()
            return
        else :
            # Quit
            return



if __name__ == "__main__" :
    turnOffJarvis()
    _runGame = True
    playGame()



# Define applet functions

def stop() :
    global _runGame
    _runGame = False

def start() :
    sleep(2)
    turnOffJarvis()

    global _runGame
    _runGame = True
    

    playGame()
    stop()
    turnOnJarvis()

