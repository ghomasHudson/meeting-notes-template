# meeting-notes-template
Write meeting notes in markdown, have them backed up on github, and synced to other things.

## Setup
To setup an rss feed and rolling meeting notes page:
1. Fork your own copy of this repo (Click fork on top right of this page)
2. ssh into mira
3. [Add ssh keys](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) for mira to github
4. Clone your repo into the public html directory: `git clone git@github.com:USERNAME/REPONAME.git public_html/meetingNotes`
5. Clone the same repo onto your own machine

This will give you a php file (http://community.dur.ac.uk/CIS_NAME/meetingNotes/167468974.php) and an rss file (http://community.dur.ac.uk/CIS_NAME/meetingNotes/167468974.rss)

Additionally, to post in discord:
1. Add a new channel to discord and setup the permissions so only you and Noura can see it (you'll have to add a new role)
2. Go to [discordrss.xyz](https://discordrss.xyz)
3. Click control panel (may need to sign in)
4. Add the rss feed (above) to post in the channel you created in 1.
5. Setup a template

## Adding new notes
1. Write your meeting notes in the `notes` directory. Modify the filename to have the correct date/time.
2. Run `./push_notes.sh`
