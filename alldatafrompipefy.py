import requests
from urllib import request
import json

id = 166920

values = """
  {
    "query": "{ cards(organization_id: 166920) { name pipes { id name } } }"
}
"""

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozNDQ5OTMsImVtYWlsIjoiZWR1YXJkby5udW5lc0BoaWRyb3Njb25zdWx0b3JpYS5jb20uYnIiLCJhcHBsaWNhdGlvbiI6MjU2MDh9fQ.shCe2EivVt1qAku5xOewnqij62jn6eIL7q8DamINRzUPTfcuCPS3Ehrs8fxv35oCaUPgIVwc1qcbisomGl75Bg'
}
request = requests.request("POST", url = 'https://app.pipefy.com/queries', data=values, headers=headers)

data = request.text

datajson = json.loads(data)

print(datajson)

#print(datajson['data']['organization']['pipes'][0])

