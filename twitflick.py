import imdb
import twitter
import sentiment

from utils import avg
from itertools import imap
from functools import partial

def twitflick():
    movie_titles = imdb.box_office_titles()    
    movie_tweets = imap(twitter.tweets_for, movie_titles)
    movie_tweet_text = imap( imap(lambda x: x.text, tweets), movie_tweets ) 
    movie_sentiments = imap( imap(sentiment.sentiment, tweet_texts), movie_tweet_text)
    avg_movie_sentiments = imap(avg, movie_sentiments)
    movie_ratings = imap(lambda x: remap(x, sentiment.min, sentiment.max, rating_min, rating_max), avg_movie_sentiments)
    movie_ratings = imap(round, movie_ratings)

    movie_title_ratings = zip(movie_titles, movie_ratings)
    print movie_title_ratings

if __name__ == "__main__":
    twitflick()
