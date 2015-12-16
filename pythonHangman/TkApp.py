from Tkinter import *
import re

class TkApp():
    def __init__(self):
        self.token = "default"
        self.master = Tk()
        self.guesses = []
        Label (self.master,text ="Guess a letter.").grid(row=0)
        self.e1 = Entry(self.master)
        self.e1.grid(row=0,column=1)
        Button(self.master,text='Enter',command=self.recordObject).grid(row=0,column=3,sticky=W,pady=4)
        self.master.mainloop()
        

    def exsists(self,token):
        for guess in self.guesses:
            if guess == token:
                return True
            
        return False
    
    def tokenHandler(self,token):
        item = token
        if len(item)>1:
            print "please only enter one character"
            return False
        elif bool(re.match('\D',item))==False:
            print"please only enter letters"
            return False
        elif self.exsists(token):
            print "you already guessed that!"
            return False
        else:
            return True
       
    def recordObject(self):
        item = self.e1.get()
        self.token=item
        if self.tokenHandler(self.token):
            self.guesses.append(self.token)
            #print self.guesses
            self.master.destroy()
        return self.token
    
    def get(self):
        return self.token




