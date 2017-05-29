#!/usr/bin/env python3

#import JSON module, specified by RFC 7159. For more information https://docs.python.org/3/library/json.html
import json
#import requests modile, allows send organic HTTP/1.1 requests. For more information http://docs.python-requests.org/en/master/
import requests
#import feedparser module, serving RSS feeds. For more information: https://pythonhosted.org/feedparser/
import feedparser
import time
#Importing finction lohing_cur_time from module app_logging
from app_logging import loging_cur_time

loging_cur_time('/home/georgis/projects/app_logs/','slack_swp.log', 'Start slack parsing ...')
#Define the RSS feeds source 
python_sans_rss_url = "https://www.sans.org/tip-of-the-day/rss"
#Define the webhook from SLACK specific application, created in api.slack.com.
#URL of the slack API application - https://api.slack.com/apps/
#The webhook generated for the "malta" channel.
#You can change the channel and generate new webhook
webhook_url= "https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#Creating var feed for specifik RSS URL
feed = feedparser.parse( python_sans_rss_url )

#Reading all RSS entries
for post in feed["entries"]:
	
#Define the SLACK post variables - post title, post link and post description
	post_title=post.title
	post_link=post.link
	post_descr=post.description
	slack_data = {'text': "*For more info follow the link...*", "attachments": [{"title": post_title,"pretext": post_link,"text": post_descr,"mrkdwn_in":["text","pretext"]}]}

#Define Slack Response
	response = requests.post(webhook_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})

#Checking for the HTTP status code and handle the exception
	if response.status_code != 200:
		raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))
#Define sleep time
	time.sleep(3600)

loging_cur_time('/home/georgis/projects/app_logs/','slack_swp.log', 'End slack parsing ...')
