from requests import post

__client_id = "9c65f969001905d"

__headers = {
    "authorization": "Client-ID {0}".format(__client_id)
}


def __upload_single(file_path):
    url = "https://api.imgur.com/3/image"

    file = {
        "image": open(file_path, "rb")
    }

    response = post(url, headers=__headers, files=file)
    try:
        return response.json()["data"]
    except Exception as e:
        print("Upload to imgur failed.")
        print(e)
        exit(1)


def upload(file_path):
    response_data = __upload_single(file_path)
    print(response_data["link"])


def upload_multiple(files):
    url = "https://api.imgur.com/3/album"

    deletehashes = []

    for file in files:
        upload_data = __upload_single(file.path)
        deletehashes.append(upload_data["deletehash"])

    payload = {
        "deletehashes[]": deletehashes,
        "privacy": "public",
    }

    response_data = post(url, headers=__headers, data=payload)
    try:
        album_id = response_data.json()["data"]["id"]
        print("https://imgur.com/a/{}".format(album_id))
    except Exception as e:
        print("Creating album failed.")
        print(e)
        exit(1)
