# Python imports
from os import path, makedirs

# Kivy setups
from kivy.uix.camera import Camera

# Local imports
from utils import subfolders_count, files_count

class PBCamera(Camera):
    photo_path = ''
    photos_basepath = '/mnt/photos'

    def __init__(self, **kwargs):
        super(PBCamera, self).__init__(**kwargs)

        self.resolution = (640, 480)
        self.play = True

        # Prepare the folder to store the photos
        self.photos_basepath = '{}/{}'.format(self.photos_basepath, subfolders_count(self.photos_basepath) + 1)
        if not path.exists(self.photos_basepath):
            makedirs(self.photos_basepath)

    def _camera_loaded(self, *largs):
        self.texture = self._camera.texture
        self.texture.flip_horizontal()

    def take_photo(self):
        # Capture photo and save it to photos_basepath
        self.photo_path = '{}/IMG_{}.png'.format(self.photos_basepath, files_count(self.photos_basepath) + 1)
        self.export_to_png(self.photo_path)
