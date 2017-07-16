from collections import namedtuple

from . import helpers, hosts, extensions


def upload_multiple(file_path_list, hostname):
    FileInfo = namedtuple("FileInfo", "extension size path")
    files = []

    for file_path in file_path_list:
        size_mb = helpers.size_mb(file_path)
        file_extension = helpers.extension(file_path)

        files.append(FileInfo(extension=file_extension,
                              size=size_mb,
                              path=file_path))

        host = helpers.parse_host(hostname)

        if not host:
            if not file_extension:
                host = hosts.anonfile
            else:
                if all(file.size <= 10 and file.extension in extensions.imgur
                       for file in files):
                    host = hosts.imgur
                elif all(file.size <= 1 and file.extension in extensions.gist
                         for file in files):
                    host = hosts.gist
                else:
                    host = hosts.anonfile

    host.upload_multiple(files)
