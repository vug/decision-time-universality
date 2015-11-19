import requests
from bs4 import BeautifulSoup
import random

# set the number of words to query
nWords = 2000

# use the dictionary that comes with unix systems
fp = open('/usr/share/dict/web2', 'rt')
dictionary = fp.readlines()
fp.close()

# shuffle the dictonary and choose first nWords words
idxs = range(len(dictionary))
random.shuffle(idxs)
idxs = idxs[:nWords]
chosenWords = [dictionary[n][:-1] for n in idxs]

def googleSearchDuration(word):
    # returns the durations of a google search query
    query = 'https://www.google.co.uk/search?hl=en&q=%s&meta=&gws_rd=ssl'%(word)
    # imitate a browser so that the reponse includes the duration
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}    
    r = requests.get(query, headers=header)  
    soup = BeautifulSoup(r.content, 'html.parser')
    # parse the response first by finding the div with search result info such as number of results and duration
    resultStats = soup.find(id='resultStats')
    nobr = resultStats.find('nobr')
    # parse the duration from that div
    dur = float(nobr.contents[0][2:-1].split(' ')[0])
    return dur

# write the results into a file
fp = open("durations.txt", "wt")
for k, word in enumerate(chosenWords):
    dur = googleSearchDuration(word)
    fp.write('%f %s\n'%(dur, word))
    print k, dur, word
fp.close()