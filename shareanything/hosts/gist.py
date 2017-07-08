from requests import post


def upload(filename, filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()

    payload = {
        "public": True,
        "files": {
            filename: {
                "content": file_contents
            }
        }
    }

    headers = {
        "User-Agent": "tallpants"
    }

    response = post("https://api.github.com/gists",
                    headers=headers, json=payload)
    try:
        return response.json()["html_url"]
    except Exception as e:
        print("Upload to Gist failed")
        print(e)


print(upload('test.py', './test.py'))
