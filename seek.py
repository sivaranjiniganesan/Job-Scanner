#Modules
import requests
from bs4 import BeautifulSoup as soup
import re


def get_job_list(site,page_soup,my_bar,file,url):
    my_data = []
   
    for i in page_soup.find_all('a',{'data-testid':'job-list-item-link-overlay'}):
    
        jd_link = "https://www.seek.com.au"+i.get('href')
        title = i.find('a',{'data-automation':"jobTitle"})
       
        jd_req = requests.get(jd_link)
        jd_soup = soup(jd_req.text, 'html.parser')
        title = jd_soup.find('h1',{'data-automation':"job-detail-title"}).text
        company = jd_soup.find('span',{'data-automation':"advertiser-name"}).text
        location = jd_soup.find('span',{'data-automation':"job-detail-location"}).text
        jd_details = jd_soup.find('div',{"data-automation":"jobAdDetails"})
        li_details = [j.text for j in jd_details.find_all('li')]
        jd_content = jd_details.text
        jd_content = jd_content + (",".join(li_details))
        all_span = jd_soup.find_all('span',{'class':"y735df0 _1iz8dgs4y _94v4w0 _94v4w1 _94v4w22 _4rkdcp4 _94v4w7"})
        for span in all_span:
            s = span.text
            z = re.match("Posted.*ago",s)
            if z:
                time = s
        

        temp = [company, location, title,time, jd_link, jd_content]
        my_data.append(temp)

    return my_data