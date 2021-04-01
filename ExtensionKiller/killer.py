import click
import os
import shutil


@click.command()
@click.option("--id", help="put the extension id here")
def kill(id):
    if os.name == "nt":
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
    elif os.name == "posix":
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
        print("Very sorry, {0} is not currently supported".format(os.name))
    shutil.rmtree(path=path)
    print(f"Removed extension ID {id}.")


if __name__ == "__main__":
    kill()
