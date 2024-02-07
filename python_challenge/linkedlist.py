import requests

BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"



def payload(next_value):
    return {"nothing" : f"{next_value}"}

# w/o sessions the requests send many requests, that is slower
def fetch_with_session(session : requests.Session, next_value: str):
    response = session.get(BASE_URL, params=payload(next_value))
    return response
    
    
def get_next_value(response_data: str) -> str:
    resp_arr = response_data.split(" ")
    return [x for x in resp_arr if str.isnumeric(x)][0]


with requests.Session() as session:
    
    next_value = "44827"
    
    for i in range(400):
        try:
            
            print(f"======={i}=======")
            
            resp = fetch_with_session(session, next_value)

            print(resp)

            print(resp.text)  # and the next nothing is 45439
            
            next_value = get_next_value(resp.text)
            
            print(f"next value string: {next_value}")
        except Exception as e:
            print(e)
            print(f"final value is: {next_value}")
    
