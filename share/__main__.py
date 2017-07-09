from os.path import basename, getsize
from math import ceil
from argparse import ArgumentParser

parser = ArgumentParser(
    description="Upload a file to a sharing service and print a URL to it",
    usage="share FILE [-h] [--host HOST]"
)

parser.add_argument("file", nargs=1, help="path to the file to upload")
parser.add_argument("--host", help="explicitly specify the host to use")
args = parser.parse_args()

if not args.file[0]:
    print("No file specified.")
    exit(1)

file_path = args.file[0]

try:
    size_mb = ceil(getsize(file_path) / 1000000)
except OSError as e:
    print("The file does not exist or is inaccessible")
    exit(1)

if size_mb > 1024:
    print("File is too large. (1GB limit)")
    exit(1)

file_name = basename(file_path)
file_extension = file_name.split(".")[-1]

from . import hosts, extensions

host = None

if args.host:
    if args.host == "imgur":
        host = hosts.imgur
    elif args.host == "gist":
        host = hosts.gist
    else:
        print("Invalid host specified. Falling back to auto-detect")

if not host:
    if size_mb <= 10 and file_extension in extensions.imgur:
        host = hosts.imgur
    elif size_mb <= 1 and file_extension in extensions.gist:
        host = hosts.gist

host.upload(file_name, file_path)
