import json


def processResponse(responseObj):
  theStatusCode = responseObj.status_code
  if theStatusCode != 200:
    raise Exception(f"API CALL NOT SUCCESSFUL -- STATUS CODE {theStatusCode} NOT 200")
  msgJson = json.loads(responseObj.text)
  return msgJson
