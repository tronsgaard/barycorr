#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test():
    import barycorr
    import numpy as np
    params = {
        'jd_utc': [2457535.067362, 2457462.12724721],
        'ra': 293.08995940,
        'dec': 69.66117649,
        'lat': 28.2983,
        'lon': -16.5094,
        'elevation': 2400,
        'pmra': 598.07,
        'pmdec': -1738.40,
        'parallax': 173.77,
        'rv': 26780,
        'zmeas': [-4.99432219e-06, 1.16637407e-05]
    }
    result = barycorr.bvc(**params)
    diff = result - [-1312.08186269, 515.87479325]

    # Returns: numpy.array([-1312.08186269,   515.87479325])
    assert np.all(diff < 0.01), "Should be [-1312.08186269,   515.87479325]"

if __name__ == "__main__":
    test()
    print("It works!")
