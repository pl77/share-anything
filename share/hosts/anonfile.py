from requests import post as __post

__url = "https://anonfile.com/api/upload"


def upload(file_name, file_path):
    payload = {
        "file": open(file_path, "rb")
    }

    response = __post(__url, files=payload)
    try:
        print(response.json()["data"]["file"]["url"]["short"])
    except Exception as e:
        print("Upload to anonfile failed")
        print(e)
        exit(1)
