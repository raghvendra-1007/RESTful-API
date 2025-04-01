import requests
def get(base_url):
    url=f"{base_url}/users"
    response=requests.get(url,timeout=5)
    response.raise_for_status()
    data=response.json()
    print("get response - ")
    print(data)
    return data