import requests
def post(base_url):
    url=f"{base_url}/users"
    payload={
    'id': 1,
        'name': 'Leanne Graham',
            'username': 'Bret',
                'email': 'Sincere@april.biz',
    }
    response=requests.post(url,json=payload,timeout=5)
    response.raise_for_status()
    data=response.json()
    print("post response - ")
    print(data)
    return data