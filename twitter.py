from pattern.web import Twitter

def fuzzy_find(thing):
    t = Twitter()

    fuzzy_things = fuzzy_list(thing)

    tweets = []
    for item in fuzzy_things:
        tweets += t.search(item)

    return tweets

def fuzzy_list(thing):
    things = []

    things.append(thing)
    things.append(thing.upper())
    things.append(thing.lower())
    things.append(thing.capitalize())
    things.append(thing.title())

    nospace = ''.join(thing.split())
    things.append(nospace.upper())
    things.append(nospace.lower())
    things.append(nospace.capitalize())
    things.append(nospace.title())

    return things

if __name__ == "__main__":
    print fuzzy_find('nyan cat')
