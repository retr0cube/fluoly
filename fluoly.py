#________Modules__________#

import click
import atexit
import json
import os
import requests
import wget

#___Exit Handling Stuff____#

def exit_handler():
    print("\n\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m\033[92m √ Done!\033[0m\n")

#__________________________#

print("\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m 🌿 Fluoly by Retr0cube\n")

#__________________________#

# @click.option('--show', help='Shows Info about an Add-on.')
@click.group()
def fluoly():
    """An Open Source Add-on Library for Minecraft: Bedrock Edition."""

#__________________________#

@click.command()
@click.argument('addon_name')
def install(addon_name):
    """Installs an Add-on."""
    atexit.register(exit_handler)


    print("\n\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Fetching JSON data...\n")
    wget.download("https://raw.githubusercontent.com/retr0cube/fluoly/master/repo/{}.json".format(addon_name),"{}.json".format(addon_name))
    with open('{}.json'.format(addon_name),) as load_json:
        repo_json = json.load(load_json)

    print("\n\n\033[0;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['name']))
    print("\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Installing Package...\n")
    wget.download(repo_json['download_url'],'{}.{}'.format(addon_name,repo_json['file_extension']))
    os.remove('{}.json'.format(addon_name))

@click.command()
@click.argument('addon_name')
def show(addon_name):
    """Shows info about an Add-on."""
    with open('{}.json'.format(addon_name),) as load_json:
        repo_json = json.load(load_json)

    print("\n\033[0;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['name']))
    print("\033[1;35;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(repo_json['desc']))

fluoly.add_command(install)
fluoly.add_command(show)

#__________________________#

if __name__ == '__main__':
    fluoly(prog_name='fluoly')
