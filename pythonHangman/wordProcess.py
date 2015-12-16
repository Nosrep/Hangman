import re
class wordProcess:


    def __init__(self,word):
        self.word = word
        self.size = len(self.word)
        self.guesses = []

    def execute(self,letter):
        index_letters = []
        index = 0
        empty = False
        guessed = False
        if not letter in self.guesses:
            self.guesses.append(letter)
            if self.word.isupper():
                empty = True
            else:
                while index < len(self.word):
                    index = self.word.find(letter)
                    if(index == -1):
                        break
                    index_letters.append(index)
                    #change element in list to accommidate for it being guessed
                    s = list(self.word)
                    s[index]=s[index].upper()
                    self.word = "".join(s)
        else:
            guessed = True
                
        return index_letters,empty,guessed

    def display_word(self):
        index = 0
        s = list(self.word)
        while index<len(s):
            if s[index].islower():
                s[index] = " __ "
            else:
                s[index] = " "+s[index]+" "
            index+=1
        display_string = "".join(s)
        return display_string
        



            

