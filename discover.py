
import os, slackclient

VIBHOR_SLACK_TOKEN = os.environ.get('VIBHOR_SLACK_TOKEN')
VIBHOR_SLACK_NAME = os.environ.get('VIBHOR_SLACK_NAME')

#VIBHOR_SLACK_TOKEN='xoxb-207770090644-nuaIgpyyG8eX48voyZAb5Mgd'
#VIBHOR_SLACK_NAME='vibhor_bot'

#initialise the slack client
vibhor_slack_client = slackclient.SlackClient(VIBHOR_SLACK_TOKEN)

#check if everything is alright
print VIBHOR_SLACK_NAME
print VIBHOR_SLACK_TOKEN
is_ok = vibhor_slack_client.api_call('users.list').get('ok')
print is_ok

# need to find id of our bot
if is_ok:
    for user in vibhor_slack_client.api_call('users.list').get('members'):
        if user.get('name') == VIBHOR_SLACK_NAME:
            print user.get('id')
