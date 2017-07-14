from os.path import getsize, splitext
from math import ceil
from . import hosts


def size_mb(file_path):
    try:
        val = ceil(getsize(file_path) / 1000000)
    except OSError:
        print("{0} doesn't exist or is inaccessible".format(file_path))
        exit(1)

    return val


def extension(file_path):
    return splitext(file_path)[1][1:]


def parse_host(hostname):
    if not hostname:
        return None
    elif hostname == "imgur":
        return hosts.imgur
    elif hostname == "gist":
        return hosts.gist
    elif hostname == "anonfile":
        return hosts.anonfile
    else:
        print("Invalid host specified.")
        exit(1)
