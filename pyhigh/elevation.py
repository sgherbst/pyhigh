import os
import requests
import yaml
import zipfile

from shutil import rmtree
from pathlib import Path
from math import floor
from subprocess import check_output

CACHE_DIR = Path(__file__).resolve().parent / '.cache'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'
}

def get_hgt_name(lat, lon, hgt_dot=True):
    retval = ''

    retval += 'N{:02d}'.format(+int(floor(lat)))
    retval += 'W{:03d}'.format(-int(floor(lon)))
    if hgt_dot:
        retval += '.'
    retval += 'hgt'

    return retval

def get_zip_name(lat, lon):
    return get_hgt_name(lat, lon, lat<=54) + '.zip'

def get_url(lat, lon):
    return 'https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/North_America/' + get_zip_name(lat, lon)

def unzip(path):
    # modified from: https://stackoverflow.com/questions/3451111/unzipping-files-in-python
    zip_ref = zipfile.ZipFile(path, 'r')
    zip_ref.extractall(path.parent)
    zip_ref.close()
    os.remove(path)

def clear_cache():
    rmtree(CACHE_DIR)

def get_elevation(lat, lon):
    # find out the file containing this latitude and longitude
    filename = get_hgt_name(lat, lon)

    # find out if the file exists
    fullfile = CACHE_DIR / filename
    if not fullfile.is_file():
        # if not determine the URL where it is located
        url = get_url(lat, lon)

        # then download the file
        CACHE_DIR.mkdir(exist_ok=True, parents=True)
        print(f'Downloading {get_zip_name(lat, lon)}')
        r = requests.get(url, timeout=5, headers=HEADERS)
        with open(CACHE_DIR / get_zip_name(lat, lon), 'wb') as f:
            f.write(r.content)

        # finally unzip and remove the file
        unzip(CACHE_DIR / get_zip_name(lat, lon))

    # then call a function to analyze the file
    gdal_o = check_output(['gdallocationinfo', '-wgs84', f'{fullfile}', f'{lon}', f'{lat}'])
    parsed = yaml.safe_load(gdal_o)

    return parsed['Report']['Band 1']['Value']

if __name__ == '__main__':
    print(get_elevation(36.52011, -118.671))  # should be 1884
