from boids_velocity import tmp_velocity

def update_boids(boids):
    [x_positions, y_positions, x_velocities, y_velocities] = boids
    boids_number = len(x_positions)

    for i in range(boids_number):
        for j in range(boids_number):
            # Fly towards the middle
            x_velocities[i] += (x_positions[j]-x_positions[i])*0.01/boids_number
            y_velocities[i] += (y_positions[j]-y_positions[i])*0.01/boids_number

            # Fly away from nearby boids
            if tmp_velocity(x_positions,y_positions,i,j) < 100:
                x_velocities[i] += (x_positions[i]-x_positions[j])
                y_velocities[i] += (y_positions[i]-y_positions[j])

            # Try to match speed with nearby boids
            elif tmp_velocity(x_positions,y_positions,i,j) < 10000:
                x_velocities[i] += (x_velocities[j]-x_velocities[i])*0.125/boids_number
                y_velocities[i] += (y_velocities[j]-y_velocities[i])*0.125/boids_number

        # Move according to velocities
        x_positions[i]+=x_velocities[i]
        y_positions[i]+=y_velocities[i]