

from instascrape import Reel
import time

# session id
SESSIONID = "Paste session Id Here"

# Header with session id
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
	Safari/537.36 Edg/79.0.309.43",
	"cookie": f'sessionid={SESSIONID};'
}

# Passing Instagram reel link as argument in Reel Module
insta_reel = Reel(
	'https://scontent.cdninstagram.com/o1/v/t16/f1/m82/E048F4C08D5E4816ADD501E5D0F1B290_video_dashinit.mp4?efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uNzIwLmNsaXBzLmJhc2VsaW5lIn0&_nc_ht=instagram.fisb1-2.fna.fbcdn.net&_nc_cat=108&vs=1230557977669888_1914227201&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC9FMDQ4RjRDMDhENUU0ODE2QURENTAxRTVEMEYxQjI5MF92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVABgkR0FEN0pBY2tWcUxfMFpNQUFPNmg0V1AzM3djX2JwUjFBQUFGFQICyAEAKAAYABsAFQAAJtLqxJmTw%2FE%2FFQIoAkMzLBdAIGZmZmZmZhgSZGFzaF9iYXNlbGluZV8xX3YxEQB1%2FgcA&ccb=9-4&oh=00_AfBb4PzL1qFTTwZB0qru_a8o1ngtKTB5x1ksEXUcRjg3-g&oe=63E65D3B&_nc_sid=30a2ef')

# Using scrape function and passing the headers
insta_reel.scrape(headers=headers)

# Giving path where we want to download reel to the
# download function
insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")

# printing success Message
print('Downloaded Successfully.')
