from setuptools import setup, find_packages, setup

with open("README") as f:
    long_description = f.read()

setup(
    name="sort-photo",
    version="0.1",
    packages=find_packages(include=['sort-photo', 'sort-photo.*']),
    description="SortPhoto is a lightweight, dependency-free image sorting tool that organizes your photos by date or file type",
    url="https://github.com/jharri34/sort-photo",
    author="jharri34",
    long_description=long_description,
    install_requires=[],
    setup_requires=[],
    test_requires=[],
    tests_suite="tests",
)