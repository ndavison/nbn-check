import requests
import os
import json

url = f'https://places.nbnco.net.au/places/v2/details/{os.environ["LOC_ID"]}'
r = requests.get(url, headers={'referer': 'https://www.nbnco.com.au/'})
if r.ok:
    resp = r.json()
    addr = resp.get('addressDetail', {})
    if addr.get('techChangeStatus', '').lower() == 'planned':
        with open('results.json', 'w') as f:
            f.write(json.dumps(resp))
