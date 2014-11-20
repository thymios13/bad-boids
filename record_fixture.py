import yaml
import boids as bd
from copy import deepcopy

boids = bd.Boids(
    flock_attraction=0.01 / 50,
    avoidance_radius=10,
    formation_flying_radius=100,
    speed_matching_strength=0.125 / 50
)

boids.initialise_random(50)
boids.add_eagle(0, 0, 0, 50)

before = deepcopy(boids.boids)
bd.update_boids(boids)
after = boids.boids

fixture = {"before": before, "after": after}
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
