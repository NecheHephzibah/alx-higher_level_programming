#!/bin/bash
#script that makes a request to 0.0.0.0:5000/catch_me that causes the server
curl -sL -X PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
