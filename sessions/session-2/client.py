# call /users/jack and print all their tweets
#%%
import requests

response = requests.get("http://127.0.0.1:5000/users/jack")

list_of_tweets = response.json()

for tweet in list_of_tweets:
    print(tweet) 
# %%
