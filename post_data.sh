#!/bin/bash

# USAGE
# ./post_data.sh <filename.json>
# where filename.json is a json file structured as follows:
#{
#    "group_id" : "4",  # this is the group_id
#    "group_hash" : "1154rt65", # this is the group hash - irrelevant for now
#    "result" : "76.58" # this is the submission result
#}

curl -X POST -H "Content-Type: application/json" -d @$1 'http://localhost:5000/group/create/'
