import click
import os
import platform
import shutil


@click.command()
@click.option("--id", help="put the extension id here")
def kill(id):
    if platform.system() == "Windows":
        path = os.path.join(
            "C",
            "Users",
            os.getlogin(),
            "AppData",
            "Local",
            "Google",
            "Chrome",
            "User Data",
            "Default",
            "Extensions",
            id,
        )
    elif platform.system() == "Darwin":
        path = os.path.join(
            os.path.expanduser("~"),
            "Library",
            "Application Support",
            "Google",
            "Chrome",
            "Default",
            "Extensions",
            id,
        )
    else:
        print("Very sorry, {0} is not currently supported".format(platform.system()))
    shutil.rmtree(path=path)
    print(f"Removed extension ID {id}.")


if __name__ == "__main__":
    kill()
