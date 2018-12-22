# Kivy setups
from kivy.uix.button import Button

class PBTrigger(Button):
    def __init__(self, callback, **kwargs):
        super(PBTrigger, self).__init__(**kwargs)

        self.text = 'Take Photo !'
        self.font_size = 40
        self.font_name = 'BOD_B.TTF'
        self.color = 0, 0, 0, 1.0
        self.background_color = 1, 0.84, 0, 1.0
        self.bind(on_press = lambda dt: callback(counter = 3))