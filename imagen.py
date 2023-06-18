import os
import sys
import requests

sea = sys.argv[1]
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "comf.vbs")

for x in range(5):
    url = f"https://source.unsplash.com/random/200x200/?{sea}"
    r = requests.get(url, allow_redirects=True)
    open(f'images\{sea}{x}.png', 'wb').write(r.content)

os.startfile(file_path)
