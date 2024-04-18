import numpy as np
from pyhigh import *

def test_pyhigh():
    assert get_elevation(36.52011, -118.671, "North_America") == 1884

    res = get_elevation_batch([(36.52011, -118.671,"North_America"), (36.62011, -118.771,"North_America")])
    assert np.array_equal(res, [1884, 2438])

    clear_cache()

if __name__ == "__main__":
    test_pyhigh()