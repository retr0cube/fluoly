# ________Modules__________ #

import os
import sys
import platform
import atexit
import time

from rich.traceback import install
from rich.markdown import Markdown
import requests
import yaml
import click

# __________________________ #

# Version of the program
__VERSION__ = "0.2.1"

# The start time of the program
start = time.perf_counter()

# Rich formatting
console = Console()
install()

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


def download(download_link, filename=None):
    """
    Download the file from the link and save it to the filename
    """

    # Check the filename :param
    if not filename:
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
@click.version_option(__VERSION__)
def fluoly():
    """An Open Source Library/Repo of Add-ons, Tools... for Minecraft: Bedrock Edition."""

    # __________________________ #

    print(
        "\n      \U0001F33F \x1B[3mFluoly \x1B[0m\033[1;30;40m-\033[0m v{}\n".format(
            __VERSION__
        )
    )

    # Send an HTTP request to the GitHub API to get the latest release of fluoly :D
    load_repo = requests.get(
        "https://api.github.com/repos/retr0cube/fluoly/releases/latest"
    )
    # Loads the Latests version number
    repo_json = load_repo.json()["tag_name"]

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
    "--machine",
    "-m",
    help="Lets you choose which operating system version of a package to choose. Note: This is only available for Tools.",
)
@click.option(
    "--cpu_arch",
    "-c",
    help="Lets you choose which CPU architecture version of a package to choose. Note: This is only available for Tools.",
)
@click.option(
    "--version", "-v", help="Lets you choose which version of a package to choose."
)
@click.option(
    "--path",
    "-p",
    help="Lets you change the path where the package will be downloaded to.",
    type=click.Path(exists=True)
)
@click.option("--name", "-n", help="Changes the file name of the downloaded package.")
@click.argument("package_name")
def install(version, package_name, cpu_arch, machine, path, name):
    """Installs a Package."""

    if package_name == "self":
        print("\n You can't install yourself !\n")
        sys.exit(1)    
    elif package_name == "fluoly":
        # Send an HTTP request to the GitHub API to get the latest release of fluoly :D
        load_repo = requests.get(
            "https://api.github.com/repos/retr0cube/fluoly/releases/latest"
        )
        # Loads the Latests version number
        repo_json = load_repo.json()

        if __VERSION__ == repo_json["tag_name"]:
            print(
                " \033[1;30;40m- \033[0mYou're using the latest version of Fluoly \033[1;30;40m- \033[0m\n"
            )
            sys.exit(1)
        else:
            download(download_link=repo_json["assets"][0]["browser_download_url"])



        sys.exit(1)

    # __________________________ #

    # Check if the "downloads" folder exists
    if path and os.path.isdir(path):
        # Changes the working directory to the "downloads" folder
        os.chdir(r"{}".format(path))

    # Check if the "downloads" folder doesn't exist
    if not os.path.isdir("downloads"):
        # Create the "downloads" folder
        os.mkdir("downloads")
    # Changes the working directory to the "downloads" folder
    os.chdir("downloads")

    # __________________________ #

    # Send an HTTP request to the GitHub API to get the Info about a package
    load_yaml = requests.get(
        "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}.info.yaml".format(
            package_name, package_name
        )
    ).text

    # Load the YAML file
    repo_yaml = yaml.safe_load(load_yaml)

    if not "type" in repo_yaml:
        raise ValueError(" Can't find package with name '{}'\n".format(package_name))

    # __________________________ #

    # Decides which version to install depending on the user's choice
    repo_yaml["version"] = version or repo_yaml["version"]

    # __________________________ #

    # Send an HTTP request to the GitHub API to get the Install Info about a package :D
    package_installer = requests.get(
        "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}/{}.installer.yaml".format(
            package_name, repo_yaml["version"], package_name
        )
    ).text

    # Loads the Installer YAML file
    package_yaml = yaml.safe_load(package_installer)

    if not "package_version" in package_yaml:
        raise ValueError(" Unvalid package version '{}'\n".format(version))

    # __________________________ #

    # Print the package's name
    print(
        """\n\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}
\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}

\033[1;36;40m Info \033[0m\033[1;30;40m- \033[0m Instaling {} {}...\n""".format(
            repo_yaml["name"],
            repo_yaml["author"],
            repo_yaml["name"],
            package_yaml["package_version"],
        )
    )

    # __________________________ #

    # Check if the Package's type is a tool
    if repo_yaml["type"] == "tool":

        # detects the user's operating system and the processor architecture
        os_type = machine or platform.system()
        proc_arch = cpu_arch or platform.machine()

        # __________________________ #

        download(
            package_yaml[os_type][
                proc_arch if proc_arch in package_yaml[os_type] else "Universal"
            ]
        )

    # __________________________ #

    # Check if the Package's type is a plugin or an add-on
    else:

        # Check if "sys" is None
        if machine or cpu_arch:
            print(
                "\n\033[1;31;40m Notice \033[0m\033[1;30;40m- \033[0m You can't use --cpu_arch or --os with this package type."
            )

        download(package_yaml["download_link"], name)

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
@click.option("--tag", "-t", help="Shows the content of a tag", is_flag=True)
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
        dict.get(repo_yaml["type"])

    # if the checks failed and raise a "KeyError" Exception a "ValueError" exception will be raised
    except KeyError:
        raise ValueError(" Can't find package with name '{}'\n".format(package_name))

    # __________________________ #

    print(
        """
\033[1;36;40m Package Type \033[0m\033[1;30;40m- \033[0m {}
    
\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}
\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}
    
\033[1;36;40m Latest Version \033[0m\033[1;30;40m- \033[0m v{}
        """.format(
            repo_yaml["type"].title(),
            repo_yaml["name"],
            repo_yaml["author"],
            repo_yaml["version"],
        )
    )

    # checks if the "read_me" flag is True
    if not read_me:
        print(
            "\n\033[0;35;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(
                repo_yaml["desc"]
            )
        )
    else:

        # Send an HTTP request to the GitHub API to get the README.md of a package
        package_md = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/README.md".format(
                package_name
            )
        ).text

        # prints and formats the Markdown file
        print(
            "\n\033[0;35;40m Package's README.MD file \033[0m:033[1;30;40m:\033[0m\n{}"
        ).format(console.print(Markdown(package_md)))

    # __________________________ #


# Adding the "find" & "install" command
fluoly.add_command(install)
fluoly.add_command(find)

# __________________________#

if __name__ == "__main__":
    fluoly(prog_name="fluoly")
