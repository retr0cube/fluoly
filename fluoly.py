# ________Modules__________ #

import os
import sys
import platform
import atexit
import time

import requests
import yaml
import click

# __________________________ #

__VERSION__ = "0.1.2"

start = time.perf_counter()

proc_arch = platform.machine()
os_type = platform.system()

# __________________________ #


class PackageNotFound(Exception):
    pass


# __________________________ #


def download(download_link, filename):

    if filename == "default":
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
                            "%.4f" % (downloaded / 1000000),
                            "%.4f" % (total / 1000000),
                        )
                    )
                    sys.stdout.flush()

        atexit.register(exit_handler)

    except KeyboardInterrupt:
        os.remove(filename)
        print("\n\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m Aborted !")

    sys.stdout.write("\n")


# __________________________ #

print(
    "\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m 🌿 \x1B[3mFluoly \x1B[0m\033[1;30;40m-\033[0m v{}\n".format(
        __VERSION__
    )
)

load_repo = requests.get(
    "https://api.github.com/repos/retr0cube/fluoly/releases/latest"
)

repo_json = load_repo.json()["name"]

if repo_json != __VERSION__:
    print(
        "\033[1;33;40m /!\ Warning /!\ You're using v{}, But v{} is the newest version available\033[0m\n".format(
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

    if path is not None and os.path.isdir(path):
        os.chdir(r"{}".format(path))

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
        "\033[1;36;40m Package Name \033[0m\033[1;30;40m- \033[0m {}".format(
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
            if name is not None:
                download(package_yaml[os_type][proc_arch], name)
            else:
                download(package_yaml[os_type][proc_arch], "default")
        except KeyError:
            if name is not None:
                download(package_yaml[os_type]["Universal"], name)
            else:
                download(package_yaml[os_type]["Universal"], "default")

    # __________________________ #

    elif repo_yaml["type"] == "addon" or "plugin":

        if name is not None:
            download(package_yaml["download_link"], name)
        else:
            download(package_yaml["download_link"], "default")


# ___Exit Handling Stuff____ #


def exit_handler():
    finish = time.perf_counter()

    print(
        "\n\033[0;32;40m Info \033[0m\033[1;30;40m- \033[0m\033[92m √ Done in {}s !\033[0m\n".format(
            "%.3f" % (finish - start)
        )
    )


# __________________________ #


@click.command()
@click.option("--read_me", "-md", help="Shows the README.md of a package")
@click.argument("package_name")
def find(package_name, read_me):
    """Shows info about a Package."""

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

    if read_me is None:
        print(
            "\n\033[0;35;40m Package Description \033[0m\033[1;30;40m- \033[0m {}\n".format(
                repo_yaml["desc"]
            )
        )
    elif read_me is not None:

        package_md = requests.get(
            "https://raw.githubusercontent.com/retr0cube/fluoly/master/packages/{}/README.md".format(
                package_name
            )
        ).text

        print(
            "\n\033[0;35;40m Package's README.MD file \033[0m\033[1;30;40m-\n\033[0m{}\n".format(
                package_md
            )
        )

    # __________________________ #


fluoly.add_command(install)
fluoly.add_command(find)

# __________________________#

if __name__ == "__main__":
    fluoly(prog_name="fluoly")
