# filename: sendMessageToRoom.py
import requests
import json
access_token = 'ZGJhNWZjODEtOTU3MS00MjI2LWI4NjAtZGJiY2MyMmU1MDQ1MzhmZGRmYWEtYzcw_P0A1_5998ff09-9c27-4407-818f-2305709e8d49'
url = 'https://webexapis.com/v1/messages'

headers = {
   'Authorization': 'Bearer {}'.format(access_token),
   'Content-Type': 'application/json'
}
data = {'roomId': 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNzFmODljYTAtOGQxOS0xMWVjLTlkNTMtNzM5MTM0ZjlhOGVi',
         'markdown': 'Here are my screenshots of netacad-devasc skill-based exam'
}
res = requests.post(url, headers=headers, json=data)
print(res)
print(res.json)
print(json.dumps(res.json(), indent=4))

