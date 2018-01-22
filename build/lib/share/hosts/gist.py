from os.path import basename
from requests import post

__url = "https://api.github.com/gists"

__headers = {
    "User-Agent": "tallpants"
}

__payload = {
    "public": True,
    "files": {}
}


def __add_file_to_payload(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()

    file_name = basename(file_path)

    __payload["files"][file_name] = {
        "content": file_contents
    }


def __post_payload():
    response = post(__url, headers=__headers, json=__payload)

    try:
        print(response.json()["html_url"])
    except Exception as e:
        print("Upload to gist failed.")
        print(e)
        exit(1)


def upload(file_path):
    __add_file_to_payload(file_path)
    __post_payload()


def upload_multiple(files):
    for file in files:
        __add_file_to_payload(file.path)

    __post_payload()
