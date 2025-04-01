from GET import get
from POST import post
from PUT import put
from PATCH import patch
from DELETE import delete
from HEAD import head

base_url="https://jsonplaceholder.typicode.com"
def main():
    print("printing http methods")

    get(base_url)
    post(base_url)
    put(base_url)
    patch(base_url)
    delete(base_url)
    head(base_url)

if __name__=="__main__":
    main()