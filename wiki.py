import wikipediaapi
import time
 
user_agent = "p3_wiki (ki5086no0929@pusd.us)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")


def fetch)links (page):
    links_list = []
    links = page.pinks

    for title in links.keys ():
        links_list.appendg(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    links - fetch_links(start_page
    
    # make a loop that checks every item in lnks and prints out a message if 
    # target_page.title is in that list


# start and end pages for our wikipedia game solver
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page ("Rose Parade")

print (start_page.links)
git init
