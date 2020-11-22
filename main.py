import random

def binary_search(l, v):
    """
    (list, int) -> int

    Prend une liste et un entier v. Retourne l'index de l'entier v si'il exist dans la liste.
    Précondition: la liste est triée
    """
    gauche = 0
    droite = len(l)-1
    milieu = int(droite/2)
    while gauche <= droite:
        if v == l[milieu]:
            return milieu
        elif v < l[milieu]:
            droite = milieu-1
            milieu = int((gauche+droite)//2)
        elif v > l[milieu]:
            gauche = milieu+1
            milieu = int((gauche+droite)//2)
    return -1

def binary_search_network(user, network):
    """
    (int, list) -> int
    Searches for the user in the network and returns the index of the tuple that contains the user.
    Returns -1 if the user does not exist.
    Preconditon: the network is sorted from lowest to highest

    >>> 2 , [(0, [1, 2, 3]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6, 8, 9]), (3, [0, 2, 8, 9]), (4, [1, 6, 7, 8]),
    (5, [9]), (6, [1, 2, 4, 8]), (7, [1, 4, 8]), (8, [2, 3, 4, 6, 7]), (9, [1, 2, 3, 5])]
    Output: 3
    """
    left = 0
    right = len(network) - 1
    mid = int(right / 2)
    while left <= right:
        if user == network[mid][0]:
            return mid
        elif user < network[mid][0]:
            right = mid - 1
            mid = int((left + right) // 2)
        elif user > network[mid][0]:
            left = mid + 1
            mid = int((left + right) // 2)
    return -1


def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    # friends = open(file_name).read().splitlines()
    # network = []
    # list_IDs = list()
    # list_friends = list()
    # final_list = list()
    # ID_index = 0
    #
    # # YOUR CODE GOES HERE
    # for i in range(len(friends)):
    #     friends[i] = friends[i].split()
    # del friends[0]  # deletes the # of people in the network from the list
    #
    # # convert all items in the list from str to int
    # for i in range(len(friends)):
    #     for j in range(len(friends[i])):
    #         friends[i][j] = int(friends[i][j])
    #
    # # remove all duplicate IDs and put them into a list of IDs
    # for i in range(len(friends)):
    #     if friends[i][0] not in list_IDs:
    #         list_IDs.append(friends[i][0])
    # print(list_IDs)
    #
    # # if the ID part from friends is equal to the list of IDs, keep adding the FRIENDS part from friends
    # # to a new list called list_friends
    # for i in range(len(friends)):
    #     if friends[i][0] == list_IDs[ID_index]:
    #         list_friends.append(friends[i][1])
    #     else:
    #         final_list.append((list_IDs[ID_index], list_friends.copy()))
    #         ID_index += 1
    #         list_friends.clear()
    #         # append any friends from previous IDs into the new list_friends FIRST, then proceed with next tasks
    #         for j in range(ID_index):
    #             if list_IDs[j] in final_list[j]:
    #                 list_friends.append(list_IDs[j])
    #         list_friends.append(friends[i][1])  # immediately make a new list of friends for the next user
    #
    # # the loop above does not append the final user and his/her friends, so, append it now
    # final_list.append((list_IDs[ID_index], list_friends.copy()))
    #
    # print("final", final_list)
    #
    # # copy the final_list to network
    # network = final_list.copy()
    #
    # # delete all lists to free up memory
    # list_IDs.clear()
    # list_friends.clear()
    # final_list.clear()
    # return network
    friends = open(file_name).read().splitlines()
    network = []

    list_IDs = list()
    temp_network = []

    for i in range(len(friends)):
        friends[i] = friends[i].split()
    del friends[0]  # deletes the # of people in the network from the list

    # convert all items in the list from str to int
    for i in range(len(friends)):
        for j in range(len(friends[i])):
            friends[i][j] = int(friends[i][j])

    # remove all duplicate IDs and put them into a list of IDs
    for i in range(len(friends)):
        if friends[i][0] not in list_IDs:
            list_IDs.append(friends[i][0])
        if friends[i][1] not in list_IDs:
            list_IDs.append(friends[i][1])
        # if binary_search(list_IDs, friends[i][0]) is False:
        #     list_IDs.append(friends[i][0])
        # if binary_search(list_IDs, friends[i][1]) is False:
        #     list_IDs.append(friends[i][1])
    list_IDs.sort()
    # print(list_IDs)

    # add each IDs' list of friends into a list which will be added to the network later
    for j in range(0, len(list_IDs)):
        for k in range(0, len(friends)):
            if list_IDs[j] == friends[k][0]:
                temp_network.append(friends[k][1])
            if list_IDs[j] == friends[k][1]:
                temp_network.append(friends[k][0])
        tupples = (list_IDs[j], temp_network.copy())
        temp_network.clear()
        network.append(tupples)
    return network


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs,
    and friends of user 1 and user 2 sorted
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common = []

    # find index for user1 and user2
    i_user1 = 0
    i_user2 = 0
    # for i in range(len(network)):
    #     if network[i][0] == user1:
    #         i_user1 = i
    #         i = len(network)-1  # break out of loop. this is better than break
    # for i in range(len(network)):
    #     if network[i][0] == user2:
    #         i_user2 = i
    #         i = len(network) - 1  # break out of loop. this is better than break

    i_user1 = binary_search_network(user1, network)
    i_user2 = binary_search_network(user2, network)

    # find common friends
    for i in range(len(network[i_user1][1])):
        for j in range(len(network[i_user2][1])):
            if network[i_user1][1][i] == network[i_user2][1][j]:
                common.append(network[i_user1][1][i])
    return common

# print("Getcommonfriends")
# print(getCommonFriends(3, 1, [(0, [1, 2, 3]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6, 8, 9]), (3, [0, 2, 8, 9]), (4, [1, 6, 7, 8]),
# (5, [9]), (6, [1, 2, 4, 8]), (7, [1, 4, 8]), (8, [2, 3, 4, 6, 7]), (9, [1, 2, 3, 5])]))
# print("next\n")
# print(getCommonFriends(0, 112, [(0, [1, 2, 3, 4, 5, 6, 7, 8, 9]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6,8, 9]), (3, [0, 2, 8, 9]), (4, [0, 1, 6, 7, 8]),
# (5, [0, 9]), (6, [0, 1, 2, 4, 8]), (7, [0, 1, 4, 8]), (8, [0, 2, 3, 4, 6, 7]), (9, [0, 1, 2, 3, 5]),
# (100, [112]), (112, [100, 114]), (114, [112])]))


def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.

    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # # linear search for the user's tuple index in the network
    # for i in range(len(network)):
    #     if user == network[i][0]:
    #         user_friends = network[i][1].copy()

    # look for the user's list of friends from the network
    # binary for the user's tuple index in the network
    user_index = binary_search_network(user, network)
    user_friends = network[user_index][1].copy()

    length_most_common_friends = 0
    recommended_ID = -1  # ID of the user that will be recommended to the user
    for i in network:
        if user != i[0] and i[0] not in user_friends:
            # list of common friends between the user and the user we are comparing to
            common_friends = getCommonFriends(user, i[0], network)
            # find the user with the most mutual friends
            if len(common_friends) > length_most_common_friends:
                length_most_common_friends = len(common_friends)
                recommended_ID = i[0]

    return recommended_ID


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    num_users = 0
    for i in network:
        if len(i[1]) >= k:
            num_users += 1
    return num_users

# print(k_or_more_friends([(0, [1, 2, 3]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6, 8, 9]), (3, [0, 2, 8, 9]), (4, [1, 6, 7, 8]),
# (5, [9]), (6, [1, 2, 4, 8]), (7, [1, 4, 8]), (8, [2, 3, 4, 6, 7]), (9, [1, 2, 3, 5])], 5))

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # returns the number of friends the user with the most friends has
    highest_friends = 0
    for i in network:
        if len(i[1]) > highest_friends:
            highest_friends = len(i[1])
    return highest_friends

# print(maximum_num_friends([(0, [1, 2, 3]), (1, [0, 4, 6, 7, 9]), (2, [0, 3, 6, 8, 9]), (3, [0, 2, 8, 9]), (4, [1, 6, 7, 8]),
# (5, [9]), (6, [1, 2, 4, 8]), (7, [1, 4, 8]), (8, [2, 3, 4, 6, 7]), (9, [1, 2, 3, 5])]))


def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends = []
    hf = maximum_num_friends(network)
    for i in network:
        if len(i[1]) == hf:
            max_friends.append(i[0])
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''
    total_friends = 0
    for i in network:
        total_friends += len(i[1])
    avg = float(total_friends / len(network))
    return avg


def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''

    # reads the first "word" in the textfile and convert it to an int
    total_users = int(open(file_name).read().split()[0])
    max_possible_friends = total_users - 1
    for i in network:
        if len(i[1]) == max_possible_friends:
            return True
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''

    ID_exists = False
    while ID_exists is False:
        try:
            ID = int(input("Enter the ID of the user you are looking for: "))
            for i in network:
                if ID == i[0]:
                    ID_exists = True
                    break
            if ID_exists is False:
                print("ERROR: The ID you are looking for does not exist in the network.")
        except:
            print("ERROR: That was not an integer")
    return ID



##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name = get_file_name()

net = create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is " + str(
    maximum_num_friends(net)) + ".")
print("The average number of friends is " + str(average_num_friends(net)) + ".")
mf = people_with_most_friends(net)
print("There are", len(mf), "people with " + str(maximum_num_friends(net)) + " friends and here are their IDs:",
      end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k = random.randint(0, len(net) // 4)
print("\nThat number is: " + str(k) + ". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net, k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid = get_uid(net)
rec = recommend(uid, net)
if rec == None:
    print("We have nobody to recommend for user with ID", uid,
          "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid, "we recommend the user with ID", rec)
    print("That is because users", uid, "and", rec, "have", len(getCommonFriends(uid, rec, net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1 = get_uid(net)
print("About 2st user ...")
uid2 = get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common = getCommonFriends(uid1, uid2, net)
for item in common:
    print(item, end=" ")


