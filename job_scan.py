import requests
from bs4 import BeautifulSoup as soup
from requests.auth import HTTPBasicAuth
import colorama
auth = ""
site_url = {}
site_url['Remote.co'] = "https://remote.co"
def request_site(site,url):
    try:
        if site == "linkedin":
            req = requests.get(url, auth = auth)
        else:
            req = requests.get(url)
        
        req.raise_for_status()

        # create Soup
        page_soup = soup(req.text, 'html.parser')
        return page_soup
    except requests.HTTPError as err:
        print(colorama.Fore.RED,
                f'[!!] Something went wrong! {err}', colorama.Style.RESET_ALL)