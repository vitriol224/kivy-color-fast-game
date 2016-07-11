#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy



from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen 
from kivy.uix.screenmanager import FadeTransition
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import random


Builder.load_file("color-fast.kv")



    
class ScreenManagement(ScreenManager,Widget):
    
    
    def play_game(self):
    
        ''' this function is called when the start game
        button is clicked...it prepares everything for
        the game to begin...'''
        
        self.color_dict = ({"darkgreen":"#006400",
            "grey":"#bebebe",
            "gold":"#ffd700","green":"#00ee00",
            "purple":"#a020f0",
            "red":"#ee0000","yellow":"#ffff00",
            "white":"#ffffff","pink":"#FFC0CB",
            "deeppink":"#FF1493","maroon":"#FF34B3",
            "violet":"#EE82EE","blue":"#0000FF",
            "orchid":"#DA70D6","magenta":"#CD00CD",
            "indigo":"#4B0082","navy":"#000080",
            "skyblue":"#87CEEB","cyan 3":"#00CDCD",
            "mint":"#BDFCC9","khaki":"#F0E68C",
            "orange":"#FFA500","wheat":"#F5DEB3",
            "brick":"#9C661F","carrot":"#ED9121",
            "flesh":"#FF7D40","sienna":"#A0522D",
            "sepia":"#5E2612","tomato":"#FF6347",
            "snow":"#FFFAFA","rosybrown":"#BC8F8F",
            "brown":"#A52A2A","firebrick":"#B22222",
            "silver":"#C0C0C0","coral":"#FF7F50",
            "chocolate":"#D2691E","greenyellow":"#ADFF2F",
            "pale":"#db7093","oldlace":"#fdf5e6","olivedrab":"#c0ff3e"
            })#end color dictionary
            
        self.name_list = (["many","just","apple","bike",
        	    "money","job","prince",
            "ride","sizzle","ballet","meow",
            "hahaha","bingo!","gambler","rogger","swagger",
            "melon","pimple","dimple","sample","aluminium",
            "battery","kivy","django","favourite","professor",
            "alkaline","smuggle","android","java","python",
            "calculate","hospital","camera","lens","papaya",
            "alhaji","mallam","mermaid","states","nigeria",
            "laughing","yes","programming","shoe","boast",
            "bread","thread","linker","text file","vity loves",
            "lil wayne","music rocks","hmmm","great","perfect",
            "freeman","university","primary","said","gas bag",
            "plump","never say die","farewell" ])
            #end random name list here...
        
        self.dict_values = [x for x in self.color_dict.values()]
        #collect all color hex codes and make this list
        
        self.time_left_number = self.ids.seconds_left
        #get the id of time left label...
        
        self.the_text = self.ids.current_text
        #get the id of the current random text
        
        self.current_score = self.ids.score
        #get the id of current score label
        
        self.current_score.text = "00"
        #make the current score be 00 on game start
        
        self.final_score = self.ids.score_text
        #ger the final score id @ game over screen
        
        self.final_score.text = "00"
        #set the score @ game over screen 00
        
        self.submitted_color2 = self.ids.color_name_box
        #get the text the user typed...
        
        self.submitted_color2.text = ""
        #make the text box empty on game start...
        
        self.initial_color_hex = ""
        #create a variable to hold color hex
        
        self.initial_name = ""
        #create a variable to hold a random name
        
        self.initial_color_hex = random.choice(self.dict_values)
        #pick a random color hex code from
        #color hex list above...
        
        self.initial_name = random.choice(self.name_list)
        #pick a random name from the name list variable
        #above
        
        self.the_text.text = ("[color={}] {} [/color]"
        .format(self.initial_color_hex,self.initial_name))
        #show the user a random text picked from name list
        #painted with the random color hex picked
        
        self.time_left_number.text = "90"
        #set the countdown time to 90 secs...
        
        self.current = "game_screen"
        #take the user to the game screen...
        
        self.time_left_number.color = 0,1,0,1
        #set the countdown seconds number color to green...
        
        self.beep_sound = SoundLoader.load("beep-06.wav")
        #load the countdown beep sound...
        
        Clock.schedule_interval(self.time_left,1)
        #start the countdown from time_left method...


    ##############################################



    def time_left(self,dt):
        
        '''this method gets the current seconds left in
        playing the game and keeps deducting by 1. When the
        time hits zero,it ends the game and takes you to the 
        game over screen...'''
        
        self.initial_score = int(self.current_score.text)
        #get the initial score label id when game starts...
        #score should be 00
        
        if self.beep_sound.state == "play":
            self.beep_sound.stop()
            #stop beep sound if it played once...
            
        self.final_score = self.ids.score_text
        #get the game over score number label...
        
        self.initial_time = int(self.time_left_number.text)
        #create a variable with the time allocated to play
        #according tk the time_left_number id..
        
        self.initial_time -=1
        #deduct a second from the time left...
        
        self.time_left_number.text = str(self.initial_time)
        #update the time left...
        
        if self.initial_time == 10:
            self.beep_sound.play()
            #play beep sound...
            
            self.time_left_number.color = 255,0,0
            #if the seconds reach ten,play the beep sound
            #and change the seconds color to red...
            
        if self.initial_time == 0:
            self.beep_sound.stop()
            self.current = "game_over"
            self.final_score.text = str(self.initial_score)
            return False ##end countdown
            
            '''if the time hits zero,take the user to the 
            game over screen,stop beep sound and show them thier score
            '''

    #############################################
    
    
    def check_color(self):
        ''' this method is called each thw submit button is called
        during play '''
        
        self.submitted_color = self.ids.color_name_box.text
        #get the text submitted by player...
        
        self.text = self.ids.current_text
        #get the current random text...
        
        self.initial_score = int(self.current_score.text)
        #get the the users score...
        
        try: 
            '''avoid invalidkey error when when using user entered 
            text as dictionary key'''
         
            if self.color_dict[self.submitted_color] == self.initial_color_hex:
                '''if the user entered color is same as the text color...
                ...'''
                            
                self.initial_score += 3
                #increase the player score by 3
                
                self.current_score.text = str(self.initial_score)
                #update the score text...
                
                self.submitted_color2.text = ""
                #wipe the input box...

                self.initial_color_hex = random.choice(self.dict_values)
                #pick a new random hex color code 
                
                self.initial_name = random.choice(self.name_list)
                #pick a new random name ...
        
                self.the_text.text = ("[color={}] {} [/color]"
                    .format(self.initial_color_hex,self.initial_name))
                #display the random name painted with the random color
                    
            else:
                if self.submitted_color2.text == "":
            	        pass
                else:
                    self.submitted_color2.text = ""
        
                    self.initial_color_hex = random.choice(self.dict_values)
            
                    self.initial_name = random.choice(self.name_list)
        
                    self.the_text.text = ("[color={}] {} [/color]"
                        .format(self.initial_color_hex,self.initial_name))
                
                    '''continue the game and wipe the text box,pick and display
                    a new name and color even though the user entered a wrong color'''
                                                
        except:
            
            if self.submitted_color2.text == "":
            	    pass
            else:
                self.submitted_color2.text = ""
        
                self.initial_color_hex = random.choice(self.dict_values)
            
                self.initial_name = random.choice(self.name_list)
        
                self.the_text.text = ("[color={}] {} [/color]"
                    .format(self.initial_color_hex,self.initial_name))
                
                '''continue the game and wipe the text box,pick and display
                a new name and color even though key error is encountered'''
            
                    

    ##############################################

    
    def goto_home(self):
        self.current = "main"

        
    ##############################################
    
    def confirm_quit(self):
        self.box=FloatLayout()
        
        self.lab=(Label(text="Do you want to quit? ",font_size=30,
        	size_hint=(None,None),pos_hint={'x':.25,'y':.6}))
        self.box.add_widget(self.lab)
        
        self.but=(Button(text="No",size_hint=(None,None),
        	width=self.width/3,height=70,pos_hint={'x':0,'y':0}))
        self.box.add_widget(self.but)

        self.but2=(Button(text="Yes",size_hint=(None,None),
        	width=self.width/3,height=70,pos_hint={'right':1,'y':0}))
        self.box.add_widget(self.but2)
       
        self.main_pop = Popup(title="QUIT GAME ?",content=self.box,
        	size_hint=(.8,.5),auto_dismiss=False,title_size=25)
        	
        self.but.bind(on_press=self.main_pop.dismiss)
        #self.but2.bind(on_press=self.quit_game)
        
        self.main_pop.open()

    ##############################################
        

    
    def quit_game(self):
        exit()
        #close the application...
    
    
    ##############################################

    
    



class Manage(App):
    def build(self):
       return ScreenManagement()



Manage().run()

