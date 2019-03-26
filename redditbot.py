# bigwordbot

import praw
from PyDictionary import PyDictionary

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='ABE3GvD7NVP6yA',
                    client_secret='_Zlz0wpMDBtyeyL_vDXITVgDhxc',
                    username='safetick',
                    password='Charlie199104',
                    user_agent='SafeTick bot created for MTIA 2019')


# dictionary and word check

# check if the word is real
commands  =['safe', 'unsafe']

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('SafeTick')

# phrase to activate the bot
keyphrase = '!bot'

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        try:
            if comment.body == "safe":
                # get meaning as object, get the index of a sentence and reply it
                comment.reply('Hello.')
                print('posted')
            else:
                reply = 'This is not a word.'
                comment.reply(reply)
                print('posted')
        except:
            print('to frequent')
