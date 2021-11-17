# ________Modules__________ #

import os
import sys
import platform
import atexit
import time

from rich.console import Console
from rich.markdown import Markdown
import requests
import yaml
import click

# __________________________ #

# Version of the program
__VERSION__ = "0.2.0"

# The start time of the program
start = time.perf_counter()

# detects the user's operating system and the processor architecture
proc_arch = platform.machine()
os_type = platform.system()

# __________________________ #

# An Exception class to handle errors about non Existing Packages
class PackageNotFound(Exception):
    pass


# __________________________ #


def get_nonexistant_path(fname_path):
    """
    Get the path to a filename which does not exist by incrementing path.
    """
    if not os.path.exists(fname_path):
        return fname_path
    filename, file_extension = os.path.splitext(fname_path)
    i = 1
    new_fname = "{}_{}{}".format(filename, i, file_extension)
    while os.path.exists(new_fname):
        i += 1
        new_fname = "{}_{}{}".format(filename, i, file_extension)
    return new_fname


# __________________________ #


def download(download_link, filename):
    """
    Download the file from the link and save it to the filename
    """

    # Check the filename :param is "default"
    if filename == "default":
        filename = download_link.split("/")[-1]

    # Check if the file already exists
    if os.path.isfile(filename):
        user_input = input(
            "\n\033[1;33;40m Warning \033[0m\033[1;30;40m- \033[0m The following file already exists, do you want to delete it (Y/n)? "
        )
        sys.stdout.write("\n")

        # If the user wants to delete the file
        if user_input.lower() == "y":
            # Removes the file
            os.remove(filename)
        # If the user doesn't want to delete the file
        elif user_input.lower() == "n":
            # Renames the file
            filename = get_nonexistant_path(filename)

    try:
        # Download the file
        with open(filename, "wb") as f:
            response = requests.get(download_link, stream=True)
            total = response.headers.get("content-length")

            if total is None:
                f.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    downloaded += len(data)
                    f.write(data)
                    # Count the progress bar length
                    done = int(61 * downloaded / total)
                    # Count the percentage of the download
                    percentage = float("%.1f" % (downloaded * 100 / total))
                    # Print the progress of the download
                    sys.stdout.write(
                        "\r {}% |{}{}| {} \033[2;37;40m/\033[0m {} \033[1;33;40mMB\033[0m".format(
                            percentage,
                            "\033[92m█\033[0m" * done,
                            " " * (61 - done),
                            "%.4f" % (downloaded / 1000000),
                            "%.4f" % (total / 1000000),
                        )
                    )
                    sys.stdout.flush()

        # Print the download success message
        atexit.register(exit_handler)

    # If the user cancels the download by CTRL+C
    except KeyboardInterrupt:
        os.remove(filename)
        print("\n\n\033[91m     X\033[0m Aborted !")

    sys.stdout.write("\n")


# __________________________ #


@click.group()
def fluoly():
    """An Open Source Library/Repo of Add-ons, Tools... for Minecraft: Bedrock Edition."""

    # __________________________ #

    print(
        "\n     🌿 \x1B[3mFluoly \x1B[0m\033[1;30;40m-\033[0m v{}\n".format(__VERSION__)
    )

    # Send an HTTP request to the GitHub API to get the latest release of fluoly :D
    load_repo = requests.get(
        "https://api.github.com/repos/retr0cube/fluoly/releases/latest"
    )
    # Loads the Latests version number
    repo_json = load_repo.json()["name"]

    # Checks if the program's version number atches the latest release
    if repo_json != __VERSION__:
        print(
            "\033[1;33;40m /!\ Warning /!\ You're using v{}, But v{} is the newest version available\033[0m".format(
                __VERSION__, repo_json
            )
        )


# __________________________ #


