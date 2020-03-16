import numpy as np
from pyhigh import *

def test_pyhigh():
    assert get_elevation(36.52011, -118.671) == 1884

    res = get_elevation_batch([(36.52011, -118.671), (36.62011, -118.771)])
    assert np.array_equal(res, [1884, 2438])

    clear_cache()