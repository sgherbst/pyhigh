# modified from: https://github.com/aatishnn/srtm-python/blob/master/srtm.py
import numpy as np

def read_elevation_from_file(hgt_file, lats, lons, mode='srtm3'):
    # low-level function: given a file and a list of longitudes and latitudes,
    # return the elevation at those points.  "lats" and "lons" should be numpy
    # arrays

    # determine file format
    if mode.lower() == 'srtm1':
        samples = 3601
    elif mode.lower() == 'srtm3':
        samples = 1201
    else:
        raise Exception(f'Unknown mode: {mode}')

    # read in elevation data
    with open(hgt_file, 'rb') as hgt_data:
        # HGT is 16bit signed integer(i2) - big endian(>)
        elevations = np.fromfile(
            hgt_data,  # binary data
            np.dtype('>i2'),  # data type
            samples * samples  # length
        ).reshape((samples, samples))

    # determine rows and columns to be read
    lat_rows = np.round((lats - np.floor(lats)) * (samples - 1)).astype(int)
    lon_cols = np.round((lons - np.floor(lons)) * (samples - 1)).astype(int)

    # look up data at computed indices
    return elevations[samples - 1 - lat_rows, lon_cols].astype(int)