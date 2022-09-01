# URL Shortener Tinyurl
#### pip install pyshorteners 
import pyshorteners
# get url from user
long_url = input("Please input the url to shorten: ")

# Tiny url shortener service
typ_shortener = pyshorteners.Shortener()
short_url     = typ_shortener.tinyurl.short(long_url)

print("Short URL: " + short_url)