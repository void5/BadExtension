from setuptools import setup, find_packages

setup(
    name='ExtensionKiller',
    version='0.1',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        killer=killer:cli
    ''',
)