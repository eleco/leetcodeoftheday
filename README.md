# Leetcode of the day bot

A python app to email the leecode of the day problem. 

## Usage

1. Set the env variables below to point to the recipient+sender email and the mailgun api+endpoint respectively:
```
LEETCODE_RECIPIENT
LEETCODE_SENDER
LEETCODE_MAILJET_KEY
LEETCODE_MAILJET_SECRET
```

2. either run main.py manually or deploy on a hosting service e.g heroku and schedule to run every day.
