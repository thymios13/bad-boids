"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
from initializing_boids import initialize_boids
from my_update_boids import update_boids

# Number and positions/velocities of boids initialization
boids_number = 50
boids = initialize_boids(boids_number)


# Boids Animation
figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])
def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))
anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
