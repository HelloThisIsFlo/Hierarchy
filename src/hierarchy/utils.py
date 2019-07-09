import click


def display(text, variant=None, reason=None):
    if not variant:
        click.echo(text)
        return

    if variant == 'ERROR':
        click.echo(text, err=True)

