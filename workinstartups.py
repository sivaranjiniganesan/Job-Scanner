import requests
from bs4 import BeautifulSoup as soup
import csv
import job_scan


def get_job_list(site,page_soup,my_bar,file,url):
    my_data = []
    
    pagination = page_soup.find_all('li',{'class','d-inline-block'})
    count = 1
    for i in pagination:
        if ','.join(i['class']) == 'd-inline-block':
            count = count + 1
            

    for i in range(1,count+1):
        page_url = url + "&page=" + str(count)
        new_soup = job_scan.request_site(site, page_url)
    
        job_list = new_soup.find('div', {'class': 'job-listings'})
        for i in job_list.find_all('a'):

            company = i.find('span',{'class':'company-text'}).text
            time = i.find('span', {'class':'d-inline-block'}).text
            
            
            job_link = i['href']
            print(job_link)
            jd_req = requests.get(job_link)
            jd_content = soup(jd_req.text,'html.parser')
            job_title = jd_content.find('h1').text.split("at")[0].strip()
            place = jd_content.find('i', {'class':'icon-location'}).text
            try:
                job_description = jd_content.find('div',{'id':'job-description'}).text
            except AttributeError:
                print("ERROR")

            temp = [company,place, job_title, time, job_link, job_description]
            my_data.append(temp)

    return my_data