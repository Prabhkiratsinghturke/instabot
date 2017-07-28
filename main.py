import requests,urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from termcolor import colored
import time



app_access_token = ''            #app access token.....

base_url = "https://api.instagram.com/v1/"                                          #base url for request url.....

print "HELL0 ! What's up..."
print "' WELCOME ' to ' INSTABOT '"


# Function declaration to get your own information starts.....
def self_info():

    print"\nSELF INFO :\n"
    request_url =(base_url + 'users/self/?access_token=%s') % (app_access_token)
    print "\tGET request url : %s" % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print '\n\t* USERNAME: %s' % (user_info['data']['username'])
            print '\n\t  -No. of FOLLOWERS: %s' % (user_info['data']['counts']['followed_by'])
            print '\t  -No. of people you are FOLLOWING: %s' % (user_info['data']['counts']['follows'])
            print '\t  -No. of POSTS: %s' % (user_info['data']['counts']['media'])
        else:
            print colored('User does not Exist!!!',' red')
    else:
        print colored('Status code other than 200 received!', 'red')
 # Function declaration to get your own information ends.....



# Function declaration to get the ID of a user by username starts.....
def get_user_id(instabot_username):


    request_url = (base_url + 'users/search?q=%s&access_token=%s') % (instabot_username, app_access_token)
    print "\tGET request url : %s" % request_url
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print colored('\tStatus code other than 200 received!', 'red')
        return None
        exit()
  # Function declaration to get the ID of a user by username ends.....



# Function declaration to get the info of a user by username starts......
def get_user_info(instabot_username):

    print"\nGET USER INFO :\n"
    user_id = get_user_id(instabot_username)
    if user_id == None:
        print colored('\n\tUser does not exist !...', 'red')
        exit()
    request_url = (base_url + 'users/%s?access_token=%s') % (user_id, app_access_token)
    print '\tGET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print '\n\t* Username: %s' % (user_info['data']['username'])
            print '\n\t  -No. of FOLLOWERS: %s' % (user_info['data']['counts']['followed_by'])
            print '\t  -No. of people you are FOLLOWING: %s' % (user_info['data']['counts']['follows'])
            print '\t  -No. of POSTS: %s' % (user_info['data']['counts']['media'])
        else:
            print colored('There is no data for this user!', 'red')
    else:
        print colored('Status code other than 200 received!', 'red')
# Function declaration to get the info of a user by username ends......



#Function declaration to get your recent post starts.....
def get_own_post():

    print"\nGET OWN POST :\n"
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
    print '\tGET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:

        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print '\n\t  Your image has been Downloaded !...'

        else:
            print colored('\n\t  Post does not Exist !...', 'red')

    else:
        print colored('\n\tStatus code other than 200 received!', 'red')
#Function declaration to get your recent post ends.......



#Function declaration to get the recent post of a user by username starts.....
def get_user_post(instabot_username):

    print"GET USER POST :\n"
    user_id = get_user_id(instabot_username)
    if user_id == None:
        print colored('\tUser does not exist!', 'red')
        exit()

    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:

        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print colored('\n\t   Your image has been downloaded!', 'blue')

        else:
            print colored('\tPost does not exist!', 'red')

    else:
        print colored("  Status code other than 200 received!!!",'red')
#Function declaration to get the recent post of a user by username ends.....



#Function declaration to get the ID of the recent post of a user by username starts....
def get_a_post_id(instabot_username):

    user_id = get_user_id(instabot_username)
    if user_id == None:
        print colored('\tUser does not exist!', 'red')
        exit()

    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
    print "\tGET request url : %s" % request_url
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:

        if len(user_media['data']):
            return user_media['data'][0]['id']

        else:
            print colored('\n\t  There is no recent post of the user !', 'red')
            exit()

    else:
        print colored('\n\tStatus code other than 200 received !', 'red')
        return None
        exit()
#Function declaration to get the ID of the recent post of a user by username ends....



#Function declaration to like the recent post of a user starts.....
def like_a_post(instabot_username):

    print"\nLIKE A POST :\n"
    media_id = get_a_post_id(instabot_username)
    request_url = (base_url + 'media/%s/likes') % media_id
    payload = {"access_token": app_access_token}
    print '\tPOST request url : %s' % request_url
    post_like = requests.post(request_url, payload).json()
    if post_like['meta']['code'] == 200:
        print '\n\t  Like successful...'
    else:
        print colored('\n\t  Your like was unsuccessful. Try again !..', 'red')
#Function declaration to like the recent post of a user ends.....



