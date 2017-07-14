from requests import post

url = "https://anonfile.com/api/upload"


def upload(file_path):
    payload = {
        "file": open(file_path, "rb")
    }

    response = post(url, files=payload)
    try:
        print(response.json()["data"]["file"]["url"]["short"])
    except Exception as e:
        print("Upload to anonfile failed")
        print(e)
        exit(1)
