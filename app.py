import streamlit as st
import pandas 
import pandas
import job_scan
import csv
import remote_io
import get_score
import os
# [theme]
# base="dark"
# primaryColor="#ce1a1a"
# backgroundColor="#0e1e39"
# secondaryBackgroundColor="#0e1237"

st.set_page_config(page_title="Job Scanner", layout="wide")
margins_css = """
    <style>
        .main > div {
            padding: 1rem;
        }
        .stTabs{
         padding-left: 8%;
    padding-right: 12%;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] 
        {
        padding-left: 2%;
    padding-top: 1%;
        }
       div[data-baseweb="tab-list"] 
        {
        display: flex;
    flex-direction: row;
    gap: 2%;
        }
        div[data-testid="stMarkdownContainer"] p {
    font-size: 19px;
        }
        #job-scanner
        {
        padding-left: 4%;
        padding-bottom: 2%;
        margin-top: -1%;
        }
        .stProgress{
           padding-left: 13%;
    padding-right: 21%;
    padding-top: 3%;
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)
st.title('Job Scanner')


tab3, tab1, tab2 = st.tabs(["Your Profile","Job Search", "Match JD"])

tab3.subheader("Upload Your Profile")
resume = tab3.file_uploader("Choose a file...")

if resume:
    CV_text = get_score.cv_to_text(resume)
###############################################################################################################################
tab1.subheader("Select Job Site")
# st.write('<style>div.Widget.row-widget.stCheckbox > div{flex-direction:row;}</style>', unsafe_allow_html=True)
check1,check2,check3,check4= tab1.columns([2,1,2,2])

site1 = check1.checkbox("Remote.co(All developer jobs)")

site2 = check2.checkbox("Upwork")
tab1.subheader("Search Jobs")
col1, col2 , col3= tab1.columns([1,1,1])
title = col1.text_input("Job title", disabled=site1)
location = col2.text_input('Location', disabled=site1)
col3, col4,col5,col6= tab1.columns([1,1,5,2])
search = col3.button("Search")
st.session_state['match'] = False
if site1:
    site = "Remote.co"
    csv_filename = f'jobs_in_{site}.csv'
elif site2:
    site = "Upwork"

if search:
    progress_text = "Please Wait...Getting Results..."
    my_bar = st.progress(0, text=progress_text)
    # tab1.write('Results')
    html = ''
    
    if site == 'Remote.co':
        my_bar.progress(10, text="(10%)Requesting "+site+" ...")
        html = job_scan.request_site("Remote.co",'https://remote.co/remote-jobs/developer/')
    # else:
    #     url = get_url('remote.co', 'data', 'vietnam')
    #     html = job_scan.request_site('linkedin',url)
    
    
    with open(csv_filename, 'w', encoding='utf-8') as f:
        headers = ['Source','Organization', 'Job Title',  'Posted', "Job Link", 'Job Description']
        write = csv.writer(f, dialect='excel')
        write.writerow(headers)

        if html != '':
            result = remote_io.get_job_list(site,html,my_bar,csv_filename)
            for val in result:
                write.writerows([val])
    my_bar.empty()
    csvFile = pandas.read_csv(csv_filename)
    
    
    csvfile_table = tab1.dataframe(csvFile)
match = col4.button("Get Score", help="Match all the job with your CV", key="match_select")
if match:
    if resume:
        if os.path.isfile(csv_filename):
            with st.spinner('Wait for it...Getting results...'):
                csvFile = pandas.read_csv(csv_filename)
                desc_list = csvFile['Job Description']
                data = []
                final_data = []
                for i in range(0,len(csvFile["Job Description"])):
                    data = [csvFile['Organization'][i],csvFile['Job Title'][i],csvFile["Job Link"][i],get_score.get_match(CV_text, csvFile['Job Description'][i])]
                    final_data.append(data)
                    
                df = pandas.DataFrame(final_data, columns=['Company',"Job","Job Link", 'Match %'])
                #del csvfile_table
                # print dataframe.
                tab1.dataframe(df)
        else:
            tab1.error("There is no saved jobs...Search for job")
    else:
        tab1.error('Please upload your profile...')
###################################################################################################################

JD_text = tab2.text_area("Job Description")

score = tab2.button("Match and Get Score")

if score:
    if resume:
        score = get_score.get_match(CV_text,JD_text)
        tab2.write(score)
    else:
        tab2.error('Please upload your profile...')
