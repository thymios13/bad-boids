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
