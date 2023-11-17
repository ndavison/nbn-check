import requests
import os
import sys

url = f'https://places.nbnco.net.au/places/v2/details/{os.environ["LOC_ID"]}'
r = requests.get(url, headers={'referer': 'https://www.nbnco.com.au/'})
if r.ok:
    resp = r.json()
    addr = resp.get('addressDetail', {})
    if addr.get('techChangeStatus', '').lower() == 'planned':
        out = {'reasonCode': addr.get('reasonCode'),
               'altReasonCode': addr.get('altReasonCode'),
               'techChangeStatus': addr.get('techChangeStatus'),
               'previousTechChangeStatus': addr.get('previousTechChangeStatus')}
        print(out)
        sys.exit(1)
