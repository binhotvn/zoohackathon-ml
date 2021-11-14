import requests
def crawl_fb(usid,accessToken): 
    r = requests.get("https://graph.facebook.com/"+str(usid)+"/posts?access_token="+str(access_token))
    return r.json()

access_token = "EAAAAUaZA8jlABAOoykXsAlYUAz0XlsJ5x8rWpyPTUC6Iog2nZBczkdqYZAjUZBSTMFU01sW8uetItudcQBEaWsZBbaW7jcBZCSTOM37ZCvZA8aPdNMvi4uZBfQA4IyFZBeFiY05LC8aCQaojpbWk3kZAp5kUzSzoO66hMigcqQyVM4fYjCZBjad1DyJp3NqRZCP7GAlNxZCj3flHY7EgZDZD"
usid = "105547491951088"
url = "30.102.5.4"

#run script for crawl data server
try:
    while True:
        dataAfter = crawl_fb(usid,access_token)
        r = requests.post(url,dataAfter)
except:
    print("There are some problem")
