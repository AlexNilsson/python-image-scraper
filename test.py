import time, math
from datetime import date

import csv

from urllib.parse import quote

from gscraper.web import getURLContents
from gscraper.scraper import get_all_imgage_urls_from_html, download_images, get_match_data
from gscraper.utility import create_sub_directory

def scrapeData():
  t0 = time.time()

  all_matches = []

  print("\n Query Rugby Scores -->")
  print("Scraping...")

  N_PAGES = 376
  for i in range(N_PAGES):

    ''' SCRAPE URLS '''
    # set for further filtering; color, size, etc
    url = 'http://stats.espnscrum.com/statsguru/rugby/stats/index.html'
    url += '?class=1;page='
    url += str(i+1)
    url += ';spanmin1=01+Jan+1900;spanval1=span;template=results;type=team;view=results'

    raw_html = getURLContents(url)
    time.sleep(0.1)

    ''' DOWNLOAD URLS '''
    print("Downloading..." + " page " + str(i+1) + "/" + str(N_PAGES))
  
    matches = get_match_data(raw_html)
    all_matches += matches

    t1 = time.time()
    total_time = t1 - t0

    print("Total time taken: " + str(math.floor(total_time)) + " Seconds")

  print("\n Everything downloaded!")
  print("Total Matches: " + str(len(all_matches)))
  print("\n writing file...")

  # make a new directory for this search_query
  today = str(date.today())
  create_sub_directory(today, "downloads")

  with open("./downloads/" + today + "/data.csv", 'w', newline='\n', encoding='utf-8') as output_file:
    wr = csv.writer(output_file, dialect='excel')
    wr.writerows(all_matches)
      
  print("\n Done!")


def test_write ():
  today = str(date.today())
  with open("./downloads/" + today + "/data.csv",'w') as output_file:
    wr = csv.writer(output_file, dialect='excel')

    wr.writerow(['a', 'b', 'c'])
    wr.writerow(['a', 'b', 'c'])
    wr.writerow(['a', 'b', 'c'])

scrapeData()
#test_write()