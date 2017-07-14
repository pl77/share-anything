from os.path import basename, getsize, splitext
from math import ceil


def upload_single(file_path, hostname):
    try:
        size_mb = ceil(getsize(file_path) / 1000000)
    except OSError as e:
        print("The file does not exist or is inaccessible.")
        exit(1)

    if size_mb > 1024:
        print("File is too large (1GB limit)")
        exit(1)

    file_name = basename(file_path)

    file_extension = splitext(file_path)[1][1:]

    from . import hosts, extensions

    host = None

    if hostname:
        if hostname == "imgur":
            host = hosts.imgur
        elif hostname == "gist":
            host = hosts.gist
        elif hostname == "anonfile":
            host = hosts.anonfile
        else:
            print("Invalid host specified. Falling back to auto-detect")

    if not host:
        if not file_extension:
            host = hosts.anonfile
        elif size_mb <= 10 and file_extension in extensions.imgur:
            host = hosts.imgur
        elif size_mb <= 1 and file_extension in extensions.gist:
            host = hosts.gist
        else:
            host = hosts.anonfile

    host.upload(file_name, file_path)
