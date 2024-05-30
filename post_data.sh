#!/bin/bash

#curl --location 'http://localhost:5000/group/create/' \
#--header 'Content-Type: application/json' \
#--data $(cat $1)


#{
#    "group_id" : "4",
#    "group_hash" : "1154rt65",
#    "result" : "76.58"
#}


curl -X POST -H "Content-Type: application/json" -d @$1 'http://localhost:5000/group/create/'