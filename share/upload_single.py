from . import helpers, hosts, extensions


def upload_single(file_path, hostname):

    size_mb = helpers.size_mb(file_path)

    if size_mb > 1024:
        print("File is too large (1GB limit)")
        exit(1)

    file_extension = helpers.extension(file_path)
    host = helpers.parse_host(hostname)

    if not host:
        if not file_extension:
            host = hosts.anonfile
        elif size_mb <= 10 and file_extension in extensions.imgur:
            host = hosts.imgur
        elif size_mb <= 1 and file_extension in extensions.gist:
            host = hosts.gist
        else:
            host = hosts.anonfile

    host.upload(file_path)
