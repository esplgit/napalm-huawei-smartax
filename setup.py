"""setup.py file."""

from setuptools import setup, find_packages

# with open("requirements.txt", "r") as fs:
#     reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

__author__ = 'Juan Gomez <jgomez@phicus.es>'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="napalm-huawei-smartax",
    version="0.0.1",
    packages=find_packages(),
    author="Juan Gomez",
    author_email="jgomez@phicus.es",
    description="Network Automation and Programmability Abstraction Layer with Multi-vendor support,Driver for Huawei SmartAX and OLT",
    long_description_content_type="text/markdown",
    long_description=long_description,

    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/johnbarneta/napalm-huawei-smartax",
    include_package_data=True,
    install_requires=(
        'napalm==3.*',
        'netmiko==3.*',
    ),
)