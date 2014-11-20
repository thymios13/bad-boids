from nose.tools import assert_raises

from boids_velocity import tmp_velocity


def test_empty_input():
    with assert_raises(TypeError):
        tmp_velocity([])