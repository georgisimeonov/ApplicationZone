#!/usr/bin/env python3

########################################################################
# Use a script to config and test you cronjob
# Example:
# * * * * * /home/user/bin/test_cron.py >> /home/user/crontab_log/cron.listener.log 2>&1
# This command in crontab will put every minute a line with the curent time in file cron.listener
# Replace the path and the test_cron.py file with your scripti after the test 

# This function creates a log file and writes a message for a script activity adding the current time

import time
def loging_cur_time(path_to_log, log_file_name, log_msg):

	localtime = time.asctime(time.localtime(time.time()))
	
	total_log = path_to_log + log_file_name
	total_msg= log_msg + " " + localtime + "\n"
	try:
		open_log = open(total_log,'a')
	except OSError:
		print("Cannot open: ", total_log)
	else:
		open_log.write(total_msg)
		open_log.close()


loging_cur_time('/home/georgis/projects/app_logs/','slack_swp.log', 'This is a test log')
#localtime = time.asctime(time.localtime(time.time()))
#print(["This is a crontab test, generated at:", localtime], end="\n", file='test.log' )
#title = "test...... \n"
#log_file = '/home/georgis/projects/app_logs/slack_swp.log'
#open_log = open(log_file,'w')
#open_log.write(title)
#open_log.write(localtime)
#print('title')
#open_log.close()
