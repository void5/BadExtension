import click
import os
import shutil


@click.command()
@click.option("--id", help="put the extension id here")
def kill(id):
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
    shutil.rmtree(path=path)
    print(f"Removed extension ID {id}.")


if __name__ == "__main__":
    kill()
