# Kivy setups
from kivy.uix.label import Label

class PBLabel(Label):
    def __init__(self, **kwargs):
        super(PBLabel, self).__init__(**kwargs)

        self.text = 'L&X Wedding - 15 Sept 2018'
        self.font_size = 40
        self.font_name = 'BOD_B.TTF'
        self.color = 0, 0, 0, 1.0
