from argparse import ArgumentParser

from share.upload_single import upload_single
from share.upload_multiple import upload_multiple


parser = ArgumentParser(
    description="Upload a file to a sharing service and print a URL to it",
    usage="share FILE [-h] [--host HOST]"
)

parser.add_argument("file", nargs="*", help="path to the file to upload")
parser.add_argument("--host", help="explicitly specify the host to use")


def main():
    args = parser.parse_args()


    if len(args.file) == 0:
        print("No file(s) specified.")
        exit(1)
    elif len(args.file) == 1:
        upload_single(args.file[0], args.host)
    else:
        upload_multiple(args.file, args.host)


if __name__ == "__main__":
    main()
