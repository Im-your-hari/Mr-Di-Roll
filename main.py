import random
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
'''
a = random.choice([1,2,3,4,5,6])
print(a)

switch = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six"
}
s = switch.get(a)
print(s)
'''
class MyPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20
        self.label = Label(text="Mr-Di-Roll")
        self.image = Image(source='./images/dice-six-faces-five.png')
        self.button = Button(text="ROLL",background_color=(0,0,1,1))#,on_press=self.roll)
        self.image.keep_ratio = False
        self.image.allow_stretch = False
        self.add_widget(self.label)
        self.add_widget(self.image)
        self.add_widget(self.button)
    
    #def roll(self,instace):
        #Need to add dice logic

class MrDiRoll(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        #self.icon = '#'
        return MyPage()

if __name__ == '__main__':
    MrDiRoll().run()
