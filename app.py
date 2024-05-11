import streamlit as st
import pandas 
import pandas
import job_scan
import csv
import remote_io
import get_score
import os
import workinstartups
import euro_job
import relifweb
import seek

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
no_title = False
no_location = False
site = 'none'
Places = ['London', 'Remote', 'Bristol', 'Edinburgh', 'Birmingham', 'Cambridge', 'Epsom', 'Pimpri-Chinchwad', 'Chatham', 'Bude', 'Dublin', 'Glasgow', 'Norwich', 'San Francisco', 'Wallington', 'Tonbridge', 'Leeds', 'Hitchin', 'New Delhi', 'Sheffield', 'Lisbon', 'Worcester', 'Liverpool', 'Skopje', 'Rickmansworth', 'Reigate', 'Chichester', 'Helston', 'Harrow', 'Mataró', 'Milan', 'Hayle', 'Uxbridge', 'Cheltenham', 'Ruislip', 'Thames Ditton', 'Toronto', 'Bromley', 'Knutsford', 'Newcastle upon Tyne', 'Penryn', 'Dubai', 'Farnham', 'New York', 'Manchester', 'Oxford', 'Borehamwood', 'Berkeley', 'Eastleigh', 'Gravesend', 'Royal Leamington Spa', 'Richmond', 'Brighton and Hove', 'Lisburn', 'Bournemouth', 'West Wickham', 'Milton Keynes', 'Sale', 'Dar es Salaam', 'Bourne End', 'Sunbury-on-Thames', 'Riyadh', 'Lincoln', 'Mirrabooka', 'Chelmsford', 'Watford', 'Paphos', 'Oslo', 'Cardiff', 'Southall', 'Oberon', 'Wednesbury', 'Santa Cruz de Tenerife', 'Brierfield', 'Maidstone', 'Copenhagen', 'Singapore', 'Broadway', 'Maidenhead', 'Saffron Walden', 'Warrington', 'Woodford Green', 'Hanover', 'Dartford', 'Hatfield', 'Shefford', 'Hayes', 'High Wycombe', 'Ludwigshafen', 'Frome', 'Hebden Bridge', 'Ooty', 'Zürich', 'Bracknell', 'Royal Oak', 'Rugby', 'Helsinki', 'Berkhamsted', 'Zug', 'Denver', 'Poole', 'Belfast', 'Guildford', 'Shotts', 'Bury', 'Basildon', 'Gateshead', 'Winchester', 'Bangkok', 'Barnsley', 'Croydon', 'Tampere', 'Newtown', 'Crawley', 'Didcot', 'Brighton', 'Berlin', 'Seattle', 'Mexico City', 'Frederikshavn', 'Beaverton', 'York', 'Derby', 'Nottingham', 'Walton-on-Thames', 'Plymouth', 'Johannesburg', 'Windsor', 'Nantwich', 'Park City', 'Tavistock', 'Chipping Norton', 'Coulsdon', 'Banbury', 'Largs', 'Kanpur', 'Colchester', 'Leighton Buzzard', 'Sydney', 'Bath', 'Radlett', 'Tallinn', 'Hull', 'Folkestone', 'Wembley', 'Reading', 'Tadley', 'Stalybridge', 'Pershore', 'Harlow', 'Malvern', 'Southampton', 'Gerakas', 'Saint Asaph', 'Stockton-on-Tees', 'Ibiza', 'Pontefract', 'Tunbridge Wells', 'Santa Cruz', 'Bury Saint Edmunds', 'Amsterdam', 'Saint Julians', 'Stockport', 'Chicago', 'Upminster', 'Fareham', 'Münster', 'Hove', 'Bedford', 'Haymarket', 'Reykjavík', 'Minato City', 'East London', 'Feltham', 'Harpenden', 'Wantage', 'Athens', 'Duluth', 'Sarasota', 'Road Town', 'Gurugram', 'Santa Monica', 'Taunton', 'Wokingham', 'South Croydon', 'Teddington', 'Dunstable', 'Cologne', 'Barcelona', 'Westhill', 'Los Angeles', 'Mitcham', 'Brussels', 'Portsmouth', 'Flagstone', 'Trowbridge', 'Falmouth', 'Lagos', 'Madrid', 'Haarlem', 'Lviv', 'Paris', 'Iver', 'Edmonton', 'Nairobi', 'Auckland', 'Clayton Bay', 'Mississauga', 'Rotterdam', 'Bridgwater', 'Newport', 'Ramsgate', 'Bushey', 'Rome', 'Coventry', 'Macclesfield', 'Kyiv', 'Ternopil', 'Kakamega', 'Prague', 'Málaga', 'Burgess Hill', 'Houston', 'Almaty', 'Kington', 'Barking', 'Michigan City', 'Dhenkanal', 'Eindhoven', 'Faversham', 'Sevenoaks', 'Darlington', 'Johnstone', 'Vancouver', 'Dudley', 'Schuttrange', 'Washington', 'Bradford', 'Anzac', 'Huddersfield', 'Wilmslow', 'Saint-Ouen', 'Boston', 'Bengaluru', 'Great Barrington', 'Warsaw', 'Newton Abbot', 'Paignton', 'San Jose', 'Ringwood', 'Cirencester', 'Godalming', 'Truro', 'Brentford', 'Mumbai', 'Broadstairs', 'Sukabumi', 'Larnaca', 'Barnet', 'Surrey', 'Exeter', 'Vienna', 'Geneva', 'Stockholm', 'Kampala', 'Wrocław', 'Esher', 'Alnwick', 'Lima', 'Aylesbury', 'Stowmarket', 'Hook', 'Harrogate', 'Warwick', 'Grantham', 'Dunbar', 'Durham', 'Melbourne', 'Ledbury', 'Ascot', 'Pontypridd', 'Markham', 'Gloucester', 'Marlow', 'Glen Ellyn', 'Abingdon', 'Brentwood', 'Nashville', 'Northampton', 'Rochdale', 'Stanmore', 'Vineland', 'Wirral', 'Loughton', 'Pudsey', 'Eastbourne', 'Canterbury', 'Las Vegas', 'Felixstowe', 'Rochester', 'Kidlington', 'New Malden', 'Kuala Lumpur', 'Greenhithe', 'Atlanta', 'Eltham', 'Tel Aviv-Yafo', 'Shrewsbury', 'Wallasey', 'Dublin 1', 'St Albans', 'Basingstoke', 'Isle of Man', 'Rainham', 'Burton-on-Trent', 'Jarrow', 'Alfreton', 'Fargo', 'Stuttgart', 'Woodbridge', 'Hassocks', 'Chester', 'Chippenham', 'Chislehurst', 'Islamabad', 'Bogotá', 'Trois-Rivières', 'March', 'Leicester', 'Evesham', 'Lyme Regis', 'Düsseldorf', 'Okehampton', 'Chatswood', 'Camberley', 'Farnborough', 'Newquay', 'Roseville', 'Royston', 'Ferndale', 'Vilnius', 'Ho Chi Minh City', 'Reno', 'Philadelphia', 'Lancaster', 'Utrecht', 'Walnut', 'Kingston upon Thames', 'Grays', 'Romford', 'Twickenham', 'Bicester', 'Yagoona', 'Greenford', 'Honolulu', 'George Town', 'Dover', 'Southend-on-Sea', 'Kings Langley', 'Palma', 'San Diego', 'Ellesmere Port', 'Hyderabad', 'Sheridan', 'Coimbra', 'Linz', 'Lowestoft', 'Remscheid', 'Palo Alto', 'Walferdange', 'Matamoras', 'Irvine', 'Altrincham', 'Lindau', 'Wilmington', 'Košice', 'Cape Town', 'Lockyer', 'Redhill', 'Wimborne', 'Faringdon', 'Hemel Hempstead', 'Musselburgh', 'Hanoi', 'Austin', 'Ware', 'Adelaide', 'Marlborough', 'Ilford', 'Randburg', 'Addison', 'Geleen', 'Goole', 'Billingshurst', 'Tokyo', 'Larkspur', 'Bishops Stortford', 'Chesterfield', 'Pittsburgh', 'Strathaven', 'Lymington', 'Scottsdale', 'Suffield', 'Redwood City', 'Barrie', 'Surry Hills', 'Salford', 'Wellingborough', 'Isleworth', 'Accra', 'Liphook', 'Northbrook', 'Porto Alegre', 'Bucharest', 'Middletown', 'Knebworth', 'Vaduz', 'Hertford', 'Great Yarmouth', 'Salem', 'Braga', 'Petaluma', 'Antwerp', 'Market Harborough', 'Hounslow', 'Tirana', 'Luton', 'Potters Bar', 'Indore', 'Dagenham', 'Cluj-Napoca', 'Cork', 'Staines-upon-Thames', 'Milton', 'Noida', 'Deal', 'Zirakpur', 'Littleton', 'Haywards Heath', 'Delhi', 'Shanghai', 'Augusta', 'Egham', 'Newry', 'Lilesville', 'Menlo Park', 'Wickford', 'Lausanne', 'Hornchurch', 'Congleton', 'Doncaster', 'Nuneaton', 'Devizes', 'Swindon', 'Malta', 'Bromsgrove', 'Louisville', 'Charleston', 'Estoril', 'Redfern', 'Peterborough', 'Martínez', 'Newbury', 'Chorley', 'Amersham', 'Crewe', 'Preston', 'Bolton', 'Moscow', 'Byron Bay', 'Enschede', 'Kingsbridge', 'Telford', 'Ranikhet', 'Vigo', 'Lytham Saint Annes', 'Hallam', 'Kristiansand', 'Welwyn Garden City', 'St. Catharines', 'Gerrards Cross', 'Swansea', 'Salisbury', 'Charthawal', 'Montreal', 'Abtwil SG', 'St. Louis', 'Englewood', 'Poitiers', 'Horsham', 'Jaipur', 'Henley-on-Thames', 'Oldham', 'Liss', 'Christchurch', 'Stevenage', 'Harleston', 'FFW', 'Kitchener', 'Portland', 'Chesham', 'Woking', 'Middlesbrough', 'Kidderminster', 'Dorchester', 'Loughborough', 'Slough', 'Sacramento', 'Englewood Cliffs', 'Jedburgh', 'Exmouth', 'Worthing', 'San Mateo', 'Brampton', 'Alton', 'Aberdeen', 'Pinner', 'St Andrews', 'Redruth', 'Ljubljana', 'Leatherhead', 'St Leonards', 'Lombard', 'Hinckley', 'Dundee', 'Cairo', 'Biggar', 'Barnstaple', 'Peregian Springs', 'Redditch', 'Nijkerk', 'Waterlooville', 'Parramatta', 'Solihull', 'Woolloomooloo', 'İstanbul', 'Bondi Beach', 'Youngstown', 'Minsk', 'Beckenham', 'Riga', 'Jersey City', 'Epping', 'Tartu', 'Sunnyvale', 'Tring', 'Berwick', 'Downham Market', 'Łódź', 'Glenrothes', 'Petaling Jaya', 'Lucknow', 'Witney', 'Edgware', 'Pécs', 'Salt Lake City', 'Paul Roux', 'Letchworth Garden City', 'Chigwell', 'Saint Helens', 'Lemoyne', 'Urmston', 'Bella Vista', 'Phuket', 'Inverness', 'Hastings', 'Bellshill', 'Falls Church', 'Glassboro', 'Gdańsk', 'Wellington', 'The Hague', 'Isle of Mull', 'Dewsbury', 'Porsgrunn', 'Joliet', 'Newark', 'Frankfurt', 'Hokksund', 'Hamburg', 'Carnforth', 'Waterloo', 'Taipei', 'Antwerpen', 'Secret Harbour', 'Bushmills', 'Orange', 'Lutterworth', 'Thame', 'Alderley Edge', 'Delaware City', 'Tetbury', 'Canvey Island', 'West Vancouver', 'Much Wenlock', 'Southwell', 'Tipton', 'Corsham', 'Penarth', 'Sidcup', 'Oxted', 'Chinnor', 'Droitwich', 'Ormskirk', 'Stamford', 'Nuremberg', 'Lawrence Township', 'Dorking', 'Prahran', 'Hampton', 'Romsey', 'Yateley', 'Hoxton Park', 'Haslet', 'Munich', 'Pontypool', 'Orpington', 'Shoreham-by-Sea', 'Caerphilly', 'Stroud', 'Clifton', 'Baltimore', 'Newport Pagnell', 'Rossendale', 'Ballston Lake', 'Aberystwyth', 'Barbil', 'Penzance', 'Motherwell', 'Antrim', 'Beaconsfield', 'Lymm', 'Stratford-upon-Avon', 'Malton', 'Falkirk', 'Welwyn', 'Stafford', 'Princes Risborough', 'Kensington', 'Oakville', 'Hindmarsh', 'Blacktown', 'Carouge', 'Uttoxeter', 'Burlingame', 'Glen Allen', 'Faridabad', 'Bruxelles', 'Fleet', 'Cullompton', 'Belconnen', 'Augsburg', 'Bordon', 'Alpharetta', 'Lewes', 'Penicuik', 'Derrimut', 'Tampa', 'Tewkesbury', 'Theydon Bois', 'Port Talbot', 'Forrestfield', 'Providencia', 'Farrukhabad', 'Gold Coast', 'Addlestone', 'Boulder', 'Chennai', 'Morden', 'Saint Paul', 'Carlisle', 'Bexley', 'Sutton', 'Holwerd', 'Bradford-on-Avon', 'Sahibzada Ajit Singh Nagar', 'Valencia', 'Spearwood', 'Osnabrück', 'Worcester Park', 'South Petherton', 'Kumanovo', 'Shepparton', 'Camberwell', 'Patna', 'Lucena', 'Newport Beach', 'West Palm Beach', 'Mount Airy', 'Stourbridge', 'Godstone', 'Woodbridge Township', 'Culver City', 'Halstead', 'Dublin 14', 'Metropolitan Borough of Stockport', 'Enfield', 'Caterham', 'Cromer', 'Hasbrouck Heights', 'Sheringham', 'Northwood', 'Nelson', 'Pyrmont', 'Wetherby', 'Zwijndrecht', 'Wexford', 'Bern', 'Somerville', 'Brunswick West', 'Glendale', 'Rockville', 'Fort Myers', 'Dublin 11', 'Limerick', 'Killarney', 'Neath', 'Smethwick', 'Komotini', 'Kittery', 'Stoke-on-Trent', 'Bourne', 'Airdrie', 'Reutlingen', 'Yeovil', 'Buckingham', 'Drury', 'Mayfield', 'Aylesford', 'Glebe', 'Stockport District', 'Lusaka', 'Towcester', 'Maastricht', 'Blackpool', 'Big Pine Key', 'Warlingham', 'Franklin Township', 'Lower Sackville', 'San Bernardino', 'Haslemere', 'Port Adelaide', 'Providence', 'Old Lyme', 'South Nowra', 'Roslin', 'Greater Manchester', 'East Grinstead', 'Elizabeth', 'Southbank', 'Perivale', 'Darmstadt', 'Deepdene', 'Spring Hill', 'Sandbach', 'Tadcaster', 'Northwich', 'Cincinnati', 'Wolverhampton', 'Meningie', 'Porto', 'Gillingham', 'Surbiton', 'Mauchline', 'Loanhead', 'Lanark', 'Montville', 'Haverfordwest', 'Bartlett', 'Londo', 'Waterville', 'Burneside', 'Kents Hill', 'Southwick', 'Copperopolis', 'London, Old Street, Shoreditch', 'Bremen', 'Madison', 'San Antonio'
          , 'Thurleigh', 'Rancho Santa Margarita', 'Nice', 'Saint Leonards', 'Dunfermline', 'Halifax', 'Redbourn', 'Staverton', 'Belmont', 'Groes-faen', 'Afton', 'Stoke Gifford', 'Mainz', 'Iowa City', 'Marousi', 'Noxon', 'Woolley Green', 'Norwood', 'Drayton', 'Chilworth', 'Easton on the Hill', 'High Point', 'Portishead', 'Potsdam', 'Parsippany-Troy Hills', 'Lake George', 'Mount Hawthorn', 'Bridgeton', 'Lyons', 'Kennett', 'Williamsburg', 'Purley', 'Monaghan', 'Victoria', 'Woodford', 'Kennington', 'Knowl Hill', 'Cowes', 'Emersons Green', 'Lichfield', 'Poynton', 'Langford', 'Whiteley', 'Unterschleißheim', 'Thatcham', 'West Fleetham', 'Sandside', 'Holmes Chapel', 'Plainview', 'Fulbourn', 'Milton Abbas', 'Longford', 'Billericay', 'Black Notley', 'Timperley', 'Brackley', 'Bideford', 'East Bethel', 'Saint-Maur-des-Fossés', 'Chessington', 'Bielefeld', 'Potts Point', 'Heath Hayes', 'Corby', 'Greatworth', 'Costa Mesa', 'Bexleyheath', 'Bordesley Green', 'Hopewell', 'Westfield', 'Ravensburg', 'Falmer', 'Adderbury', 'Bow', 'Sudbury', 'Yarnton', 'Wooburn Green', 'Lund', 'Greater Napanee', 'Schönefeld', 'Cooksbridge', 'Saint Austell', 'Kilwinning', 'Bramham', 'Stanstead Abbotts', 'Hellerup', 'Hoo', 'Lena', 'Clinton', 'Yurihonjo', 'Great Gaddesden', 'Knowlhill', 'Lawrence', 'Auburn', 'Royal Tunbridge Wells', 'Smithfield', 'Nantucket', 'Castle Donington', 'Eynsham', 'Rosyth', 'Horsforth', 'Keltybridge', 'Loudwater', 'Princeton', 'Seoul', 'Promised Land', 'Ottweiler', 'Elstree', 'Bexhill', 'Wymeswold', 'Weybridge', 'West Bromwich', 'Pury End', 'Waltham Abbey', 'Blandford Forum', 'Sunningdale', 'South Shields', 'Offham', 'Msida', 'Wareside', 'Brewer', 'Ashford', 'Stoke Prior', 'Bewdley', 'Commerce City', 'Carfin', 'Merstham', 'Chita', 'Rock Port', 'Tea', 'Manhasset', 'Hereford', 'Barquisimeto', 'Mountain View', 'Whitstable', 'Livingston', 'Denham', 'Saint Johns', 'Linthwaite', 'Westminster', 'Dunchurch', 'Broadbridge Heath', 'Brooklet', 'Reisterstown', 'Shibuya', 'Rewari', 'Clydebank', 'Sauternes', 'Menard', 'Elie', 'Bilston', 'Thornaby', 'Ghent', 'Raigmore', 'Battersea', 'Santa Barbara', 'Arlesey', 'Orsett', 'East Malling', 'Stony Stratford', 'Stretford', 'Temple', 'Concord', 'Chandler', 'Edgewood', 'Ash Vale', 'Church Stowe', 'Theale', 'Budapest', 'Ipswich', 'Kendal', 'Wrexham', 'Cheshunt', 'Plumpton Green', 'Rustington', 'Greenford Park', 'Offord DArcy', 'Port Tennant', 'Lansing', 'Edenbridge', 'West Grinstead', 'Knaphill', 'Saint Albans', 'Dumbarton', 'Lake Zurich', 'Old Stratford', 'Jankowice Rybnickie', 'Littring', 'Honeybourne', 'Winkfield Row', 'Kilgore', 'Halfway', 'Walsall', 'East Kilbride', 'Camden', 'Colwyn Bay', 'Hampton Wick', 'Springdale', 'Didmarton', 'Marseille', 'Lambourn', 'Hayward', 'London', 'Halifax', 'Remote', 'SE1 Waterloo', 'London, E2 8JF', 'UK', 'Liverpool', 'Edinburgh', 'EC1V 9NQ London', 'Belfast', 'Birmingham', 'Bristol', 'Cardiff', 'SW1 Victoria', 'SW19 Wimbledon', 'Cambridge', 'Uttoxeter', 'NW1 9PX London', 'WC2R 0AP London', 'Leeds', 'Reading', 'Maidstone', 'Hybrid - London', 'Swindon/Hybrid', 'United Kingdopm', 'SW19 3ES Wimbledon', 'Darmstadt', 'Brighton', 'WC1A 2SL London', 'United States', 'London/Hybrid', 'Sheffield', 'Nottingham', 'Inverness', 'Peterborough', 'Hybrid', 'Aylesbury', 'Remote / Hybrid', 'London, SW18 1UY', 'London, WC1V 6NY', 'Manchester', 'Warrington', 'London, E1 5LN', 'London, UK', 'Office + Remote', 'London, EC1Y8AF', 'UK Based', 'Penryn', 'Hanover', 'N1 7GU London', 'SE1 7ND London', 'Guildford, GU27HJ', 'Glasgow', 'E1 5JL London', 'Frome', 'Epsom']
