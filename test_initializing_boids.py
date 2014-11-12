from nose.tools import assert_equal
from initializing_boids import initialize_boids

boids_number = 50 # Define the number of boids to be tested
boids_x_positions, boids_y_positions, boids_x_velocities, boids_y_velocities = initialize_boids(50)

def test_that_returns_four_vectors():
    assert_equal(len(initialize_boids(boids_number)),4)

def test_if_boids_x_positions_is_equal_with_boids_number():
    assert_equal(len(boids_x_positions),boids_number)

def test_if_boids_y_positions_is_equal_with_boids_number():
    assert_equal(len(boids_y_positions),boids_number)

def test_if_boids_x_velocities_is_equal_with_boids_number():
    assert_equal(len(boids_x_velocities),boids_number)

def test_if_boids_y_velocities_is_equal_with_boids_number():
    assert_equal(len(boids_y_velocities),boids_number)
