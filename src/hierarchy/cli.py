import os
from pathlib import Path

import click

from hierarchy.rename import clone_hierarchy

HOME = Path(os.path.expanduser('~'))

DEFAULT_HIERARCHY_FILE = HOME / '.hierarchy'


@click.command()
@click.option('-f', '--file', 'hierarchy_file', type=click.Path(exists=True))
def main(hierarchy_file):
    if hierarchy_file:
        hierarchy_file = Path(hierarchy_file)
    else:
        hierarchy_file = DEFAULT_HIERARCHY_FILE

    click.echo('Running Hierarchy')
    click.echo('-----------------')
    click.echo('')

    clone_hierarchy(hierarchy_file)


if __name__ == '__main__':
    main()
