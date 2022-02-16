# filename: createWebexRoom.py
import requests
import json
access_token = 'N2E4YjRmZjItZWZlOC00MDljLTlhODAtZDI1NDM5OGY5OTAyY2ViYjQ1ZWEtMDc2_P0A1_5998ff09-9c27-4407-818f-2305709e8d49'
url = 'https://webexapis.com/v1/rooms'

headers = {
   'Authorization': 'Bearer {}'.format(access_token),
   'Content-Type': 'application/json'
}
data = {'title': 'netacad_devasc_skills_JvdH'}
res = requests.post(url, headers=headers, json=data)
print(res)
print(json.dumps(res.json(), indent=4))

