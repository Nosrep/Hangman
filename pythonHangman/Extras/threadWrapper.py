from Tkinter import *
import threading

class TkApp(threading.Thread):
    def __init__(self):
        self.master=Tk()
        #self.s = Tkinter.StringVar()
        #self.s.set('Foo')
        Label(self.master,text ="Guess a letter.").grid(row=0)
        e1 = Entry(self.master)
        e1.grid(row=0,column=1)
        Button(self.master,text='Enter',command=self.master.quit).grid(row=0,column=3,sticky=W,pady=4)
        threading.Thread.__init__(self)

    def run(self):
        self.master.mainloop()


#app = TkApp()
#app.start()

# Now the app should be running and the value shown on the label
# can be changed by changing the member variable s.
# Like this:
# app.s.set('Bar')
