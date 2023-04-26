import random

class SiraylatTweetSec:
    def __init__(self):
        pass

        
    def sirayla_tweet_sec(self, i):

        with open("hashtaglar.txt", "r") as file:
            hashtags = file.readlines()

        with open("tweetler.txt", "r") as file:
            tweets = file.readlines()

        with open("mentionlar.txt", "r") as file:
            mentions = file.readlines()
        random_tweet = (tweets[i]).strip()
        available_mentions = list(set(mentions))
        if len(available_mentions) > 0:
            num_mentions = min(len(available_mentions), 5)
            random_mentions = random.sample(available_mentions, num_mentions)
            mentions_str = " ".join([f"@{m.strip()}" for m in random_mentions])
        else:
            mentions_str = ""
        available_hashtags = list(set(hashtags))
        if len(available_hashtags) > 0:
            num_hashtags = min(len(available_hashtags), 5)
            random_hashtags = random.sample(available_hashtags, num_hashtags)
            hashtags_str = " ".join([f"#{h.strip()}" for h in random_hashtags])
        else:
            hashtags_str = ""
        new_tweet = f"{random_tweet} {mentions_str} {hashtags_str}."
        while len(new_tweet) > 280:
            if len(mentions_str) > 0:
                mentions_list = mentions_str.split()
                mentions_list.pop()
                mentions_str = " ".join(mentions_list)
            elif len(hashtags_str) > 0:
                hashtags_list = hashtags_str.split()
                hashtags_list.pop()
                hashtags_str = " ".join(hashtags_list)
            else:
                break
            new_tweet = f"{random_tweet} {mentions_str} {hashtags_str}."

        return new_tweet