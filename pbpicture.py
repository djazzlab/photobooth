# Kivy setups
from kivy.properties import StringProperty
from kivy.uix.scatter import Scatter

class PBPicture(Scatter):
    source = StringProperty(None)
