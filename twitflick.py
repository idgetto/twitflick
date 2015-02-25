import movie
import twitter
import sentiment

from utils import avg
from itertools import imap

def twitflick():
    # lookup some new movies
    movie_titles = movie.top_box_office_titles()    

    # find some tweets about those movies
    movie_tweets = imap(twitter.tweets_for, movie_titles)
    movie_tweet_text = imap( imap(lambda x: x.text, tweets), movie_tweets ) 

    # find the average sentiment of those tweets
    movie_sentiments = imap( imap(sentiment.sentiment, tweet_texts), movie_tweet_text)
    avg_movie_sentiments = imap(avg, movie_sentiments)

    # remap the sentiments to a movie rating
    movie_ratings = imap(sentiment_to_rating, avg_movie_sentiments)

    movie_title_ratings = zip(movie_titles, movie_ratings)
    print movie_title_ratings

def sentiment_to_rating(sentiment):
    """ converts a sentiment to a movie rating
    >>> sentiment_to_rating(1)
    5
    >>> sentiment_to_rating(-1)
    0
    >>> sentiment_to_rating(0)
    3
    """
    rating_min = 0
    rating_max = 5
    rating = remap(sentiment, sentiment.min, sentiment.max, rating_min, rating_max)
    return round(rating)

if __name__ == "__main__":
    twitflick()
