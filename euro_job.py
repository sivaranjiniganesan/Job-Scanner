#Modules
import requests
from bs4 import BeautifulSoup as soup
import csv
import job_scan

def get_job_list(site, page_soup, my_bar, file, url):

    my_data = []
    for i in page_soup.find_all('div',{"class":"listing-title"}):
        a_link = i.find_all('a')
        for j in a_link:
            if j.get("href") != None:
                link = j.get("href")
                link_req = requests.get(link)
                job_data = soup(link_req.text, 'html.parser')
                job_title = job_data.find('h2').text
                details = {}
                job_details = job_data.find_all('div',{'class':'displayFieldBlock'})
                for detail in job_details:
                    try:
                        if detail.find('h3').text == "Client:":
                            job_company = detail.find('div', {'class':'displayField'}).text
                        elif detail.find('h3').text == "Location:":
                            job_location = detail.find('div', {'class':'displayField'}).text
                        elif detail.find('h3').text == "Posted:":
                            job_posted = detail.find('div', {'class':'displayField'}).text
                        elif detail.find('h3').text == "Job Description:":
                            job_jd = detail.find('div', {'class':'displayField'}).text

                
                    except AttributeError:
                        print("Error ")
                temp = [job_company,job_location, job_title,job_posted,link, job_jd]
                my_data.append(temp)
    #                
            
    return my_data