
import os, sys
import pygame
from pygame.locals import *
from helpers import *
from Tkinter import *
from TkApp import *
from FileHandler import *
from wordProcess import *

class HangMan:
    """Handles initialiazation and creating the game"""


    
    def __init__(self,width= 800,height= 600):
        #pygame screen init
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        #pygame background images
        self.background = load_image('background.png')
        self.wrong_image = load_image('incorrect.png')
        self.final_image = load_image('noose.png')
        self.screen.blit(self.background,(0,0))
        #game data
        self.game_word = ""
        self.user_word = ""
        self.gameover = False
        self.win = False
        #pygame text
        self.font = pygame.font.Font(None,36)
        self.lose_font = pygame.font.Font(None,200)
        #wrong answer image data
        self.num_wrong = []
        self.width_wrong = 700
        self.height_wrong = 5
        self.wrong_answers = 0
        #music
        pygame.mixer.music.load('data\sound\Resistance.ogg')
        self.wrong_sound = pygame.mixer.Sound('data\sound\wrong.wav')
        self.correct_sound = pygame.mixer.Sound('data\sound\correct.wav')
        self.pump_sound = pygame.mixer.Sound('data\sound\pumpsong.wav')
        self.gameover_sound = pygame.mixer.Sound('data\sound\gameover.wav')
        self.wrong_sound.set_volume(.05)
        self.correct_sound.set_volume(.05)
        self.pump_sound.set_volume(.05)
        self.gameover_sound.set_volume(.05)
        pygame.mixer.set_num_channels(24)
        pygame.mixer.music.set_volume(0.01)
        

        
    def loadSprites(self):
        """Load the sprites that we need"""
        self.man = man()
        self.man_sprites = pygame.sprite.RenderPlain((self.man))#sprite object
        
    def display_wrong(self):
        if(self.num_wrong):
            for item in self.num_wrong:
                self.screen.blit(self.wrong_image,item)

    def set_word(self):
        #get word from text file.
        file_h = fileHandler()
        self.game_word = file_h.execute()
        
    def game_over(self):
        pygame.mixer.music.stop()
        pygame.mixer.find_channel().play(self.pump_sound,0,0,100)
        pygame.mixer.find_channel().play(self.gameover_sound,0,0,100)
        lose_text = self.lose_font.render("YOU LOSE",True,(255,0,0))
        lpos = lose_text.get_rect()
        self.screen.blit(lose_text,(self.width/2 - lpos.width/2,self.height/2-lpos.height))
        

    def winning(self):
        pygame.mixer.music.stop()
        pygame.mixer.find_channel().play(self.pump_sound,0,0,100)
        win_text = self.lose_font.render("YOU WIN!",True,(255,0,0))
        wpos = win_text.get_rect()
        self.screen.blit(win_text,(self.width/2 - wpos.width/2,self.height/2-wpos.height))
           
    
    def MainLoop(self):
        pygame.mixer.music.play(-1)
        self.set_word()
        self.process = wordProcess(self.game_word)
        self.loadSprites()
        self.user_word = self.process.display_word()#translate the hidden word
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            display_text = self.font.render(self.user_word,True,(10,10,10))
            textpos = display_text.get_rect()
            self.screen.blit(self.background,(0,0))
            self.display_wrong()
            self.screen.blit(display_text,(self.width/2-textpos.width/2+10,500))
            self.screen.blit(self.final_image,(345,70))
            self.man_sprites.draw(self.screen)
            
            if self.gameover:
                self.game_over()
            if self.win:
                self.winning()
                
                
            pygame.display.flip()
            #get user input
            master = TkApp()
            blah = master.get()
            index_letters,isfull,guessed=self.process.execute(blah)
            #do something with this information
            if not index_letters and isfull==False and not guessed:
                pygame.mixer.find_channel().play(self.wrong_sound,0,0,100)
                if self.wrong_answers <6:
                    self.num_wrong.append((self.width_wrong,self.height_wrong+(self.wrong_answers*70)))
                    self.wrong_answers+=1
                else:
                    print "YOULOSE"
                    self.gameover = True
                    
                   
            elif guessed:
                print "you already guessed that!"
            elif index_letters:
                pygame.mixer.find_channel().play(self.correct_sound,0,0,100)
                self.user_word = None
                self.user_word = self.process.display_word()
            else:
                #throw you won event
                print "YOU WIN!"
                self.win = True
                
                
            pygame.display.update()


            
class man(pygame.sprite.Sprite):
        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            self.index = 0
            self.images.append(load_image('hangman.gif',-1))
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.move_ip(500-self.rect.width,340-self.rect.height)
            self.body_parts = 0
            
        def update(self):
            self.index+=1
            self.image = self.images[self.index]
    
            
        def get_index(slef):
            return self.index        
            
            




    
if __name__ == "__main__":
    MainWindow = HangMan()
    MainWindow.MainLoop()
        
