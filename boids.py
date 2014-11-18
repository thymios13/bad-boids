"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
#from initializing_boids import initialize_boids
from my_update_boids import update_boids
from numpy import array
#import random


class Bird(object):
    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def get_position(self):
        return array([self.x_position, self.y_position])

    def get_velocity(self):
        return array([self.x_velocity, self.y_velocity])


def generate_random_bird():
    import random
    x_position = random.uniform(-450, 50.0)
    y_position = random.uniform(300.0, 600.0)
    x_velocity = random.uniform(0, 10.0)
    y_velocity = random.uniform(-20.0, 20.0)

    return Bird(x_position, y_position, x_velocity, y_velocity)

# Number and positions/velocities of boids initialization
boids_number = 50
#boids = initialize_boids(boids_number)

birds = []
x_pos = []
y_pos = []
x_vel = []
y_vel = []

for i in range(boids_number):
    birds.append(generate_random_bird())

    x_pos.append(birds[i].get_position()[0])
    y_pos.append(birds[i].get_position()[1])
    x_vel.append(birds[i].get_velocity()[0])
    y_vel.append(birds[i].get_velocity()[1])

boids = x_pos, y_pos, x_vel, y_vel



# Boids Animation
figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])
def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0], boids[1]))
anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
