# import requests
# response = requests.get("https://www.google.com")
# print(response.text)


# import requests
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'vibhu',
#     "body": 'bhai',
#     "userId":  12,
# }

# headers = {
#     'content-type': 'application/json; charset=UTF-8',
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)


import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)