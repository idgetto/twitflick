import movie
import twitter
import sentiment

from utils import avg
from utils import remap

from itertools import imap

def twitflick(): #Try including a docstring here. Have the function definition, function input, function output
    # lookup some new movies
    print("looking up titles")
    movie_titles = movie.top_box_office_titles()    

    # find some tweets about those movies
    print("finding relevant tweets")
    movie_tweets = imap(twitter.fuzzy_find, movie_titles)
    movie_tweet_text = [[tweet.text for tweet in tweets] for tweets in movie_tweets]
    print movie_tweet_text

    # find the average sentiment of those tweets
    print("analyzing tweets")
    movie_sentiments = ([sentiment.sentiment(tweet) for tweet in tweets] for tweets in movie_tweet_text)
    avg_movie_sentiments = imap(avg, movie_sentiments)

    # remap the sentiments to a movie rating
    movie_ratings = imap(sentiment_to_rating, avg_movie_sentiments)

    movie_title_ratings = zip(movie_titles, movie_ratings)
    print movie_title_ratings

def sentiment_to_rating(sent):
    """ converts a sentiment to a movie rating #Unit testing is cool!
    >>> sentiment_to_rating(1)
    100.0
    >>> sentiment_to_rating(-1)
    0.0
    >>> sentiment_to_rating(0)
    50.0
    """
    rating_min = 0
    rating_max = 100
    rating = remap(sent, sentiment.min(), sentiment.max(), rating_min, rating_max)
    return rating

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    twitflick()
