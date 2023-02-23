import requests

response = requests.get("https://bbc-news-api.vercel.app/bengali/news").json()
print(response)
print(response)