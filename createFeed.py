'''Tool to convert markdown documents to RSS feed'''
import requests
import os
import markdown2
from datetime import datetime
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
                'title': "Group Meeting - "+date_formatted,
                'link': "http://community.dur.ac.uk/g.t.hudson/groupMeetingNotes/167468974.php",
                'pubDate': date,
                'description':'<![CDATA['+meetingContents+"]]>"
        })

#Convert meetings to RSS feed
rssFeed = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">

<channel>
<title>Group meeting notes</title>
<description>Minutes from our weekly group meetings</description>
"""

for meeting in meetings:
    rssFeed += "<item>\n"
    for key in meeting.keys():
        rssFeed += "\t<"+key+">"+meeting[key]+"</"+key+">\n"
    rssFeed += "</item>\n"
rssFeed += "</channel>\n</rss>"

#Save to disk
with open("167468974.rss",'w') as f:
    f.write(rssFeed)
