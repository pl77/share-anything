from requests import post

client_id = "9c65f969001905d"
url = "https://api.imgur.com/3/image"


def upload(file_name, file_path):
    file = {
        "image": open(file_path, "rb")
    }

    headers = {
        "authorization": "Client-ID {0}".format(client_id)
    }

    response = post(url, headers=headers, files=file)
    try:
        print(response.json()["data"]["link"])
    except Exception as e:
        print("Upload to imgur failed")
        print(e)
        exit(1)


def upload_multiple(files):
    print(files)
