#!/usr/bin/env python

import os, re, random, tweepy
from time import gmtime, strftime
from wordfilter import Wordfilter
from offensive import tact
from secrets import *



# Bot configuration
bot_username = 'dreamy_bot_'
logfile_name = bot_username + ".log"


# Twitter authentication
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)
tweets = tweepy.Cursor(api.user_timeline).items()

wordfilter = Wordfilter()
amp = re.compile(r"amp;", re.IGNORECASE)

# Check for mention of "it was just a dream" or "woke up"
fourth_wall = re.compile(r"dream|woke|somebody love(d|s) me", re.IGNORECASE)


data = {'dreams':
            ['"I dreamt that"']
        }


def get_tweet():
    """Get a list of tweets matching the search query."""
    query = random.choice(data['dreams'])
    results = api.search(q=query, count=50)
    return results


def filter_tweets(tweets_):
    """Filter out tweets to avoid mentions, offensive content, etc. """
    while True:
        tweet_ = tweets_.pop(0)
        text = tweet_.text
        if len(tweets_) == 0:
            return
        if not (hasattr(tweet_, "retweeted_status") or
                tweet_.in_reply_to_status_id or
                tweet_.in_reply_to_screen_name or
                tweet_.truncated or
                '@' in text or
                'RT' in text or
                '#' in text or wordfilter.blacklisted(text) or
                not tact(text)):
            if process(text):
                break
            else:
                continue


def process(text_):
    print("\ntext_")
    print(text_)
    if "dreamt that " not in text_:
        return False
    else:
        trunc = text_.split("dreamt that ", 1)[1]
        print("\ntrunc")
        print(trunc)
        trunc = trunc.encode('utf-8').translate(None, "'\"")
        trunc = re.sub(amp, "", trunc)
        if tweet(trunc):
            return True


def tweet(text_):
    if re.search(fourth_wall, text_) is not None:
        return False

    for tweet in tweets:
        if text_ == tweet.text:
            return False

    # Send the tweet and log success or failure
    try:
        api.update_status(text_)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text_)
        return True


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " %s" % message)


if __name__ == "__main__":
    results = get_tweet()
    tweet = filter_tweets(results)

