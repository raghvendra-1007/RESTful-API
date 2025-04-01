import requests
def head(base_url):
    url=f"{base_url}/users/1"
    response=requests.head(url,timeout=5)
    response.raise_for_status()
    data=response.headers
    print("head response - ")
    print(data)
    return data