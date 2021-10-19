import praw
from praw.models import MoreComments

#creating a reddit instance (if you want to read public posts, there is no need to login)
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="RBotProject",
    password="")

#grab a subreddit from reddit using reddit instance
subreddit = reddit.subreddit("RBotProject")

#loop through first 10 hot submissions in subreddit and post the title and score
for submission in subreddit.hot(limit=10):
    print("**********")
    #print title of posts
    print(submission.title)
    #print post score(upvotes - downvotes)
    print("Score: ", submission.score)

    #loop through all comments in a submission and look for the word "test"
    for comment in submission.comments:
        #making sure all the words in the comment is lowercase
        comment_lower = comment.body.lower()
        #This is to ignore the "Load more comments" object on Reddit
        if isinstance(comment, MoreComments):
            continue
        if " test " in comment_lower:
            print("--------")
            print(comment.body)
            #If the word "test" is in the comment, reply with:
            comment.reply("It did! *Bot Reply*")
