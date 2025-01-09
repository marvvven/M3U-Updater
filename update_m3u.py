import requests

# Define the URL of the M3U file (you want to fetch from)
url = "https://a5.pokaz.me/sm9O6m6fgg-RmtvoG9IE2Q/229/1736407741/index.m3u8"

# Send a request to fetch the content of the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Write the content of the M3U file
    with open('updated_playlist.m3u', 'w') as file:
        file.write(response.text)
    print("M3U file updated successfully.")
else:
    print(f"Failed to retrieve the M3U file. Status code: {response.status_code}")
