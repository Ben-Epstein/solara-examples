from setuptools import setup


with open("requirements.txt", "r") as dependencies_file:
    DEPENDENCIES = dependencies_file.readlines()

setup(
    name="gpt-qa",
    install_requires=DEPENDENCIES,
    version="0.0.0"
)