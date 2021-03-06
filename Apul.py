#Main page for Apul.py http://github.com/GrautDevelopes/Apul.py/
#Very alpha. Expect bugs!
#Only use redirectors that go to blobar and don't go to clickvalidator.net. Examples:
#Usage `python Apul.py http://youtuber.com/ youtuber.com.log`
#http://youtuber.com/
#http://pete.com/
#http://youtibe.com/
import urllib2
import base64
import sys
import re
import os
import time
print("[Apul] Starting...")
print("[Apul] Checking " + sys.argv[1] + " ...")
print("[Apul] Getting timezone...")
utcoffsetinmin = str(
    time.timezone / 60
)  # - 60) #remove ")#" when US DST adds back an hour. #During DST this returns DST while the browser still wants to use Standard? #This is a new feature please report any issues with timezone identification!
print("[Apul] " + utcoffsetinmin + " is current timezone.")
### Config ######################
#Feel free to change these if you know what you're doing.
#utcoffsetinmin = 240 #Overides time detection if uncommented
### Useragent ###################
#ua = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" #Chrome
ua = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko"  #Internet Explorer
#ua = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0" #Edge
#ua = "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fi-fi) AppleWebKit/420+ (KHTML, like Gecko) Safari/419.3" #Mac Safari
#ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.38 (KHTML, like Gecko) Version/10.0 Mobile/14A5297c Safari/602.1" #iPhone Safari
#ua = "Insert own useragent here" #Custom
#################################
req = urllib2.Request(sys.argv[1], headers={'User-Agent': ua})
RedirectorResponse = urllib2.urlopen(req)
RedirectorResponseHTML = RedirectorResponse.read()
RedirectorResponse.close()


def clean_text(rgx, text):
    new_text = text
    new_text = re.sub(rgx, '', new_text)
    return new_text


def save():
    logstream = open(sys.argv[2], 'a+')  #Was 'w'
    for item in Popups:
        logstream.write("%s\n" % item)
    logstream.close()
    lines = open(sys.argv[2], 'r').readlines()
    lines_set = set(lines)
    logstream.close()
    out = open(sys.argv[2], 'w')
    for line in lines_set:
        out.write(line)


def getnewblobarurl():
    req = urllib2.Request(sys.argv[1], headers={'User-Agent': ua})
    RedirectorResponse = urllib2.urlopen(req)
    RedirectorResponseHTML = RedirectorResponse.read()
    RedirectorResponse.close()
    trim0 = clean_text('.*var u = \'', RedirectorResponseHTML)
    trim1 = clean_text('\'\+\(\(r.*', trim0)
    trim2 = clean_text('\'\+\(\(.*', trim1)
    Redirecter3url = trim2 + "2.1." + base64ofdomain + "&r=&z=" + utcoffsetinmin
    #print("[Apul] Resolving " + Redirecter3url + " at " + sys.argv[1] + " ...") #The blobar url, disabled because we don't clear our screen anymore
    return Redirecter3url


if "related content to what you are looking for" in RedirectorResponseHTML:
    print("[Apul] Verifed " + sys.argv[1] + " !")
    base64ofdomain = base64.urlsafe_b64encode(
        clean_text('/', clean_text('.*://', sys.argv[1])))
    Popups = []
    while True:
        req3 = urllib2.Request(getnewblobarurl(), headers={'User-Agent': ua})
        Redirector3Response = urllib2.urlopen(req3)
        PopUpHTML = Redirector3Response.read()
        PopUpURL = Redirector3Response.geturl()
        if 'ww90.' in PopUpURL:
            getnewblobarurl()
        num = re.search(
            r"(((((\(\d{3})|(\s\d{3}))((\)|-)|(\s|\) )|(\)-)?))?)|(\d{3}(-|\s)))?\d{3}(-|\s)\d{4}",
            PopUpHTML
        )  #.group(0) #Much thanks to Eclipse. Created by Eclipse for Graut and the scambaiting community. https://0-eclipse-0.github.io/phone_regex.txt
        Redirector3Response.close()
        if num:
            outline = PopUpURL + " | {}".format(num.group(0))
        else:
            outline = PopUpURL
        Popups = list(set(Popups))
        Popups.sort()
        if outline not in Popups:
            print(outline)
            Popups.append(outline)
            save()
else:
    print("[Apul] The redirector " + sys.argv[1] + " does not use blobar.")
