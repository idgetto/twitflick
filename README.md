twitflick
=========

## Overview ##

twitflick uses two data sources in order to rate top box office movies. First, twitflick compiles a list of the top movies by grabbing html from [fandango]('http://www.fandango.com/boxoffice'). Then it proceeds to find hundreds of tweets that mention these films. These tweets are then analyzed for positive or negative sentiment. Finally, an average sentiment is calculated and mapped to a movie rating.

## Implementation ##

The implimentation of twitflick is quite procedural. First we gather a list of movie titles. For each of those titles, we find a list of relevant tweets. From those tweets an average sentiment is gathered about the corresponding movie. This sentiment is then converted to a movie rating. 

In order to do this, lists are used heavily. Lists are used to store the movie titles, tweets, average sentiments, and movie ratings. While tweets are stored in a list, I initially thought to store them in a set. I planned to do this because I am only looking for unique tweets; duplicates would skew the average rating. Although sets would have provided a simple way to ensure uniqueness, they only work by comparing hash value. Unfortunately the twitter api I am using returns results that not hashable. As a result I resorted to using a list and only adding new tweets to it if their id was not currently within it. While a set implemented with a hash table might provide O(1) constant efficiency insertion, my list implementation requires O(n) time. I'm not too worried about this efficiency loss because the implementation is simple and could be changed later. Also, this is implemented in python, so who cares about efficiency. 

## Results ##

|        Title                             | twitflick rating | Metacritic rating | percent error |
|------------------------------------------|:----------------:|:-----------------:|:-------------:|
| Fifty Shades of Grey                     |        53        |        46         |       15      |
| Kingsman: The Secret Service             |        45        |        59         |       24      |
| The SpongeBob Movie: Sponge Out of Water |        53        |        63         |       16      |
| McFarland, USA                           |        58        |        60         |       3       |
| The DUFF                                 |        57        |        56         |       2       |
| American Sniper                          |        50        |        48         |       4       |
| Hot Tub Time Machine 2                   |        60        |        29         |       107     |
| Jupiter Ascending (2015)                 |        53        |        40         |       33      |
| The Imitation Game                       |        50        |        73         |       32      |
| Paddington                               |        54        |        77         |       30      |

We are able to compare the ratings found by twitflick to those by Metacritic for the current top ten box office films. We can see that there are a wide range of results. The DUFF, McFarland, USA, and American Sniper all were predicted within 5% error. On the other hand, Hot Tub Time Machine 2 was predicted with a error greater that 100%. The average error of this set of movies comes out to 27%. With this level of accuracy I have little confidence in twitflick's movie rating abilities.

It is also important to consider how close to 50 each of twitflicks ratings are. In fact, the average twitflick rating is 53. This suggests that the sentiment of the analyzed tweets often comes out to 50% positivity.

## Reflection ##

If I were to continue with this project, I would take a closer look at how the sentiments are being calculated. I would also examine more closely the set of tweets that are analyzed. Looking back, I wish I knew that some websites would be more difficult than others to extract data from. If I were to do it again, I would have spent more time looking for sources that provide tags and ids within their html that make scraping easy. Finally, I would have started earlier so that I would have more time to improve the prediction's success rate.
