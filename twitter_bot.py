import tweepy

auth = tweepy.OAuth1UserHandler('JIDc7k3FSCv2jpL5Kxu38V19D','QONtZCYLis17y33nc26D7d2BrkNh5xFOjzeonk3bgspgbt7y40')
auth.set_access_token('1467746464034181123-pE6ZIF8NySjuudtBXu4f3UriruzPgr','wlQupzIR4xit34eQDnID4jxTb41YMzcOyDRRDZSUiEzk0')
api=tweepy.API(auth)
user = api.verify_credentials()
print(user.followers_count)