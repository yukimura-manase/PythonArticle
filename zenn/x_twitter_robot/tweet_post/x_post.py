import tweepy

# 認証情報
consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''
bearer_token = ''


print('X Post Test 実行')

# X API V2 対応 の X Client
client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token=access_token_key,
    access_token_secret=access_token_secret
)

print('client')
print(client)

# 投稿
client.create_tweet(text="自動投稿・Test Hello World！")
