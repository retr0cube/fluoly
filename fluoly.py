#________Modules__________#

import click
import atexit
import json
import os
import platform
import requests
import wget

#__________________________#

class PackageNotFound(Exception):
    pass

#___Exit Handling Stuff____#

def exit_handler():
    print("\n\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m\033[92m √ Done!\033[0m\n")

#__________________________#

proc_arch = platform.machine()
os_type = platform.system()

#__________________________#


print("\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m 🌿 Fluoly by Retr0cube\n")

#__________________________#

@click.group()
def fluoly():
    """An Open Source Library/Repo of Add-ons, Tools... for Minecraft: Bedrock Edition."""

#__________________________#

@click.command()
@click.option("-U" , help="Upgrades the Package if it's outdated.")
@click.option("-o" , help="Overrides the Package if it's already installed.")
@click.argument('addon_name')
def install(addon_name, u, o):

    """Installs an Add-on."""
    atexit.register(exit_handler)

    #__________________________#

    print("\n\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Fetching JSON data...\n")
    if os.path.isfile("{}.json".format(addon_name)):
        os.remove("{}.json".format(addon_name))

    try:
        wget.download("https://raw.githubusercontent.com/retr0cube/fluoly/master/repo/{}.json".format(addon_name),"{}.json".format(addon_name))

        with open('{}.json'.format(addon_name),) as load_json:
            repo_json = json.load(load_json)
    except Exception:
        raise PackageNotFound(" Can't find package with name '{}'\n".format(addon_name))
    #__________________________#


    print(list(repo_json.keys()))
    
    if bool(repo_json["is_on_github"]) == True:

        latest_package_version = requests.get("https://api.github.com/repos/{}/{}/releases/latest".format(repo_json['author'], addon_name))
        load_version = latest_package_version.json()["tag_name"]

    #__________________________#

    print("\n\n\033[0;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['name']))
    print("\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Installing Package...\n")

    #__________________________#

    if bool(repo_json["is_on_github"]) == True and  os_type == repo_json['supported_platforms'][str(os_type)] and  proc_arch == repo_json['supported_platforms'][str(os_type)]:
        wget.download(repo_json['supported_platforms'][str(os_type)][str(proc_arch)].format(load_version),"{}_{}.zip".format(addon_name, load_version))

    #__________________________#

    os.remove('{}.json'.format(addon_name))

@click.command()
@click.argument('addon_name')
def show(addon_name):
    """Shows info about an Add-on."""
    
    try:
        wget.download("https://raw.githubusercontent.com/retr0cube/fluoly/master/repo/{}.json".format(addon_name),"{}.json".format(addon_name))

        with open('{}.json'.format(addon_name),) as load_json:
            repo_json = json.load(load_json)
    except Exception:
        raise PackageNotFound(" Can't find package with name '{}'\n".format(addon_name))

    print("\n\033[0;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['name']))
    print("\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['author']))
    print("\n\033[1;36;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(repo_json['desc']))


fluoly.add_command(install)
fluoly.add_command(show)

#__________________________#

if __name__ == '__main__':
    fluoly(prog_name='fluoly')
