import unicodedata
import job_scan

def get_job_list(site,html,my_bar,file):
    data = {}
    my_data = []
    tags = []
    orgs = []
    Source = site
    titles =[title.text.strip() for title in html.find_all('span', {'class': 'font-weight-bold larger'})]
    time_posted =[time.text.strip() for time in html.find_all('span', {'class': 'float-right d-none d-md-inline text-secondary'})]
    my_bar.progress(25, text="(25%)Getting Data...")
    
    for content in html.find_all('div', {'class': 'card-body px-3 py-0 pl-md-0'})[0:]:
        temp = []
        for val in content.find_all('p', {'class': 'm-0 text-secondary'}):
            temp.append(val.text)
            for i in temp:
                tag = unicodedata.normalize("NFKD", i).replace('\n','').replace(" ","").split("|")
                org = tag[0]
                tag.pop(0)

            tags.append(tag)
            orgs.append(org)
    my_bar.progress(50, text="(50%)Getting Data...")
    desc_link =[link['href'] for link in html.find_all(attrs={"class" : "card m-0 border-left-0 border-right-0 border-top-0 border-bottom"})]
   
    
    
    for i in range(0,len(orgs) - 1):
        data = get_jd(site, job_scan.site_url[site]+desc_link[i])
#         print(data)
        temp = [site, orgs[i], titles[i],time_posted[i],job_scan.site_url[site]+desc_link[i], data['desc']]
        my_data.append(temp)
        if i >= len(orgs) - (len(orgs)/3):
            my_bar.progress(90, text="(90%)Saving Jobs in "+file+" file...")
        if i >= len(orgs)/2:
           my_bar.progress(75, text="(75%)Getting Data...") 
    return my_data

def get_jd(site, endpoint):
    data = {}
    data['desc'] = []
    # data['Location'] = []
    # data['Salary'] = []
    # data['Benefits'] = []
    tag_arr = ['p','li']

    html = job_scan.request_site(site,endpoint)

    # title = [title.text for title in html.find_all('div', {'class': 'col-10 col-sm-11 pl-1'})]
    # for i in title:
    #     i_split = i.split(":")
    #     if i_split[0] in ['Location','Salary','Benefits']:
    #         data[i_split[0]].append(i_split[1].strip())

    for jd in html.find_all('div', {'class': 'job_description'}):
        for tag in tag_arr:
            if jd.find(tag):
                for p in jd.select(tag):
                    text_p = p.get_text(strip=True, separator='\n')
                    if len(text_p.split(" ")) > 30:
                        data['desc'].append(text_p)
    return data