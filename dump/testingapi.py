import requests
import urllib

values = """
  {
    "query": "{ me { id name } }"
  }
"""

payload = "{\"query\":\"{ me { name } }\"}"

headers = {
  #'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozNDQ5OTMsImVtYWlsIjoiZWR1YXJkby5udW5lc0BoaWRyb3Njb25zdWx0b3JpYS5jb20uYnIiLCJhcHBsaWNhdGlvbiI6MjU2MDh9fQ.shCe2EivVt1qAku5xOewnqij62jn6eIL7q8DamINRzUPTfcuCPS3Ehrs8fxv35oCaUPgIVwc1qcbisomGl75Bg'
}
#url = 'https://app.pipefy.com/queries'
url = "https://api.pipefy.com/graphql"
request = requests.request("GET",url , data=payload, headers=headers)

print(request.text)

#response_body = urllib.request.urlopen(request).read()
#print (response_body)
