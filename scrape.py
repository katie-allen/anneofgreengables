# %%
# import packages
from bs4 import BeautifulSoup
import requests
import pandas as pd

#%%
# create urls
list_of_parts = list(range(1,9))

def build_url(part):
    return 'https://greengables-1.tripod.com/script/1part' + str(part) + '.html'

list_of_urls = [build_url(part) for part in list_of_parts]
print(list_of_urls)

#%%
def scrape_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = [item.get_text() for item in soup.find_all('p')][8]
    text = text.split(sep='\n')
    text = [x for x in text if x]
    return(pd.DataFrame({'raw':text}))

#%%
script = []
for url in list_of_urls:
    data = scrape_url(url)
    script.append(data)
    print(url)

# #%%
# # https://stackoverflow.com/questions/50771343/python3-requests-connectionreseterror10054-when-opening-a-picture
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-US,en;q=0.9",
#     "cache-control": "max-age=0",
#     "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "none",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
# }

# #%%
# part1 = scrape_url(list_of_urls[0])
# #%%
# part2 = scrape_url(list_of_urls[1])
# #%%
# part3 = scrape_url(list_of_urls[2])
# #%%
# part4 = scrape_url(list_of_urls[3])
# #%%
# part5 = scrape_url(list_of_urls[4])
# #%%
# part6 = scrape_url(list_of_urls[5])
# #%%
# part7 = scrape_url(list_of_urls[6])
# #%%
# part8 = scrape_url(list_of_urls[7])



#%%
script = pd.concat(script)

#%%
script[['char','line']] = script.raw.str.split(pat = ': ', n = 1, expand = True)

#%%
script.to_csv('anne1script.csv')
# %%
