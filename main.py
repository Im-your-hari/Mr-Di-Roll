import random
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from playsound import playsound



class MyPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20
        self.label = Label(text="Mr-Di-Roll")
        self.image = Image(source='./images/dice-six-faces-five.png')
        self.button = Button(text="ROLL",background_color=(0,0,1,1),on_press=self.roll)
        self.image.keep_ratio = False
        self.image.allow_stretch = False
        self.add_widget(self.label)
        self.add_widget(self.image)
        self.add_widget(self.button)
    
    def roll(self,instace):
        #Need to add dice logic
        a = random.choice([1,2,3,4,5,6])
        if a==1:
            self.image.source = ('./images/dice-six-faces-one.png')
            playsound('./audios/one.mp3',True)
        elif a==2:
            self.image.source = ('./images/dice-six-faces-two.png')
            playsound('./audios/two.mp3',True)
        elif a==3:
            self.image.source = ('./images/dice-six-faces-three.png')
            playsound('./audios/three.mp3',True)
        elif a==4:
            self.image.source = ('./images/dice-six-faces-four.png')
            playsound('./audios/four.mp3',True)
        elif a==5:
            self.image.source = ('./images/dice-six-faces-five.png')
            playsound('./audios/five.mp3',True)
        else:
            self.image.source = ('./images/dice-six-faces-six.png')
            playsound('./audios/six.mp3',True)

class MrDiRoll(App):
    def build(self):
        Window.clearcolor = (1,0,0,1)
        self.icon = './images/icon.png'
        return MyPage()

if __name__ == '__main__':
    MrDiRoll().run()
