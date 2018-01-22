from requests import post
from zipfile import ZipFile
from os import getcwd, remove
from share import helpers

__url = "https://anonfile.com/api/upload"


def upload(file_path):
    payload = {
        "file": open(file_path, "rb")
    }

    response = post(__url, files=payload)
    try:
        print(response.json()["data"]["file"]["url"]["short"])
    except Exception as e:
        print("Upload to anonfile failed")
        print(e)
        exit(1)


def upload_multiple(files):
    zip_name = getcwd() + ".zip"
    with ZipFile(zip_name, "w") as zip:
        for file in files:
            zip.write(file.path)

    if helpers.size_mb(zip_name) >= 5120:
        print("The zip is too large. (5GB limit)")
        remove(zip_name)
        exit(1)

    upload(zip_name)
    remove(zip_name)
