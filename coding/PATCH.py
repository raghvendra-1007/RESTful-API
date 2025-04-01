import requests
def patch(base_url):
    url=f"{base_url}/users/2"
    payload={
        'name': 'Raghav',
    }
    response=requests.patch(url,json=payload,timeout=5)
    response.raise_for_status()
    data=response.json()
    print("patch response - ")
    print(data)
    return data