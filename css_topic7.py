import urllib.request
from bs4 import BeautifulSoup

conf_url_list =[]
#open the page, read it and extract the content after Artificial intelligence
#which is between ul and the next appereance of h2 which is the beginning for the next subarea
#The extracted content convert it to beautifulsoup in order to get the href value
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_computer_science_conferences')
html = response.read().decode('utf-8')
first_topic = html[html.index('id="Artificial_intelligence"'):]
conferences_list = first_topic[first_topic.find('<ul>'): first_topic.find('<h2>')]
soup = BeautifulSoup(conferences_list, 'html.parser')
conferences = [tag['href'] for tag in soup.select('li a[href]')]

#loop throu all the wiki pages of the conferences, read them, and convert the content in beautiful soup
#find the external link area and get the first link with
#assumption: the first link in the external link part is the official website of the conference
for conference in conferences:
    conf_wikipage = urllib.request.urlopen('https://en.wikipedia.org' + conference)
    conf_html = conf_wikipage.read().decode('utf-8')
    soup2 = BeautifulSoup(conf_html, 'html.parser')

    external_links = soup2.find("span", id="External_links")
    if(hasattr(external_links, 'find_parent("h2")')):
        conf_url_list.append(external_links.find_parent("h2").find_next_sibling("ul").find('a').get('href'))    
    
print(conf_url_list)

#API for getting the automated attractivness score
# r = requests.post(
#   "https://api.haystack.ai/api/image/analyze?output=json&apikey=95b75bcbad786644f46522bcedcb395c",
#   data=open('testImage.JPG', 'rb'))
# print(r.text);