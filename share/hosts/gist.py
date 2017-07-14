from os.path import basename
from requests import post

url = "https://api.github.com/gists"


def upload(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()

    file_name = basename(file_path)

    payload = {
        "public": True,
        "files": {
            file_name: {
                "content": file_contents
            }
        }
    }

    headers = {
        "User-Agent": "tallpants"
    }

    response = post(url, headers=headers, json=payload)

    try:
        print(response.json()["html_url"])
    except Exception as e:
        print("Upload to gist failed.")
        print(e)
        exit(1)


def upload_multiple(files):
    print(files)
