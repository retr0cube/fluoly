import click

# @click.option('--show', help='Shows Info about an Add-on.')
@click.group()
def fluoly():
    """An Open Source Add-on Library for Minecraft: Bedrock Edition."""

@click.command()
@click.argument('addon_name')
def install(addon_name):
    """Installs an Add-on."""
    

fluoly.add_command(install)

if __name__ == '__main__':
    fluoly(prog_name='fluoly')
