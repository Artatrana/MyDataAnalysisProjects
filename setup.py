from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))


# get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()


# base requirements
install_requires = open(path.join(here, "requirements.txt")).read().strip().split("\n")


setup(
    name="MyDataAnalysisProjects",
    version="0.0.1",
    description="My Test Analysis Project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Artatrana",
    author_email="artatana.pujahari@gmail.com",
    package_dir={"": "py_util"},
    packages=find_packages(where="py_util"),
    install_requires=install_requires,
    include_package_data=True,
)
