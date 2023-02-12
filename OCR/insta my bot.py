
from instabot import Bot
import os
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
bot=Bot()
bot.login(username="ufk_clothing",password="Whatsappnigga93909390")
#bot.unfollow_non_followers()
print('ere')
try:
    bot.upload_video(r"C:\Users\umaRf\PycharmProjects\djangopractise\OCR\0Feb-09-2023.mp4")
except PermissionError:
    print('pass')

bot.download_video(r'https://www.instagram.com/reel/CnuPsQsoW2O/?utm_source=ig_web_copy_link')