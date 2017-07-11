from os.path import basename as __basename, getsize as __getsize
from math import ceil as __ceil


def upload_single(file_path, args):
    try:
        size_mb = __ceil(__getsize(file_path) / 1000000)
    except OSError as e:
        print("The file does not exist or is inaccessible")
        exit(1)

    if size_mb > 1024:
        print("File is too large (1GB limit)")
        exit(1)

    file_name = __basename(file_path)

    file_extension = None
    if len(file_name.split(".")) >= 2:
        file_extension = file_name.split(".")[-1]
    else:
        if not file_name.startswith("."):
            file_extension = ""
        else:
            file_extension = file_name[1:]

    from . import hosts, extensions

    host = None

    if args.host:
        if args.host == "imgur":
            host = hosts.imgur
        elif args.host == "gist":
            host = hosts.gist
        elif args.host == "anonfile":
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