tab3, tab1, tab2 = st.tabs(["Your Profile","Job Search", "Match JD"])

tab3.subheader("Upload Your Profile")
resume = tab3.file_uploader("Choose a file...")

if resume:
    CV_text = get_score.cv_to_text(resume)
###############################################################################################################################
tab1.subheader("Select Job Site")
check1,check2,check3,check4= tab1.columns([2,2,2,2])
job_site = ["Remote.co(developer jobs)","Euro Jobs.com","Work In Startups","Jobs@ReliefWeb","Seek - Australia"]
site = check1.selectbox('Select Site',job_site)


if site == "Remote.co(developer jobs)":
    site = "Remote.co"
    no_title = True
    no_location = True
elif site == "Euro Jobs.com":
    site = "eurojobs"
    no_title = False    
    no_location = False
elif site == "Work In Startups":
    site = "workinstart"
elif site == "Jobs@ReliefWeb":
    site = 'relifweb'
    no_title = False
    no_location = True
elif site == "Seek - Australia":
    site = "seek"
    no_title = False    
    no_location = True
# elif site6:
#     site = "jobsdb"
# elif site7:
#     site = 'goinglobal'
#     no_title = False
#     no_location = True
csv_filename = f'jobs_in_{site}.csv'
tab1.subheader("Search Jobs")
col1, col2 , col3= tab1.columns([1,1,1])
title = col1.text_input("Job title", disabled=no_title)
if site == "Work In Startups":
    location = col2.selectbox('Location',Places)
