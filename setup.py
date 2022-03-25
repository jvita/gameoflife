from setuptools import setup, find_packages

setup(
    name='gameoflife',
    version='0.0.1',
    packages=find_packages(include=['gameoflife', 'gameoflife.*']),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': ['run-game-of-life=gameoflife.main:main']
    }
)