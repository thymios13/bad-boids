"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
from numpy import power
import random


def initialize_boids(boids_number):
    boids_x=[]
    boids_y=[]
    boid_x_velocities=[]
    boid_y_velocities=[]

    for x in range(boids_number):
        boids_x.append(random.uniform(-450,50.0))
        boids_y.append(random.uniform(300.0,600.0))
        boid_x_velocities.append(random.uniform(0,10.0))
        boid_y_velocities.append(random.uniform(-20.0,20.0))

    return boids_x, boids_y, boid_x_velocities, boid_y_velocities

# Number and positions/velocities of boids initialization
bois_number = 50
boids = initialize_boids(bois_number)


def update_boids(boids):
    xs,ys,xvs,yvs=boids
    boids_number = len(xs)
    for i in range(bois_number):
        for j in range(bois_number):
            # Fly towards the middle
            xvs[i]+=(xs[j]-xs[i])*0.01/boids_number
            yvs[i]+=(ys[j]-ys[i])*0.01/boids_number
            # Fly away from nearby boids
            tmp_velocity = power((xs[j]-xs[i]),2) + power((ys[j]-ys[i]),2)
            if tmp_velocity < 100:
                xvs[i]+=(xs[i]-xs[j])
                yvs[i]+=(ys[i]-ys[j])
            # Try to match speed with nearby boids
            elif tmp_velocity < 10000:
                xvs[i]+=(xvs[j]-xvs[i])*0.125/boids_number
                yvs[i]+=(yvs[j]-yvs[i])*0.125/boids_number
        # Move according to velocities
        xs[i]+=xvs[i]
        ys[i]+=yvs[i]


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
