from nose.tools import assert_equal
from initializing_boids import initialize_boids

def test_that_returns_four_vectors():
    assert_equal(len(initialize_boids(50)),4)
