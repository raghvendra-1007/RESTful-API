import requests
def put(base_url):
    url=f"{base_url}/users/1"
    payload={
    'id': 1,
        'name': 'Graham',
            'username': 'Brat',
                'email': 'Sincere@march.biz',
    }
    response=requests.put(url,json=payload,timeout=5)
    response.raise_for_status()
    data=response.json()
    print("put response - ")
    print(data)
    return data