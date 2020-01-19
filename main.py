from argparse import ArgumentParser
from counter import Counter


def main():
    parser = ArgumentParser(
        description='Count the total number of lines present in files in a directory')

    parser.add_argument('-r', '--root', type=str, default='.',
                        help='Root directory to start counting. Defaults to current working directory')
    parser.add_argument('-e', '--extensions', type=str, nargs='*',
                        default=[], help='List of extensions to be included in counting. Defaults to all extensions')
    parser.add_argument('-t', '--tree', action='store_true',
                        help='Visualize folder structure')

    args = parser.parse_args()
    counter = Counter(args)
    print('\nTotal Lines: ' + str(counter.get_total()))


if __name__ == '__main__':
    main()
