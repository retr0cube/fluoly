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

class FetchJsonError(Exception):
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

    if bool(repo_json["is_on_github"]):

        latest_package_version = requests.get("https://api.github.com/repos/{}/{}/releases/latest".format(repo_json['author'], addon_name))
        load_version = latest_package_version.json()["name"]

    #__________________________#

    print("\n\n\033[0;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['name']))


    #__________________________#
    supported_platforms_json = repo_json['supported_platforms_download_links']

    if bool(repo_json["is_on_github"]) and os_type in  repo_json["supported_os"] and proc_arch in repo_json["supported_arch"]:
        print("\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Installing Package...\n") 
        wget.download(supported_platforms_json[str(os_type)][str(proc_arch)].format(load_version["name"],load_version["name"]),"{}_{}.zip".format(addon_name, load_version["name"]))

    elif not bool(repo_json["is_on_github"]):
        print("\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Installing Package...\n")
        wget.download(repo_json["download_link"],"{}_{}.zip".format(addon_name, repo_json["version"]))

    else:
      FetchJsonError(" This Package doesn't have a valid download link or your processor architecture is incompatible with it")

    os.remove('{}.json'.format(addon_name))

    #__________________________#



@click.command()
@click.argument('addon_name')
def show(addon_name):
    """Shows info about an Add-on."""
    
    try:
        print("\n\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Fetching JSON data...\n")
        wget.download("https://raw.githubusercontent.com/retr0cube/fluoly/master/repo/{}.json".format(addon_name),"{}.json".format(addon_name))

        with open('{}.json'.format(addon_name),) as load_json:
            repo_json = json.load(load_json)
    except Exception:
        raise PackageNotFound(" Can't find package with name '{}'\n".format(addon_name))

    if bool(repo_json["is_on_github"]):
        latest_package_version = requests.get("https://api.github.com/repos/{}/{}/releases/latest".format(repo_json['author'], addon_name))
        load_version = latest_package_version.json()["name"]

    print("\n\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['name']))
    print("\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(repo_json['author']))
    print("\033[1;36;40m Latest Version \033[0m\033[1;30;40m- \033[0m {}".format(load_version))
    print("\n\033[1;36;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(repo_json['desc']))

    os.remove('{}.json'.format(addon_name))

fluoly.add_command(install)
fluoly.add_command(show)

#__________________________#

if __name__ == '__main__':
    fluoly(prog_name='fluoly')
