# Slack_bot
This Slack bot is an interactive and helpful bot. Using Slack's Real Time Messaging API, this bot notifies all the messages in which the user is mentioned or tagged and can even reply for most of the messages appropriately. 

Contains three files - 
1. `discover.py` checks whether the bot is working or not. Moreover, it tells us the id of our bot associated with the slack.
2. `vibhor_bot.py` starts the bot.
3. `source.sh` contains all the api tokens.
4. `lang_translator.py` translates the script into any language specified by the user. Works on the google translator module named as `googletrans`. It is one of the best features that gives the user a sense of multilinguality. It is highly beneficial for the professionals having trouble in speaking local languages.
5. `Scrabble.py` integrates scrabble helper to the Slack bot. It helps the user in getting all the valid words from the given rack of words. Thus, it helps the user to play and win the mind game- Scrabble.

## Basic Features
1. This bot replies the user for the messages (public or private) in which the user is `@mentioned` or tagged. 

2. Recognizes `['hello', 'hi', 'hey', 'hola', 'sup', 'yo', 'ohai', 'morning', 'bonjour']` messages and can even reply appropriately as `['Hello {mention}...', 'Hi {mention}!', 'Hola!']` where {mention} specifies the username of the person to whom message is to be sent.

3. Recognizes `['bye', 'cya', 'goodbye', 'later']` messages and can reply as - `['Bye {mention}', 'See you Later', 'See you soon!']`

4. Recognizes `['how are you', "what's up", 'tell me about you', "what's going on", "how it's going", "how have you been", "are you well", 'how are you keeping', 'what have you been up to', "what's happening"]` and can even reply as - `["I'm fine {mention}", 'Nice', 'Fit and Healthy', 'Awesome! {mention}', 'Fine, thanks', 'Great! How are you doing?', "I've been better"]`.

5.  Google search- just input a query and you would get top 5 results.
    Format->    google query
    
6.  Twitter search- just input a query and you would get 15 latest tweets and retweets about that query.
    Format->    twitter query
    
7.  Weather- You can know weather conditions of any city in the world just by typing in this format...
    Format->    weather city_name
                weather at city_name
                
8.  Translator- Well this the hallmark quality of scrabble that it can sentence written in English to any preferred language.
    Format->    translate hi- sentence
                here hi is language code for hindi, similarly->
                Dutch: nl
                French: fr
                Spanish: de
                Danish: da
                English: en
                
9.  Movie rating- By using this feature you can access IMDb rating of any movie broadcasted in the world.
    Format->    movie rating of name_of_movie
    
10.  Hotel rating- Over and above this feature can tell you rating of any hotels in India and that too in a spur of a moment.
    Format->    hotel rating of name_of_hotel place
    
11.  Scrabble word maker- It can tremendously generate possible words from the given set of letters. Also, it provides us the scrabble score of each word.
    Format->    scrabble set_of_letters
                jumble set_of_letters
        
12.  And last but not the least, whenever you say `'bye', 'goodbye', 'revoir', 'adios', 'later' or 'cya'....`
    Then in a doleful way, it says `'see you later, alligator...','adios amigo','Bye !' or 'Au revoir!'` because it doesn't want to leave you...

There can be lots of improvements here and new features can be added too. Contributors are welcomed!:)
