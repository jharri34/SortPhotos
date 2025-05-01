from setuptools import setup, find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="sortphoto",
    version="0.1",
    packages=find_packages(include=['sortphoto', 'sortphoto.*']),
    description="sortphoto is a lightweight, dependency-free image sorting tool that organizes your photos by date or file type",
    url="https://github.com/jharri34/sortphoto",
    author="jharri34",
    long_description=long_description,
    install_requires=[],
    setup_requires=[],
    test_requires=[],
    tests_suite="tests",
)