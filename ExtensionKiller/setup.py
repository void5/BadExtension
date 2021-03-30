from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ExtensionKiller",
    version="0.2",
    author="Finnegan McCarthy",
    author_email="mccarthy.finnegan@gmail.com",
    description="A small script to kill a chrome extension that you specify the ID for, but it only works on Windows",
    long_description=long_description,
    url="https://github.com/void5/BadExtension",
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        killer=killer:cli
    """,
    python_requires=">=3.7",
)
