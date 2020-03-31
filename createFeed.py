'''Tool to convert markdown documents to RSS feed'''
import requests
import os
import markdown2
from datetime import datetime
import glob

########################################################

FULL_USERNAME = "g.t.hudson" #TODO: Edit this!!!

############################################################
# Find .php file
for php_file in glob.glob("*.php"):
    if not php_file=="rss2html.php":
        rss_file = os.path.splitext(php_file)[0]+".rss"


#Go through notes dir and load meetings
meetings = []
for root, _, files in os.walk("notes"):

    #Sort to get most recent first in feed
    filesSorted = sorted(list(files))
    filesSorted.reverse()
    for file_ in filesSorted:
        #Find the date and title from filename
        date = file_[:19].replace("\\","")

        #Convert markdown to html
        meetingContents = open(os.path.join(root,file_),'r').read()
        meetingContents = markdown2.markdown(meetingContents)
        meetingContents = meetingContents.replace("\n","")

        #Get human-readable date
        date_formatted = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        date_formatted = date_formatted.strftime("%b %-d, %Y")

        #Construct meeting object
        meetings.append({
                'title': "Meeting - "+date_formatted,
                'link': "http://community.dur.ac.uk/"+FULL_USERNAME+"/meetingNotes/"+php_file,
                'pubDate': date,
                'description':'<![CDATA['+meetingContents+"]]>"
        })

#Convert meetings to RSS feed
rssFeed = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">

<channel>
<title>Meeting notes</title>
<description>Minutes from weekly meetings</description>
"""

for meeting in meetings:
    rssFeed += "<item>\n"
    for key in meeting.keys():
        rssFeed += "\t<"+key+">"+meeting[key]+"</"+key+">\n"
    rssFeed += "</item>\n"
rssFeed += "</channel>\n</rss>"

#Save to disk
with open(rss_file,'w') as f:
    f.write(rssFeed)
