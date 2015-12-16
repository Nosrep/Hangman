#!/usr/bin/env python2

import string

class Hangman(object):
    def __init__(self):
        self.reset()

    def reset(self, word = None):
        if word is None:
            word = ''
        self.word = word
        self.failCount = 0

    def render(self):
        displayText = string.translate(self.word,
                string.maketrans(string.lowercase, '_' * len(string.lowercase)))
        print displayText

    def guess(self, letter):
        if self.word == '':
            print "There's not even a fucking word, dumbass!"
        elif letter.upper() in self.word:
            print "You already guessed this letter you moron.  Ignoring."
        else:
            newWord = string.translate(self.word,
                    string.maketrans(letter.lower(), letter.upper()))
            if newWord == self.word:
                self.failCount += 1
                print "You fucking suck, you've failed %d times!" % self.failCount
                if self.failCount > 5:
                    print "You've lost the game.  Get good, noob."
            else:
                if newWord.isupper():
                    print "You fucking win, but failed %d times" % self.failCount
                else:
                    print "You found a new letter, have a fucking cookie."
                self.word = newWord
