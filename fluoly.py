# ________Modules__________ #

import os
import platform
import atexit
import json
import click
import requests
import wget
import send2trash

# __________________________ #


class PackageNotFound(Exception):
    pass


class FetchJsonError(Exception):
    pass


# ___Exit Handling Stuff____ #


def exit_handler():
    print(
        "\n\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m\033[92m √ Done!\033[0m\n"
    )


# __________________________ #

proc_arch = platform.machine()
os_type = platform.system()

# __________________________ #


print("\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m 🌿 Fluoly by Retr0cube")

# __________________________ #


@click.group()
def fluoly():
    """An Open Source Library/Repo of Add-ons, Tools... for Minecraft: Bedrock Edition."""


# __________________________ #


@click.command()
@click.option("--version")
@click.argument("package_name")
def install(version, package_name):

    """Installs an Add-on."""
    atexit.register(exit_handler)

    # __________________________ #

    if os.path.isdir("downloads"):
        send2trash.send2trash("downloads")
        os.mkdir("downloads")
        is_project_exists = True
    elif not os.path.isdir("downloads"):
        os.mkdir("downloads")
        is_project_exists = False
    os.chdir("downloads")

    # __________________________ #

    try:
        load_json = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}.info.json".format(
                package_name, package_name
            )
        )

        repo_json = load_json.json()

    except Exception:
        raise PackageNotFound(
            " Can't find package with name '{}'\n".format(package_name)
        )

    # __________________________ #

    print(
        "\n\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_json["name"]
        )
    )
    print(
        "\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_json["author"]
        )
    )

    # __________________________ #

    if repo_json["type"] == "tool":

        if version is not None:
            repo_json["version"] = version

        tool_installer = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}/{}.installer.json".format(
                package_name, repo_json["version"], package_name
            )
        )

        tool_json = tool_installer.json()

        print(
            "\n\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Instaling {} {}...\n".format(
                repo_json["name"], tool_json["package_version"]
            )
        )

        if os.path.isfile(
            "{}_{}_{}.zip".format(package_name, tool_json["package_version"], proc_arch)
        ):
            user_input = input(
                "\n\033[1;33;40m Warning \033[0m\033[1;30;40m- \033[0m The following file already exists do you want to keep it (Y/N)? "
            )
            print("")

            if user_input == "N" or "n":
                os.remove(
                    "{}_{}_{}.zip".format(
                        package_name, tool_json["package_version"], proc_arch
                    )
                )
            elif user_input == "Y" or "y":
                pass

        wget.download(
            tool_json[str(os_type)][str(proc_arch)],
            "{}_{}_{}.zip".format(
                package_name, tool_json["package_version"], proc_arch
            ),
        )

    # __________________________ #

    if repo_json["type"] == "plugin":
        plugin_installer = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}/{}.installer.json".format(
                package_name, repo_json["version"], package_name
            )
        )

        plugin_json = plugin_installer.json()

        print(
            "\n\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Instaling {} {}...\n".format(
                repo_json["name"], plugin_json["package_version"]
            )
        )

        if os.path.isfile(
            "{}_{}.zip".format(package_name, plugin_json["package_version"])
        ):
            user_input = input(
                "\n\033[1;33;40m Warning \033[0m\033[1;30;40m- \033[0m The following file already exists do you want to keep it (Y/N)? "
            )
            print("")

            if user_input == "N" or "n":
                os.remove(
                    "{}_{}.zip".format(package_name, plugin_json["package_version"])
                )
            elif user_input == "Y" or "y":
                pass

        wget.download(
            plugin_json["download_link"],
            "{}_{}.zip".format(package_name, plugin_json["package_version"]),
        )

    # __________________________ #

    if repo_json["type"] == "addon":
        addon_installer = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}/{}.installer.json".format(
                package_name, repo_json["version"], package_name
            )
        )

        addon_json = addon_installer.json()

        print(
            "\n\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Instaling {} {}...\n".format(
                repo_json["name"], addon_json["package_version"]
            )
        )

        if os.path.isfile(
            "{}_{}.zip".format(package_name, addon_json["package_version"])
        ):
            user_input = input(
                "\n\033[1;33;40m Warning \033[0m\033[1;30;40m- \033[0m The following file already exists do you want to keep it (Y/N)? "
            )
            print("")

            if user_input == "N" or "n":
                os.remove(
                    "{}_{}.zip".format(package_name, addon_json["package_version"])
                )
            elif user_input == "Y" or "y":
                pass

        wget.download(
            addon_json["download_link"],
            "{}_{}.zip".format(package_name, addon_json["package_version"]),
        )

    # __________________________ #

    else:
        FetchJsonError(
            "The following package doesn't have a Valid link or Your system is incompatible\n"
        )

    # __________________________ #


@click.command()
@click.argument("package_name")
def show(package_name):
    """Shows info about an Add-on."""

    # __________________________ #

    try:
        load_json = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}.info.json".format(
                package_name, package_name
            )
        )

        repo_json = load_json.json()

    except Exception:
        raise PackageNotFound(
            " Can't find package with name '{}'\n".format(package_name)
        )

    # __________________________ #

    print(
        "\n\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_json["name"]
        )
    )
    print(
        "\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_json["author"]
        )
    )
    print(
        "\033[1;36;40m Latest Version \033[0m\033[1;30;40m- \033[0m v{}".format(
            repo_json["version"]
        )
    )
    print(
        "\n\033[0;35;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(
            repo_json["desc"]
        )
    )

    # __________________________ #


fluoly.add_command(install)
fluoly.add_command(show)

# __________________________#

if __name__ == "__main__":
    fluoly(prog_name="fluoly")
