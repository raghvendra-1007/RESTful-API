import requests
def delete(base_url):
    url=f"{base_url}/users/3"
    response=requests.delete(url,timeout=5)
    if response.status_code==200 or response.status_code==204:
        print("Deleted sucessful")
    else:
        print("Failed to delete")