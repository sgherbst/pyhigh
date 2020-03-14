# pyhigh
[![Actions Status](https://github.com/sgherbst/pyhigh/workflows/Regression/badge.svg)](https://github.com/sgherbst/pyhigh/actions)
[![Code Coverage](https://codecov.io/gh/sgherbst/pyhigh/branch/master/graph/badge.svg)](https://codecov.io/gh/sgherbst/pyhigh)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pyhigh.svg)](https://badge.fury.io/py/pyhigh)

``pyhigh`` is a Python package for accessing elevation data, which is retrieved from a [USGS dataset](https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/North_America/).  The package uses caching to avoid unecessary downloads from the USGS dataset, but please respect their download policies.

## Installation

### Linux

```shell
> sudo apt-get install gdal-bin
> pip install pyhigh
```

### macOS

```shell
> brew install gdal
> pip install pyhigh
```

## Usage

### Command-line utility

The ``pyhigh`` Python package includes a command-line tool of the same name to retreive the elevation at a particular latitude and longitude:

```shell
> pyhigh --lat 36.52011 --lon -118.671
1884
```

As necessary, files will be download from a USGS dataset and cache in the folder ``pyhigh/pyhigh/.cache``.  To clear this cache, use the ``--clean`` argument:

```shell
> pyhigh --clean
```

### Python API

The ``get_elevation`` function returns the elevation, in meters, at the given latitude and longitude.

```python
>>> from pyhigh import get_elevation
>>> get_elevation(lat=36.52011, lon=-118.671)
1884
```

Similar to the command-line tool, the ``pyhigh`` cache can be cleared with the API function ``clear_cache``:

```python
>>> from pyhigh import clear_cache
>>> clear_cache()
```