import os, time, random, slackclient
import json, urllib2

#delay in secs
SOCKET_DELAY = 1

#slackbot environment variables
VIBHOR_SLACK_TOKEN = os.environ.get('VIBHOR_SLACK_TOKEN')
VIBHOR_SLACK_NAME = os.environ.get('VIBHOR_SLACK_NAME')
VIBHOR_SLACK_ID = os.environ.get('VIBHOR_SLACK_ID')

#VIBHOR_SLACK_TOKEN='xoxb-207770090644-nuaIgpyyG8eX48voyZAb5Mgd'
#VIBHOR_SLACK_NAME='vibhor_bot'
#VIBHOR_SLACK_ID='U63NN2NJY'

#initialise the slack client
vibhor_slack_client = slackclient.SlackClient(VIBHOR_SLACK_TOKEN)

#checks if mesg is privately for the user or mentioned for the user in public chat
def is_for_me(event):
    msg_type = event.get('type')
    if msg_type and msg_type=='message' and not(event.get('user') == VIBHOR_SLACK_ID):
        if is_private(event):
            return True
        text = event.get('text')
        if vibhor_slack_mention in text.strip().split():
            return True
    return False

#checks if Slack channel is private
def is_private( event):
    return event.get('channel').startswith('D')     #as private channel startswith 'D'

def get_mention(user):
    return '<@{user}>'.format( user=user)

vibhor_slack_mention = get_mention( VIBHOR_SLACK_ID)        #way the bot is mentioned in the chats

def is_hi(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any( word in tokens for word in ['hello', 'hi', 'hey', 'hola', 'sup', 'yo', 'ohai', 'morning', 'bonjour'])

def is_bye(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any( word in tokens for word in ['bye', 'cya', 'goodbye', 'later'])

def is_time( message):
    message.replace('?', '')
    return any( st in message.strip().lower() for st in ['time', 'what is the hour of the day', 'tell me the date today', "what's the day today", 'date', "what's the date today"])

def say_hi(user_mention):
    response = random.choice(['Hello {mention}...', 'Hi {mention}!', 'Hola!'])
    return response.format( mention=user_mention)

def say_bye(user_mention):
    response = random.choice(['Bye {mention}', 'See you Later', 'See you soon!'])
    return response.format( mention=user_mention)


def is_how_r_u( message):
    message.replace('?', '')
    return any( st in message.strip().lower() for st in ['how are you', "what's up", 'tell me about you', "what's going on", "how it's going", "how have you been", "are you well", 'how are you keeping',
                                                        'what have you been up to', "what's happening"])

def say_about_u (user_mention):
    response = random.choice(["I'm fine {mention}", 'Nice', 'Fit and Healthy', 'Awesome! {mention}', 'Fine, thanks', 'Great! How are you doing?',"I've been better"])
    return response.format( mention=user_mention)


def tell_time(user_mention):
    return str(time.ctime()) + str(user_mention)


def is_weather( message):
    return any( message.strip().lower().startswith(st) for st in ['weather', 'tell me weather'])


def weather_forecast(place):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast?q='
    url = base_url + place + 'india&APPID=041d68834f4ca8f569d71cd6df88ae61'
    data = json.load(urllib2.urlopen(url))
    return data


def tell_weather( message, channel):
    place = message.split()[-1]
    data2 = weather_forecast(place)
    post_message('Condition: ' + data2['list'][0]['weather'][0]['main'] + ' (' + data2['list'][0]['weather'][0]['description']   
                 + ')', channel)
    post_message('Temperature: ' + str(float(data2['list'][0]['main']['temp']) - 273.15) + ' Celsius', channel)

#posts a response to the channel on behalf of the user
def post_message( message, channel):
    vibhor_slack_client.api_call( 'chat.postMessage', text=message,
                                  channel=channel, as_user=True)

def handle_message(message, user, channel):
    if is_hi( message):
        mention = get_mention(user) 
        post_message( say_hi(mention), channel)
    elif is_bye( message):
        mention = get_mention(user)
        post_message( say_bye(mention), channel)
    elif is_how_r_u( message):
        mention = get_mention( user)
        post_message( say_about_u(mention), channel)
    elif is_time( message):
        mention = get_mention( user)
        post_message( tell_time(mention), channel)
        
    elif is_weather( message):
        tell_weather(message, channel)
        
    else:
        post_message("Not sure what you have just said!", channel)

#main()    
def run():
    if vibhor_slack_client.rtm_connect():
        print '[.] Slack bot is ONN'
        while True:
            event_list = vibhor_slack_client.rtm_read()
            if len( event_list)>0:
                for event in event_list:
                    print event
                    if is_for_me( event):
                        handle_message( message=event.get('text'),
                        user=event.get('user'), channel=event.get('channel'))
                    
                    if event.get('type') == 'typing':
                        print 'Typing...'

                    if str(datetime.now()).split()[1] == '00:00:00':
                        post_message(message="It's midnight of %s" % (str(datetime.now()).split()[0]), channel=event.get('channel'))     
            
            time.sleep( SOCKET_DELAY)
    else:
        print '[!] Connection to the Slack failed'

if __name__ == '__main__':
    run()
