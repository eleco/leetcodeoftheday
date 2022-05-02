# Leetcode of the day bot

A python app to email the [leecode](https://leetcode.com ) problem of the day. 

## Usage

1. Set the env variables below to point to the recipient+sender of the email and the mailjet properties respectively:
```
LEETCODE_RECIPIENT
LEETCODE_SENDER
LEETCODE_MAILJET_KEY
LEETCODE_MAILJET_SECRET
```

2. Either run main.py manually or deploy on a hosting service e.g heroku and schedule to run every day.

3. Check the recipient mailbox for a link to the leetcode problem of the day.
