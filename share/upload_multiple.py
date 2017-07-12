from os.path import basename, getsize
from math import ceil
from collections import namedtuple


def upload_multiple(file_path_list, hostname):
    FileInfo = namedtuple("FileInfo", "name extension size path")
    files = []

    for file_path in file_path_list:
        try:
            size_mb = ceil(getsize(file_path) / 1000000)
        except OSError as e:
            print("{} does not exist or is inaccessible.".format(file_path))
            exit(1)

        file_name = basename(file_path)

        file_extension = ""
        if len(file_name.split(".")) >= 2:
            file_extension = file_name.split(".")[-1]

        files.append(FileInfo(name=file_name,
                              extension=file_extension,
                              size=size_mb,
                              path=file_path))

        from . import hosts, extensions

        host = None

        if hostname:
            if hostname == "imgur":
                host = hosts.imgur
            elif hostname == "gist":
                host = hosts.gist
            elif hostname == "anonfile":
                print("Multiple uploads to a file host aren't supported yet.")
                exit(1)
            else:
                print("Invalid host specified. Falling back to auto-detect")

        if not host:
            if not file_extension:
                print(
                    "Can't upload these. Try zipping them up and uploading the zip file.")
                exit(1)
            else:
                if all((file.size <= 10 and file.extension in extensions.imgur) for file in files):
                    host = hosts.imgur
                elif all((file.size <= 1 and file.extension in extensions.gist) for file in files):
                    host = hosts.gist
                else:
                    print("You can upload either all text files or all image files. " +
                          "Try zipping these files up and uploading the zip file.")
                    exit(1)

    host.upload_multiple(files)
