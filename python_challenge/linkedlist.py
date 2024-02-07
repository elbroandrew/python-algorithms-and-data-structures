import requests

BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

payload = {"nothing" : "44827"}


# w/o sessions the requests send many request, that is slower
def fetch_with_session(session : requests.Session):
    response = session.get(BASE_URL, params=payload)
    return response
    

with requests.Session() as session:
    resp = fetch_with_session(session)

    print(resp)

    print(resp.text)