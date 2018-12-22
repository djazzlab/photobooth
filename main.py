# Python setups
from random import randint

# Kivy setups
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

# Local setups
from pbcamera import PBCamera
from pblabel import PBLabel
from pbpicture import PBPicture
from pbtrigger import PBTrigger

class PhotoBoothCamera(FloatLayout):
    pb_camera = None
    pb_label = None
    pb_picture = None
    pb_trigger = None

    def __init__(self, **kwargs):
        super(PhotoBoothCamera, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.size_hint = 1, 1

        # Adding the camera preview
        self.pb_camera = PBCamera()
        self.pb_camera.pos_hint = {'x': 0, 'y': 0}
        self.pb_camera.size_hint = 1, 1
        self.add_widget(self.pb_camera)

        # Adding the photo trigger button
        self.pb_trigger = PBTrigger(callback = self.capture)
        self.pb_trigger.pos_hint = {'x': 0, 'y': 0}
        self.pb_trigger.size_hint = 1, 0.15
        self.add_widget(self.pb_trigger)

    def capture(self, counter = None):
        '''
        Trigger the capture of a photo using the PBCamera
        '''
        if counter == -1:
            # Hide the button
            self.remove_widget(self.pb_trigger)
            self.pb_trigger.text = 'Take Photo !'
            
            # Take the photo
            self.pb_camera.take_photo()

            # Hide the camera
            self.remove_widget(self.pb_camera)
            
            # Display the photo, arranged
            self.pb_picture = PBPicture(source = self.pb_camera.photo_path)
            self.pb_picture.pos_hint = {'x': 0, 'y': 0.2}
            self.pb_picture.size_hint = 1, 1
            self.add_widget(self.pb_picture)

            # Add text
            self.pb_label = PBLabel()
            self.pb_label.pos_hint = {'x': 0, 'y': 0.05}
            self.pb_label.size_hint = 1, 0.15
            self.add_widget(self.pb_label)

            # Restore the button to the screen
            # after 2 sec and hide the just taken picture
            Clock.schedule_once(lambda dt: self.restore_camera(), 7)
            return
        elif counter == 0:
            self.pb_trigger.text = 'CHEEEEEEESE ;-)'
        else:
            self.pb_trigger.text = str(counter)

        # Call the capture function every seconds
        Clock.schedule_once(lambda dt: self.capture(counter = counter - 1), 1)

    def restore_camera(self):
        self.remove_widget(self.pb_picture)
        self.remove_widget(self.pb_label)
        self.add_widget(self.pb_camera)
        self.add_widget(self.pb_trigger)

class PhotoBooth(App):
    def build(self):
        return PhotoBoothCamera()

PhotoBooth().run()
