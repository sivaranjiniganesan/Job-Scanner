
#Modules
import requests
from bs4 import BeautifulSoup as soup
import csv

def get_job_list(site, page_soup, my_bar, file, url):
    all_title = page_soup.find_all('h3', {'class', 'rw-river-article__title'})
    my_data = []
    for i in all_title:
        title = i.text
        job_link = i.find('a').get('href')
        jd_content = requests.get(job_link)
        jd_soup = soup(jd_content.text, 'html.parser')
        dd_content = []
        for j in jd_soup.find_all('dd',{'class','rw-entity-meta__tag-value'}):
            dd_content.append(j.text.replace('\n','').strip())
            
        company = dd_content[0]
        time = dd_content[1]
        place = dd_content[3]+", "+ dd_content[4]
        
        job_jd = jd_soup.find('div',{'class','rw-article__content'}).text
        
        temp = [company,place, title ,time ,job_link, job_jd]
        my_data.append(temp)
                   
            
    return my_data