@click.command()
@click.option(
    "-sys",
    help="Let's you choose which operating system version of a package to choose. Note: This is only available for Tools.",
)
@click.option(
    "--cpu_arch",
    "-c",
    help="Let's you choose which CPU architecture version of a package to choose. Note: This is only available for Tools.",
)
@click.option(
    "--version", "-v", help="Let's you choose which version of a package to choose."
)
@click.option(
    "--path",
    "-p",
    help="Let's you change the path where the package will be downloaded to.",
)
@click.option("--name", "-n", help="Changes the file name of the downloaded package.")
@click.argument("package_name")
def install(version, package_name, cpu_arch, sys, path, name):

    """Installs a Package."""

    # __________________________ #

    # Check if the "downloads" folder exists
    if path is not None and os.path.isdir(path):
        # Changes the working directory to the "downloads" folder
        os.chdir(r"{}".format(path))

    # Check if the "downloads" folder doesn't exist
    if not os.path.isdir("downloads"):
        # Create the "downloads" folder
        os.mkdir("downloads")
    # Changes the working directory to the "downloads" folder
    os.chdir("downloads")

    # __________________________ #

    try:
        # Send an HTTP request to the GitHub API to get the Info about a package
        load_yaml = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}.info.yaml".format(
                package_name, package_name
            )
        ).text

        # Load the YAML file
        repo_yaml = yaml.safe_load(load_yaml)

        # __________________________ #

        # Check if the Package the Package name
        print(
            "\n\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(
                repo_yaml["name"]
            )
        )

        # __________________________ #

        # Check if the Package has a description
        print(
            "\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(
                repo_yaml["author"]
            )
        )

    # if the checks failed and raise a "KeyError" Exception a "PackageNotFound" exception will be raised
    except KeyError:
        raise PackageNotFound(
            " Can't find package with name '{}'\n".format(package_name)
        )

    # __________________________ #

    # Check if the "version" is not None
    if version is not None:
        repo_yaml["version"] = version

    # __________________________ #

    # Send an HTTP request to the GitHub API to get the Install Info about a package :D
    package_installer = requests.get(
        "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}/{}.installer.yaml".format(
            package_name, repo_yaml["version"], package_name
        )
    ).text

    # Loads the Installer YAML file
    package_yaml = yaml.safe_load(package_installer)

    # __________________________ #

    # Prints the install message
    print(
        "\n\033[1;36;40m Info \033[0m\033[1;30;40m- \033[0m Instaling {} {}...\n".format(
            repo_yaml["name"], package_yaml["package_version"]
        )
    )

    # __________________________ #

    # Check if the Package's type is a tool
    if repo_yaml["type"] == "tool":

        # Check if "cpu_arch" is not None
        if cpu_arch is not None:
            proc_arch is cpu_arch

        # Check if "sys" is None
        if sys is not None:
            os_type is sys

        try:
            # Checks if "name" is None or not
            if name is not None:
                download(package_yaml[os_type][proc_arch], name)
            else:
                download(package_yaml[os_type][proc_arch], "default")
        # if the package is Universal this exception will be raised
        except KeyError:
            # Checks if "name" is None or not
            if name is not None:
                download(package_yaml[os_type]["Universal"], name)
            else:
                download(package_yaml[os_type]["Universal"], "default")

    # __________________________ #

    # Check if the Package's type is a plugin or an add-on
    elif repo_yaml["type"] == "addon" or "plugin":

        # Check if "sys" is None
        if sys or cpu_arch is not None:
            print(
                "\n\033[1;31;40m Notice \033[0m\033[1;30;40m- \033[0m You can't use --cpu_arch or --os with this package type."
            )

        # Check if "name" is None or not
        if name is not None:
            download(package_yaml["download_link"], name)
        else:
            download(package_yaml["download_link"], "default")


# ___Exit Handling Stuff____ #


def exit_handler():
    """Handles the exit of the program."""

    # The end time of the program
    finish = time.perf_counter()

    print(
        "\n\n     \033[92m √ Done in {}s !\033[0m\n".format("%.3f" % (finish - start))
    )


# __________________________ #


@click.command()
@click.option("--read_me", "-md", help="Shows the README.md of a package", is_flag=True)
@click.argument("package_name")
def find(package_name, read_me):
    """Shows info about a Package."""

    # __________________________ #

    try:
        # Send an HTTP request to the GitHub API to get the Info about a package
        load_yaml = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}.info.yaml".format(
                package_name, package_name
            )
        ).text

        # Load the YAML file
        repo_yaml = yaml.safe_load(load_yaml)

        print(
            "\033[1;36;40m Package Type \033[0m\033[1;30;40m- \033[0m {}\n".format(
                repo_yaml["type"].title()
            )
        )

    # if the checks failed and raise a "KeyError" Exception a "PackageNotFound" exception will be raised
    except KeyError:
        raise PackageNotFound(
            " Can't find package with name '{}'\n".format(package_name)
        )

    # __________________________ #

    # Prints the package name
    print(
        "\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_yaml["name"]
        )
    )
    # Prints the package Author
    print(
        "\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_yaml["author"]
        )
    )
    # prints the package version
    print(
        "\033[1;36;40m Latest Version \033[0m\033[1;30;40m- \033[0m v{}".format(
            repo_yaml["version"]
        )
    )

    # checks if the "read_me" flag is True
    if not read_me:
        print(
            "\n\033[0;35;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(
                repo_yaml["desc"]
            )
        )
    elif read_me:

        # Send an HTTP request to the GitHub API to get the README.md of a package
        package_md = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/README.md".format(
                package_name
            )
        ).text

        print("\n\033[0;35;40m Package's README.MD file \033[0m\033[1;30;40m:\n\033[0m")

        # Formats the Markdown file
        console = Console()

        console.print(Markdown(package_md))
        print("")

    # __________________________ #


# Adding the "find" & "install" command
fluoly.add_command(install)
fluoly.add_command(find)

# __________________________#

if __name__ == "__main__":
    fluoly(prog_name="fluoly")
