"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
from numpy import power
import random


def initialize_boids(boids_number):
    boids_x_positions=[]
    boids_y_positions=[]
    boid_x_velocities=[]
    boid_y_velocities=[]

    for x in range(boids_number):
        boids_x_positions.append(random.uniform(-450,50.0))
        boids_y_positions.append(random.uniform(300.0,600.0))
        boid_x_velocities.append(random.uniform(0,10.0))
        boid_y_velocities.append(random.uniform(-20.0,20.0))

    return boids_x_positions, boids_y_positions, boid_x_velocities, boid_y_velocities

# Number and positions/velocities of boids initialization
bois_number = 50
boids = initialize_boids(bois_number)


def update_boids(boids):
    x_positions,y_positions,x_velocities,y_velocities=boids
    boids_number = len(x_positions)
    for i in range(bois_number):
        for j in range(bois_number):
            # Fly towards the middle
            x_velocities[i]+=(x_positions[j]-x_positions[i])*0.01/boids_number
            y_velocities[i]+=(y_positions[j]-y_positions[i])*0.01/boids_number
            # Fly away from nearby boids
            tmp_velocity = power((x_positions[j]-x_positions[i]),2) + power((y_positions[j]-y_positions[i]),2)
            if tmp_velocity < 100:
                x_velocities[i]+=(x_positions[i]-x_positions[j])
                y_velocities[i]+=(y_positions[i]-y_positions[j])
            # Try to match speed with nearby boids
            elif tmp_velocity < 10000:
                x_velocities[i]+=(x_velocities[j]-x_velocities[i])*0.125/boids_number
                y_velocities[i]+=(y_velocities[j]-y_velocities[i])*0.125/boids_number
        # Move according to velocities
        x_positions[i]+=x_velocities[i]
        y_positions[i]+=y_velocities[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
