import os
from pathlib import Path

import click

HOME = Path(os.path.expanduser('~'))

DEFAULT_HIERARCHY_FILE = HOME / '.hierarchy_cloner'


@click.command()
@click.option('-f', '--file', 'hierarchy_file', type=click.Path(exists=True))
def main(hierarchy_file):
    if hierarchy_file:
        hierarchy_file = Path(hierarchy_file)
    else:
        hierarchy_file = DEFAULT_HIERARCHY_FILE

    click.echo('Running Hierarchy Cloner')
    click.echo(click.format_filename(str(hierarchy_file)))



if __name__ == '__main__':
    main()
