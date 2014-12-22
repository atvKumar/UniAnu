from urllib import urlencode
from urllib2 import Request, urlopen

_url = "http://dictionary.tamilcube.com/index.aspx"
_data = ''
_viewstate = ''
_eventvalidation = ''


def getTamilCube_Data(refresh=False):
    global _data
    if _data == '' or refresh:
        _data = getWebPage(_url)
        setTamilCube_id()


def getHeaders():
    return {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; '
                       'rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,'
                   '*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
    }


def getWebPage(url):
    request = Request(url, headers=getHeaders())
    response = urlopen(request)
    if response.getcode() == 200:
        return response.read()


def setTamilCube_id():
    global _viewstate, _eventvalidation
    if _viewstate == '' and _eventvalidation == '':
        viewstate_list = list()
        eventvalidation_list = list()
        for line in _data.split('\n'):
            if "id=\"__VIEWSTATE\" value=\"/" in line:
                viewstate_list.append(line)
            if "id=\"__EVENTVALIDATION\" value=\"/" in line:
                eventvalidation_list.append(line)
        _viewstate = viewstate_list[0].split('"')[7]
        _eventvalidation = eventvalidation_list[0].split('"')[7]


def getTamilCube_FormData(search_term):
    formFields = ((r'__EVENTTARGET', r''), (r'__EVENTARGUMENT', r''),
                  (r'__VIEWSTATE', _viewstate),
                  (r'__EVENTVALIDATION', _eventvalidation),
                  (r'name', search_term), (r'Submit1', r'Search'))
    return urlencode(formFields)


def TamilCube_Eng2Tm(search_term):
    encodedFields = getTamilCube_FormData(search_term)
    request = Request(_url, encodedFields, getHeaders())
    response= urlopen(request)

    for line in response:
        if search_term in line:
            if (not 'script' in line and not 'span' in line and
                    not 'input' in line):
                #print line.strip().split('.<')[0]
                yield line.strip().split('.<')[0]


getTamilCube_Data()