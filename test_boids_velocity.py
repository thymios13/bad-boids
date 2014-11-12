from boids_velocity import tmp_velocity
from nose.tools import assert_raises

def test_empty_input():
    with assert_raises(TypeError):
        tmp_velocity([])