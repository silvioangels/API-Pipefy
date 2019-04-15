import requests
import urllib.request
import json

id = 20780772

values = """
  {
    "query": "{ card(id: """ + str(id) + """) { title assignees { id } comments { id } comments_count current_phase { name } done due_date fields { name value } labels { name } phases_history { phase { name } firstTimeIn lastTimeOut } url } }"
}
"""

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozNDQ5OTMsImVtYWlsIjoiZWR1YXJkby5udW5lc0BoaWRyb3Njb25zdWx0b3JpYS5jb20uYnIiLCJhcHBsaWNhdGlvbiI6MjU2MDh9fQ.shCe2EivVt1qAku5xOewnqij62jn6eIL7q8DamINRzUPTfcuCPS3Ehrs8fxv35oCaUPgIVwc1qcbisomGl75Bg'
}

request = requests.request("POST",url = 'https://app.pipefy.com/queries', data=values, headers=headers)

data = request.text

datajson = json.loads(data)

print(datajson['data']["card"]["current_phase"]["name"])
print(datajson['data']["card"]["fields"][0]['value'])