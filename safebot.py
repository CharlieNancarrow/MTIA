# bigwordbot

import praw

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='ABE3GvD7NVP6yA',
                    client_secret='_Zlz0wpMDBtyeyL_vDXITVgDhxc',
                    username='safetick',
                    password='Charlie199104',
                    user_agent='SafeTick bot created for MTIA 2019')


# dictionary and word check

# check if the word is real

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('safeticktest')

# phrase to activate the bot
safe_keyphrase = '!safe'
unsafe_keyphrase = '!unsafe'

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if safe_keyphrase or unsafe_keyphrase in comment.body:
        try:
            if safe_keyphrase:
                reply = 'Thanks for the REVIEW'
                comment.reply(reply)
                print('add to safe')
                print('sent')
            elif unsafe_keyphrase:
                reply = 'Thanks for the REVIEW'
                comment.reply(reply)
                print('add to unsafe')
                print('sent')
        except:
            print('to frequent')
