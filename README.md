# Slack_bot
Using Slack API, this bot notifies all the messages in which the user is mentioned or tagged and can even reply for some recognised messages. 

Contains three files - 
1. discover.py checks whether the bot is working or not. Moreover, it tells us the id of our bot associated with the slack.
2. vibhor_bot.py starts the bot.
3. source.sh contains all the api tokens.

## Basic Features
1. This bot notifies the user about the messages (public or private) in which the user is @mentioned or tagged. 

2. Recognizes ['hello', 'hi', 'hey', 'hola', 'sup', 'yo', 'ohai', 'morning', 'bonjour'] messages and can even reply appropriately as ['Hello {mention}...', 'Hi {mention}!', 'Hola!'] where {mention} specifies the username of the person to whom message is to be sent.

3. Recognizes ['bye', 'cya', 'goodbye', 'later'] messages and can reply as - ['Bye {mention}', 'See you Later', 'See you soon!']

4. Recognizes ['how are you', "what's up", 'tell me about you', "what's going on", "how it's going", "how have you been", "are you well", 'how are you keeping', 'what have you been up to', "what's happening"] and can even reply as - ["I'm fine {mention}", 'Nice', 'Fit and Healthy', 'Awesome! {mention}', 'Fine, thanks', 'Great! How are you doing?',"I've been better"].

 
