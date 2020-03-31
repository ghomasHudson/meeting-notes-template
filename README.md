# meeting-notes-template
Write meeting notes in markdown, have them backed up on github, and synced to other things.

## Setup
The setup for this is a little long, but once it's done, adding notes is simple.
### mira
To setup an rss feed and rolling meeting notes page:
1. Fork your own copy of this repo (Click fork on top right of this page)
2. ssh into mira: `ssh CIS_USERNAME@mira.dur.ac.uk`
3. [Add ssh keys](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) for mira to github
4. Install dependancies on mira: `pip install --user requests markdown2`
5. Clone your repo into the public html directory: `git clone git@github.com:USERNAME/REPONAME.git public_html/meetingNotes`
6. Clone the same repo onto your own machine
7. On your machine, change your USERNAME in `push_notes.sh`

You might want to rename `12345.php` to be something less guessable. You will end up with a php page: http://community.dur.ac.uk/CIS_NAME/meetingNotes/12345.php and after running `./update.sh`, you'll also get an rss feed: http://community.dur.ac.uk/CIS_NAME/meetingNotes/12345.rss

In order to be able to see some files, you might need to set the permissions: `chmod 755 ~/public_html/meetingNotes` and `chmod 644 ~/public_html/meetingNotes/index.html ~/public_html/meetingNotes/12345.php ~/public_html/meetingNotes/12345.rss`

### discord
Additionally, to post in discord:
1. Add a new channel to discord and setup the permissions so only you, the bot, and Noura can see it (you'll have to add a new role)
2. In the channel you just created, type `~rssadd https://community.dur.ac.uk/CIS_NAME/12345.rss` or whatever your feed url is
3. Change the format of the notes with `~rssmessage`, e.g.
```
**{title}**
*{date}*
------------------------------------------

{description}

{link}
```
Whenever you update the meeting notes, they will be posted into the channel you setup.

## Adding new notes
1. Write your meeting notes in the `notes` directory. Modify the filename to have the correct date/time.
2. Run `./push_notes.sh`
