from urllib import urlencode
from urllib2 import Request, urlopen

def getVIEWSTATE(search_term="id=\"__VIEWSTATE\" value=\"/",
                 url="http://dictionary.tamilcube.com/index.aspx"):
    response = urlopen(url)
    data = [x for x in response if search_term in x]
    return data[0].split('"')[7]

def getEVENTVALIDATION(search_term="id=\"__EVENTVALIDATION\" value=\"/",
                       url="http://dictionary.tamilcube.com/index.aspx"):
    response = urlopen(url)
    data = [x for x in response if search_term in x]
    return data[0].split('"')[7]

def TamilCube_Eng2Tm(search_term,
                     url="http://dictionary.tamilcube.com/index.aspx"):
    # Dummy header to bypass blocks and bots
    headers = {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; '
                       'rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,'
                   '*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'}

    #Tamil Cube Form Fields
    formFields = ((r'__EVENTTARGET', r''), (r'__EVENTARGUMENT', r''),
                  (r'__VIEWSTATE', getVIEWSTATE()),
                  (r'__EVENTVALIDATION', getEVENTVALIDATION()),
                  (r'name', search_term), (r'Submit1', r'Search'))

    encodedFields = urlencode(formFields)

    request = Request(url, encodedFields, headers)
    response= urlopen(request)

    for line in response:
        if search_term in line:
            if (not 'script' in line and not 'span' in line and
                    not 'input' in line):
                #print line.strip().split('.<')[0]
                yield line.strip().split('.<')[0]

# for x in TamilCube_Eng2Tm('water'):
#     print x