#Function declaration to get list of likes from a post starts...
def get_like_list(instabot_username):            # Definition of the Function ............
    print"\nGET LIKE LIST :\n"
    media_id = get_a_post_id(instabot_username)  # Getting post id by passing the username .......
    request_url = base_url + 'media/%s/likes?access_token=%s' % (media_id, app_access_token)    #    passing the end points and media id along with access token ..
    print colored('GET request url : %s\n', 'blue') % (request_url)
    like_list = requests.get(request_url).json()

    if like_list['meta']['code'] == 200:  # checking the status code .....
        if len(like_list['data']):
            position = 1
            print colored("\n\t  List of people who Liked Your Recent post", 'blue')
            for users in like_list['data']:
                if users['username'] != None:
                    print '\n\t     ', position,'. ', colored(users['username'], 'green')
                    position = position + 1
                else:
                    print colored('\n\t  No one had liked Your post!\n', 'red')
        else:
            print colored("\n\t User Does not have any post.\n", 'red')
    else:
        print colored('\n\tStatus code other than 200 recieved.\n', 'red')
    time.sleep(5)
#Function declaration to get list of likes from a post ends...


#Function declaration to post a comment on a post starts...
def post_a_comment(instabot_username):

    print"\nCOMMENT ON POST :\n"
    media_id = get_a_post_id(instabot_username)
    comment_text = raw_input(colored("\n\t\tYour comment: ", 'green'))
    payload = {"access_token": app_access_token, "text" : comment_text}
    request_url = (base_url + 'media/%s/comments') % media_id
    print '\n\tPOST request url : %s' % request_url

    make_comment = requests.post(request_url,payload).json()
    print make_comment
    if make_comment['meta']['code'] == 200:
        print "\n\tSuccessfully added a new comment!"
    else:
        print colored("\n\tUnable to add comment. Try again!", 'red')
# Function declaration to post a comment on a post ends...



#Function declaration to get list of comments from a post starts...
def get_comment_list(instabot_username):  # Defining the Function ............

    print"\nGET COMMENT LIST :\n"
    media_id = get_a_post_id(instabot_username)  # Getting post id by passing the username .......
    request_url = base_url + 'media/%s/comments?access_token=%s' % (media_id, app_access_token)   #    passing the end points and media id along with access token ..
    print '\tGET request url : %s\n' % (request_url)
    comment_list = requests.get(request_url).json()

    if comment_list['meta']['code'] == 200:  # checking the status code .....
        if len(comment_list['data']):
            position = 1
            print colored('\n\t List of people who commented on Your Recent post : %d', 'blue') % (len(comment_list['data']))
            for _ in range(len(comment_list['data'])):
                if comment_list['data'][position-1]['text']:
                    print '\n\t   ',colored(comment_list['data'][position-1]['from']['username'],'green') +colored( ' said : ','green') + colored(comment_list['data'][position-1]['text'],'blue')      #    Json Parsing ..printing the comments ..
                    position = position+1
                else:
                    print colored('\n\t    No one had commented on Your post!\n', 'red')
        else:
            print colored('\n\t  There is no Comments on User\'s Recent post.\n', 'red')
    else:
        print colored('\n\tStatus code other than 200 recieved.\n', 'red')

    time.sleep(5)
#Function declaration to get list of comments from a post ends...


#Function declaration to make delete negative comments from the recent post starts...
def delete_negative_comment(instabot_username):
    media_id = get_a_post_id(instabot_username)
    request_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, app_access_token)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):

            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (base_url + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, app_access_token)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'
    time.sleep(5)
#Function declaration to make delete negative comments from the recent post ends....


#definition of start_instabot()
def start_instabot():


    while True:


        print "\n MENU :"
        print "\n\t1. Get your own details."
        print "\t2. Get details of a user by username."
        print "\t3. Get your own recent post."
        print "\t4. Get the recent post of a user by username."
        print "\t5. Get a list of people who have liked the recent post of a user."
        print "\t6. Like the recent post of a user."
        print "\t7. Get a list of comments on the recent post of a user."
        print "\t8. Make a comment on the recent post of a user."
        print "\t9. Delete negative comments from the recent post of a user."
        print "\t10. Exit.\n"

        question ="  Please,Enter your Choice: "

        menu_choice = raw_input(question)
        menu_choice = int(menu_choice)
        print"\n"
        if menu_choice > 0 and menu_choice < 11:

            if menu_choice == 1:
                self_info()

            elif menu_choice == 2:
                instabot_username = raw_input("Please,Enter the username of the user: ")
                get_user_info(instabot_username)
            elif menu_choice == 3:
                get_own_post()
            elif menu_choice == 4:
                instabot_username = raw_input("Enter the username of the user: ")
                get_user_post(instabot_username)
            elif menu_choice == 5:
                instabot_username = raw_input("Enter the username of the user: ")
                get_like_list(instabot_username)
            elif menu_choice == 6:
                instabot_username = raw_input("Enter the username of the user: ")
                like_a_post(instabot_username)
            elif menu_choice == 7:
                instabot_username = raw_input("Enter the username of the user: ")
                get_comment_list(instabot_username)
            elif menu_choice == 8:
                instabot_username = raw_input("Enter the username of the user: ")
                post_a_comment(instabot_username)
            elif menu_choice == 9:
                instabot_username = raw_input("Enter the username of the user: ")
                delete_negative_comment(instabot_username)
            elif menu_choice == 10:
                exit()
        else:
            print colored(" 'WARNING' Please, Enter Correct Choice !!!", 'red')
            exit()

start_instabot()
