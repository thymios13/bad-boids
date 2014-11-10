"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
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


boids = initialize_boids(50)    # Setting up the initial number of boids


def update_boids(boids):
    xs,ys,xvs,yvs=boids

    for i in range(len(xs)):
        for j in range(len(xs)):
            # Fly towards the middle
            xvs[i]+=(xs[j]-xs[i])*0.01/len(xs)
            yvs[i]+=(ys[j]-ys[i])*0.01/len(xs)
            # Fly away from nearby boids
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
                xvs[i]+=(xs[i]-xs[j])
                yvs[i]+=(ys[i]-ys[j])
            # Try to match speed with nearby boids
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i]+=(xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i]+=(yvs[j]-yvs[i])*0.125/len(xs)
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
