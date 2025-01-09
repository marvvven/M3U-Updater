import requests

url = "https://a5.pokaz.me/sm9O6m6fgg-RmtvoG9IE2Q/229/1736407741/index.m3u8"

response = requests.get(url)

if response.status_code == 200:
    with open('updated_playlist.m3u', 'w') as file:
        file.write(response.text)
    print("M3U file updated successfully.")
else:
    print(f"Failed to retrieve the M3U file. Status code: {response.status_code}")
