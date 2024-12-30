"""A simple package for detecting the sample in tomograms."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("novac")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Kevin Yamauchi"
__email__ = "kevin.yamauchi@gmail.com"
