# email the leetcode of the day, every day
import aiohttp
import mailjet_rest
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import requests
import traceback
import os

email_sender = os.environ["LEETCODE_SENDER"]
email_recipient = os.environ["LEETCODE_RECIPIENT"]
api_key = os.environ["LEETCODE_MAILJET_KEY"]
api_secret = os.environ["LEETCODE_MAILJET_SECRET"]


def get_leetcode_of_the_day():
    transport = AIOHTTPTransport(url="https://leetcode.com/graphql/")
    client = Client(transport=transport, fetch_schema_from_transport=False)
    query = gql(
        """
        query questionOfToday { 
         activeDailyCodingChallengeQuestion {    
            date    
            userStatus    
            link    
            question {      
                acRate      
                difficulty      
                title   
            }  
        }
    }    
    """
    )

    return client.execute(query)


def send_simple_message(msg):
    date = msg["activeDailyCodingChallengeQuestion"]["date"]
    link = msg["activeDailyCodingChallengeQuestion"]["link"]
    title = msg["activeDailyCodingChallengeQuestion"]["question"]["title"]

    try:
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": email_sender,
                        "Name": "Leetcode of the day"
                    },
                    "To": [
                        {
                            "Email": email_recipient
                        }
                    ],
                    "Subject": "leetcode of the day " + date + " : " + title,
                    "TextPart": "Leetcode of the day",
                    "HTMLPart": "<html><a href=https://leetcode.com" + link + ">" + title + "</html>",
                    "CustomID": "AppLeetcode"
                }
            ]
        }
        mailjet = mailjet_rest.Client(auth=(api_key, api_secret), version='v3.1')
        return mailjet.send.create(data=data)
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    print(send_simple_message(get_leetcode_of_the_day()))
