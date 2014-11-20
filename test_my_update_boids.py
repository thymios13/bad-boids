from nose.tools import assert_raises

from my_update_boids import update_boids


def test_for_empty_input():
    with assert_raises(ValueError):
        update_boids([])