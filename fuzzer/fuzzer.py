import requests
import sys
url = input("what is the target ip? ")
for word in sys.stdin:
    word = word.strip()
    res = requests.get(url=f"{url}/{word}")
    if res.status_code == 404:
        continue
    
    data = res.json()
    print (data)
    print(res.status_code)
    print(word)