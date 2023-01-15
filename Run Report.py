import json

# read json file
followers_path = open('followers.json')
following_path = open('following.json')

# load as json object
followers = json.load(followers_path)
following = json.load(following_path)

# holds values
all_followers = []
all_following = []

# loop for collecting user who you are following
for entity_data in following['relationships_following']:
    user_info = entity_data['string_list_data']
    for values in user_info:
        all_followers.append([values['value'], values['href'] ])


# loop for collecting users that follow you
for entity_data in followers['relationships_followers']:
    user_info = entity_data['string_list_data']
    for values in user_info:
        all_following.append([values['value'], values['href'] ])

# loop for finding users not following back
not_following_back = []
for user in all_followers:
    if user not in all_following:
        not_following_back.append(user)
        
# sort by name
not_following_back.sort(key=lambda x: x[0])

        
# write all users not following back to file
f = open("Report.txt", "w")
f.write("\n~DOES NOT FOLLOW BACK~\nHandle | Link\n--------------\n")
for user in not_following_back:
    f.write(user[0] + ' - ' + user[1] + '\n')    
f.close()



