import sys
import random
import re

class fileHandler:

    def __init__(self):
        self.fileName = 'words.txt'
        self.split_text = []
    def readFile(self):
        #read file and scan into buffer
        f = open(self.fileName)
        while True:
            line = f.readline().split()
            if not line:break
            self.split_text= self.split_text + line
        f.close()

    def pick_random(self):
        #pick random word from file
        word = random.choice(self.split_text)
        #remove special characters
        word = re.sub('[^A-Za-z0-9]+', '', word)
        return word
    
    def execute(self):
        #read the file and pick a word.
        self.readFile()
        word = self.pick_random()
        while len(word)<5:
            word = self.pick_random()
        print word
        return word

        

file_h = fileHandler()
file_h.execute()
