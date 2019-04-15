import request

#url = "https://api.pipefy.com/graphql"

values = """
  {
    "query": "{ me { id name username email avatar_url created_at locale time_zone } }"
  }
"""

payload = "{\"query\":\"{me {name}}\"}"
headers = {'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozNDQ5OTMsImVtYWlsIjoiZWR1YXJkby5udW5lc0BoaWRyb3Njb25zdWx0b3JpYS5jb20uYnIiLCJhcHBsaWNhdGlvbiI6MjU2MDh9fQ.shCe2EivVt1qAku5xOewnqij62jn6eIL7q8DamINRzUPTfcuCPS3Ehrs8fxv35oCaUPgIVwc1qcbisomGl75Bg',
           'Content-Type':'application/json',
           'Content-Type':'charset=utf-8' }

#response = requests.request("POST", url, data=payload, headers=headers)
request = Request('https://app.pipefy.com/queries', data=values, headers=headers)

#print(response.text)

print(request.text)

