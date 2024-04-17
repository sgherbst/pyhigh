import numpy as np
from shutil import rmtree
from pathlib import Path
from math import floor

from .download import download
from .unzip import unzip
from .hgt import read_elevation_from_file

CACHE_DIR = Path(__file__).resolve().parent / '.cache'

CONTINENTS=["Eurasia","North_America","Africa","Australia","Islands","South_America"]

def get_hgt_name(lat, lon,continent):
    if continent in CONTINENTS:
        retval = continent + '/'
    else:
        raise ValueError(f'Continent "{continent}" not in list of continents:', CONTINENTS)
    #lat
    if lat < 0:
        prefix = 'S'
    else:
        prefix = 'N'
    retval += prefix+'{:02d}'.format(abs(int(floor(lat))))
    
    #long
    if lon < 0:
        prefix = 'W'
    else:
        prefix = 'E'
    retval += prefix+'{:03d}'.format(abs(int(floor(lon))))
    retval += '.hgt'

    return retval

def get_zip_name(lat, lon, continent):
    return get_hgt_name(lat, lon, continent) + '.zip'

def get_url_for_zip(zip_name):
    return f'https://firmware.ardupilot.org/SRTM/{zip_name}'

def clear_cache():
    rmtree(CACHE_DIR)

def get_elevation_batch(lat_lon_cont_list):
    # organize requests by filename
    req_dict = {}
    for k, (lat, lon, continent) in enumerate(lat_lon_cont_list):
        key = int(floor(lat)), int(floor(lon)), continent
        if key not in req_dict:
            req_dict[key] = ([], [], [])
        req_dict[key][0].append(k)
        req_dict[key][1].append(lat)
        req_dict[key][2].append(lon)

    # process the files one-by-one
    retval = np.zeros(len(lat_lon_cont_list))
    for (lat_int, lon_int, continent), (indices, lats, lons) in req_dict.items():
        # find the location of the file
        
        filename = get_hgt_name(lat_int, lon_int, continent)
        fullfile = CACHE_DIR / filename

        # download the file if needed
        if not fullfile.is_file():
            # if not determine the URL where it is located
            zip_name = get_zip_name(lat_int, lon_int, continent)
            url = get_url_for_zip(zip_name)
            # then download the file
            print(f'Downloading {zip_name}')
            CACHE_DIR.mkdir(exist_ok=True, parents=True)
            (CACHE_DIR / continent).mkdir(exist_ok=True, parents=True)
            download(url, CACHE_DIR / zip_name)
            # finally unzip and remove the file
            unzip(CACHE_DIR / zip_name)
        # process the file
        data = read_elevation_from_file(fullfile, np.array(lats), np.array(lons))
        # write data back into the return value at the appropriate indices
        retval[indices] = data

    # return the elevation data
    return retval

def get_elevation(lat, lon, continent):
    return get_elevation_batch([(lat, lon, continent)])[0]

if __name__ == '__main__':
    print(get_elevation(36.52011, -118.671, "North_America"))  # should be 1884
