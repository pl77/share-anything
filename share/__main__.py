from argparse import ArgumentParser


parser = ArgumentParser(
    description="Upload a file to a sharing service and print a URL to it",
    usage="share FILE [-h] [--host HOST]"
)

parser.add_argument("file", nargs=1, help="path to the file to upload")
parser.add_argument("--host", help="explicitly specify the host to use")
args = parser.parse_args()


if len(args.file) == 0:
    print("No file(s) specified.")
    exit(1)
elif len(args.file) == 1:
    from .upload_single import upload_single
    upload_single(args.file[0], args.host)
