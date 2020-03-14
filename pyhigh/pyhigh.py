from argparse import ArgumentParser

def main():
    # set up command line arguments
    parser = ArgumentParser()

    # parse command line input
    args = parser.parse_args()

    print('Hello World!')

if __name__ == '__main__':
    main()