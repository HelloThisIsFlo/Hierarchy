import os
from pathlib import Path

import click

from hierarchy import clone_hierarchy
from hierarchy.utils import display

HOME = Path(os.path.expanduser('~'))

DEFAULT_HIERARCHY_FILE = HOME / '.hierarchy'


@click.command()
@click.option('-f', '--file', 'hierarchy_file', type=click.Path(exists=True))
def main(hierarchy_file):
    if hierarchy_file:
        hierarchy_file = Path(hierarchy_file)
    else:
        hierarchy_file = DEFAULT_HIERARCHY_FILE

    display('Running Hierarchy')
    display('-----------------')
    display('')

    clone_hierarchy(hierarchy_file)


if __name__ == '__main__':
    main()
