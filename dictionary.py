import urllib
import urllib2


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
                  (r'__VIEWSTATE', r"/wEPDwUJNzI2OTY1ODY2ZGT+USYocTWgqVnvgrJNdq"
                                   r"HahgipM9X34+cTfAJeXeq91w=="),
                  (r'__EVENTVALIDATION', r'/wEdAAQ9u5MsVEMABr3X9N71X16h7GsfM2YV'
                                         r'i005lGOvNgWeftVVywmZ4kBIoTw2mza0rfQS'
                                         r'YOQVAPr9tiF9q7nSHjzoi+sT5c19W6Lxf9E7'
                                         r'q+QpuOjCZ6Ppf+nxzkSuoRvROm0='),
                  (r'name', search_term), (r'Submit1', r'Search'))

    encodedFields = urllib.urlencode(formFields)

    request = urllib2.Request(url, encodedFields, headers)
    response= urllib2.urlopen(request)

    for line in response:
        if search_term in line:
            if (not 'script' in line and not 'span' in line and
                    not 'input' in line):
                #print line.strip().split('.<')[0]
                yield line.strip().split('.<')[0]

# for x in TamilCube_Eng2Tm('water'):
#     print x