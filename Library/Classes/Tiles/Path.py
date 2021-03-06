#Path.py
# 
# File Contributors
#     Nathan Veillon
#

import random
from .BaseTile import *

class Path(BaseTile):

    directions = ['U','R','D','L']

    def __init__(self,tile_size,current_direction,previous_direction=None,type='Path'):
        self.current_direction = current_direction
        if(previous_direction):
            self.previous_direction = previous_direction
        else:
            self.previous_direction = current_direction
        self.type = type

        image_location = self.select_correct_image()

        BaseTile.__init__(self,tile_size,image_location)
        self.type = type
        self.orientation = self.find_orientation()
        self.surface = pygame.transform.rotate(self.surface,self.orientation)
        self.can_place_tower = False

    def find_orientation(self):
        orientation = 0
        if(self.previous_direction == self.current_direction):
            if(self.current_direction == 'R'):
                orientation = 0
            elif(self.current_direction == 'D'):
                orientation = 90
            elif(self.current_direction == 'L'):
                orientation = 180
            elif(self.current_direction == 'U'):
                orientation = 270
        return orientation

    def select_correct_image(self):
        if(self.type == 'Start'):
            return 'Library/Assets/Tiles/StartPath.png'
        elif(self.type == 'End'):
            return 'Library/Assets/Tiles/EndPath.png'
        else:
            return self.select_path_image()



    def select_path_image(self):
        if(self.previous_direction != self.current_direction):
            return 'Library/Assets/Tiles/Corner'+self.previous_direction+self.current_direction+'.png'
        path_type = random.randint(1,3)
        return 'Library/Assets/Tiles/Path'+str(path_type)+'.png'


