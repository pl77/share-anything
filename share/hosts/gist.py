from requests import post as __post

url = "https://api.github.com/gists"


def upload(file_name, file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()

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

    response = __post(url, headers=headers, json=payload)

    try:
        print(response.json()["html_url"])
    except Exception as e:
        print("Upload to gist failed.")
        print(e)
