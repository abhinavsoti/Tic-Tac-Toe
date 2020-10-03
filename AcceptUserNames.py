import os
import datetime

def acceptusernames():
    user1 = input('Please enter first player name: ')
    user2 = input('Please enter second player name: ')
    print ('Thanks ' + user1 + ' & ' + user2 + ' for registering')
    print ('Lets Start Now')
    registeredUser = user1 + '|' + user2
    return registeredUser