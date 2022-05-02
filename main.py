# email the leetcode of the day, every day
import aiohttp
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import requests
import traceback
import os

env_email = os.environ['LEETCODE_EMAIL']
env_mailgun_api = os.environ['LEETCODE_MAILGUN_API']
env_mailgun_endpoint = os.environ['LEETCODE_MAILGUN_ENDPOINT']


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
        return requests.post(
            env_mailgun_endpoint,
            auth=("api", env_mailgun_api),
            data={"from": "leetcode of the day bot <mailgun@YOUR_DOMAIN_NAME>",
                  "to": [env_email],
                  "subject": "leetcode of the day " + date + " : " + title,
                  "html": "<html><a href=https://leetcode.com" + link + ">" + title + "</html>"
                  })
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    print(send_simple_message(get_leetcode_of_the_day()))
