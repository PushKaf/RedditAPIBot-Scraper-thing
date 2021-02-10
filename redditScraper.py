import praw
import matplotlib.pyplot as plt
import numpy as np


#pick subreddit to scan through
subreddit = ""

#enter your reddit API credentials, REQUIRED
reddit = praw.Reddit(
     client_id="",
     client_secret="",
     user_agent=""
)

subRedditToScan = reddit.subreddit(subreddit)

#add to this dict what you want scanned, so EXAMPLE:
#"hello":0           It will scan for the word, "hello". 
picksDict = {}

#loops through the comments
for submission in subRedditToScan.hot(limit=2):
    for comment in submission.comments:
        if hasattr(comment, "body"):
            lowerComments = comment.body.lower()
            for word in lowerComments.split(" "):
                if word in picksDict:
                    picksDict[word] += 1
                    # print(picksDict)

#matplotlib bar graph
plt.bar(list(picksDict.keys()), list(picksDict.values()), color='aqua')
plt.ylabel("# Of Comments")
plt.xlabel("Words")
plt.title(f"Talked About In: {subreddit}")
plt.show()
