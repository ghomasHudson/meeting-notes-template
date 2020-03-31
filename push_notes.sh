#!/bin/sh
#
# Script to commit and push meeting notes
#

# TODO: Edit this
USERNAME=abc123


git add notes/*
git commit -m "Update meeting notes"
ssh $USERNAME@mira.dur.ac.uk "./public_html/meetingNotes/update.sh"
