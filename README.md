dreamy-bot
==========

**Note**: dreamy-bot is a work in progress.

dreamy-bot is a Twitter bot that searches for tweets with phrases like "Last night I dreamt that" or "I dreamt" and then tweets only what follows those phrases — turning dreams into realities.

## Requires ##
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) for HTML parsing
* [TextBlob](http://textblob.readthedocs.io/en/dev/index.html) for POS tagging, noun phrase extraction, and sentiment analysis
* [wordfilter](https://github.com/dariusk/wordfilter) for filtering bad words 
* [tweepy](https://github.com/tweepy/tweepy) for Tweeting
* [pycorpora](https://github.com/aparrish/pycorpora) for extra filtering using [Darius Kazemi's Corpora Project](https://github.com/dariusk/corpora)

##License

dreamy-bot is licensed under the MIT License. See LICENSE for more information.