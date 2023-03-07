import requests

url = "https://textapis.p.rapidapi.com/sentiment"

payload = {"text": "Android Developer"}
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "YJf4cjWDY1mshQhnCYGpFYPUrG4Hp1lTGxIjsnfJ3SKTrqeH5f",
	"X-RapidAPI-Host": "textapis.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)