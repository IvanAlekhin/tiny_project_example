import click

from src.scripts import ShipFinder


@click.command()
@click.option('--file', help='path to file', required=True)
@click.option('--log_level', default='WARNING')
def count_ships(file: str, log_level: str):
    s = ShipFinder(file, log_level.upper())
    click.echo(s.count_ships())


if __name__ == '__main__':
    count_ships()
