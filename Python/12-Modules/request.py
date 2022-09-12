import requests
r = requests.get("https://www.w3schools.com")
print(r.status_code)
# print(r.text)