else:
    location = col2.text_input('Location', disabled=no_location)

col3,col4,col5,col6= tab1.columns([1,1,5,2])
search = col3.button("Search")
st.session_state['match'] = False



if search:
    
    progress_text = "Please Wait...Getting Results..."
    my_bar = st.progress(0, text=progress_text)
    # tab1.write('Results')
    html = ''
    
    if site == 'Remote.co':
        my_bar.progress(10, text="(10%)Requesting "+site+" ...")
        html = job_scan.request_site("Remote.co",'https://remote.co/remote-jobs/developer/')
    elif site == 'eurojobs':
        url = "https://eurojobs.com/search-results-jobs/?action=search&listing_type%5Bequal%5D=Job&keywords%5Ball_words%5D="+title+"&Location%5Blocation%5D%5Bvalue%5D="+location
        html = job_scan.request_site(site,url)
    elif site == 'workinstart':
        url = "https://workinstartups.com/jobs-search/?keywords="+title+"&location="+location
        html = job_scan.request_site(site,url)
    elif site == "relifweb":
        url = "https://reliefweb.int/jobs?search="+title
        html = job_scan.request_site(site, url)
    elif site == "seek":
        url = "https://www.seek.com.au/"+title+"-jobs"
        html = job_scan.request_site(site, url)
    
    
    with open(csv_filename, 'w', encoding='utf-8') as f:
        headers = ['Organization', 'Location','Job Title',  'Posted', "Job Link", 'Job Description']
        write = csv.writer(f, dialect='excel')
        write.writerow(headers)

        if html != '':
            if site == "Remote.co":
                result = remote_io.get_job_list(site,html,my_bar,csv_filename)
            elif site == "workinstart":
                result = workinstartups.get_job_list(site,html,my_bar,csv_filename,url)
            elif site == "eurojobs":
                result = euro_job.get_job_list(site,html,my_bar,csv_filename,url)
            elif site == "relifweb":
                result = relifweb.get_job_list(site,html,my_bar,csv_filename,url)
            elif site == "seek":
                result = seek.get_job_list(site,html,my_bar,csv_filename,url)
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
                    data = [get_score.get_match(CV_text, csvFile['Job Description'][i]), csvFile['Organization'][i],csvFile['Location'][i],csvFile['Job Title'][i],csvFile["Job Link"][i]]
                    final_data.append(data)
                    
                df = pandas.DataFrame(final_data, columns=['Match %','Company','Location',"Job","Job Link"])
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
