# ________Modules__________ #

import os
import sys
import platform
import atexit
import yaml
import click
import requests

# __________________________ #

__VERSION__ = "0.1.1"

# __________________________ #


class PackageNotFound(Exception):
    pass


# ___Exit Handling Stuff____ #


def exit_handler():
    print("\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m\033[92m √ Done!\033[0m\n")


# __________________________ #

proc_arch = platform.machine()
os_type = platform.system()

# __________________________ #


def download(download_link):

    filename = download_link.split("/")[-1]

    if os.path.isfile(filename):
        user_input = input(
            "\033[1;33;40m Warning \033[0m\033[1;30;40m- \033[0m The following file already exists, do you want to delete it (Y/n)? "
        )
        print("")

        if user_input == "Y" or "y":
            os.remove(filename)
    try:
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
                    done = int(65 * downloaded / total)
                    percentage = int(downloaded * 100 / total)
                    sys.stdout.write(
                        "\r {}% |{}{}| \033[0;33;40mSize:\033[0m {} \033[2;37;40m/\033[0m {} MB ".format(
                            percentage,
                            "\033[92m█\033[0m" * done,
                            " " * (65 - done),
                            downloaded / 1000000,
                            total / 1000000,
                        )
                    )
                    sys.stdout.flush()
    except KeyboardInterrupt:
        os.remove(filename)

    sys.stdout.write("\n")


# __________________________ #

print("\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m 🌿 \x1B[3mFluoly\x1B[0m\n")

load_repo = requests.get(
    "https://api.github.com/repos/retr0cube/fluoly/releases/latest"
)

repo_json = load_repo.json()["name"]

if repo_json != __VERSION__:
    print(
        "\033[1;33;40m /!\ Warning /!\ You're using v{}, But v{} is the newest version available\033[0m".format(
            __VERSION__, repo_json
        )
    )

# __________________________ #


@click.group()
def fluoly():
    """An Open Source Library/Repo of Add-ons, Tools... for Minecraft: Bedrock Edition."""


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
@click.argument("package_name")
def install(version, package_name, cpu_arch, sys):

    """Installs an Package."""
    atexit.register(exit_handler)

    # __________________________ #

    if not os.path.isdir("downloads"):
        os.mkdir("downloads")
    os.chdir("downloads")

    # __________________________ #

    try:
        load_yaml = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}.info.yaml".format(
                package_name, package_name
            )
        ).text

        repo_yaml = yaml.safe_load(load_yaml)

    except requests.exceptions.InvalidURL:
        raise PackageNotFound(
            " Can't find package with name '{}'\n".format(package_name)
        )

    # __________________________ #

    print(
        "\n\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_yaml["name"]
        )
    )

    # __________________________ #

    print(
        "\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_yaml["author"]
        )
    )

    # __________________________ #

    if version is not None:
        repo_yaml["version"] = version

    # __________________________ #

    package_installer = requests.get(
        "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}/{}.installer.yaml".format(
            package_name, repo_yaml["version"], package_name
        )
    ).text

    package_yaml = yaml.safe_load(package_installer)

    # __________________________ #

    print(
        "\n\033[1;35;40m Info \033[0m\033[1;30;40m- \033[0m Instaling {} {}...\n".format(
            repo_yaml["name"], package_yaml["package_version"]
        )
    )

    # __________________________ #

    if repo_yaml["type"] == "tool":

        if cpu_arch is not None:
            proc_arch is cpu_arch

        if os is not None:
            os_type is sys

        try:
            download(package_yaml[os_type][proc_arch])
        except KeyError:
            download(package_yaml[os_type]["Universal"])

    # __________________________ #

    elif repo_yaml["type"] == "addon" or "plugin":

        download(package_yaml["download_link"])

    # __________________________ #


@click.command()
@click.argument("package_name")
def show(package_name):
    """Shows info about an Add-on."""

    # __________________________ #

    try:
        load_yaml = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/{}.info.yaml".format(
                package_name, package_name
            )
        ).text

        repo_yaml = yaml.safe_load(load_yaml)

    except Exception:
        raise PackageNotFound(
            " Can't find package with name '{}'\n".format(package_name)
        )

    # __________________________ #

    print(
        "\033[1;36;40m Package Type \033[0m\033[1;30;40m- \033[0m {}\n".format(
            repo_yaml["type"].title()
        )
    )

    print(
        "\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_yaml["name"]
        )
    )
    print(
        "\033[0;35;40m Author \033[0m\033[1;30;40m- \033[0m {}".format(
            repo_yaml["author"]
        )
    )
    print(
        "\033[1;36;40m Latest Version \033[0m\033[1;30;40m- \033[0m v{}".format(
            repo_yaml["version"]
        )
    )
    print(
        "\n\033[0;35;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(
            repo_yaml["desc"]
        )
    )

    # __________________________ #


fluoly.add_command(install)
fluoly.add_command(show)

# __________________________#

if __name__ == "__main__":
    fluoly(prog_name="fluoly")
