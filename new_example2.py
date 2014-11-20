import numpy as np

class Bird(object):

    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        print "Init2"

    def get_position(self):
        return [self.x_position, self.y_position]

    def get_velocity(self):
        return np.array([self.x_velocity, self.y_velocity])
