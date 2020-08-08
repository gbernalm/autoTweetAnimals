import tweepy, os, time, random, shutil

lastComment = ''
Comment_Types = ['comments.txt', 'ClassComments.txt']
PostTypes = ['other', 'dog', 'cat', 'bird']
directory = 'D:\Pictures\ '
directory = directory.strip()
dst = 'D:\Pictures\\Used\\'


# Comment choosing:
def Comment_choose(classification):
    if classification != 'other':
        Types = random.choice(Comment_Types)
        txtFile = open(Types, "r")
        comments = []
        commentline = txtFile.readline()
        while commentline != "":
            commentline = txtFile.readline()
            commentline = commentline.strip('\n')
            comments.append(commentline)

        latestComment = random.choice(comments)

        while latestComment == lastComment:
            latestComment = random.choice(comments)
        if Types == 'ClassComments.txt':
            latestComment = latestComment.replace('&&&&', classification)
        txtFile.close()
        return latestComment
    else:
        txtFile = open('comments.txt', "r")
        comments = []
        commentline = txtFile.readline()
        while commentline != "":
            commentline = txtFile.readline()
            commentline = commentline.strip('\n')
            comments.append(commentline)
        latestComment = random.choice(comments)
        while latestComment == lastComment:
            latestComment = random.choice(comments)
        txtFile.close()
        return latestComment


postingTime = [13, 18]  # Hours to post
minute_Post = 30  # Minute to post
# Authenticate to Twitter
auth = tweepy.OAuthHandler("",
                           "")
auth.set_access_token("#-#",
                      "")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

# load image
imagePath = ''
comment = ''


def Pic_choose(classification):
    Picname = random.choice(os.listdir(directory + classification))
    pic = directory + classification + '\\' + Picname
    return pic


def checktime():
    rightnow = time.localtime()
    hrs = rightnow.tm_hour
    mns = rightnow.tm_min
    secs = rightnow.tm_sec
    return hrs, mns


Posted = False
print('Start!')

while True:
    hours, minutes = checktime()

    if hours in postingTime and minutes == minute_Post and Posted is False:

        print(hours, minutes)
        try:
            classification = random.choice(PostTypes)
            comment = Comment_choose(classification)
            imagePath = Pic_choose(classification)
            api.update_with_media(imagePath, comment)
            shutil.move(imagePath, dst)
            Posted = True
            print("Posted!")
        except:
            print("Sorry mate, didn't work...")

    if hours in postingTime and minutes == minute_Post + 10 and Posted is True:
        Posted = False
