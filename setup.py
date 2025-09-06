from setuptools import setup, find_packages

with open("requirement.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "Anime_Recommender",
    version = "0.1",
    author = "Yunfei",
    packages = find_packages(),
    install_requires = requirements,
)