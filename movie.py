from pattern.web import URL
from pattern.web import DOM

BOX_OFFICE_URL = 'http://www.fandango.com/boxoffice'

def box_office_titles():
    # download the webpage
    html = URL(BOX_OFFICE_URL).download() 
    dom = DOM(html)

    # find the movie titles
    title_elements = dom('td.movieTitle a')
    titles = map(lambda x: x.content, title_elements)
    
    return titles

def top_box_office_titles():
    return box_office_titles()[:10]

if __name__ == "__main__":
    print top_box_office_titles()
