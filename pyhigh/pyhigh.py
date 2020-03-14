from .elevation import clear_cache, get_elevation

from argparse import ArgumentParser

def main():
    # set up command line arguments
    parser = ArgumentParser()
    parser.add_argument('--lat', type=float, default=None)
    parser.add_argument('--lon', type=float, default=None)
    parser.add_argument('--clean', action='store_true')

    # parse command line input
    args = parser.parse_args()

    # clear the cache if desired
    if args.clean:
        clear_cache()

    # get the elevation
    lat, lon = args.lat, args.lon
    if lat is not None:
        if lon is not None:
            print(get_elevation(lat=lat, lon=lon))
        else:
            raise Exception('Must specify longitude with --lon')
    else:
        if lon is not None:
            raise Exception('Must specify latitude with --lat')
        else:
            pass

if __name__ == '__main__':
    main()