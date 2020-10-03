import os
import datetime

os.system("python display_information.py")
import display_information

import AcceptUserNames
import PlayTicTacToe

display_information.diplay_information()
usernames = AcceptUserNames.acceptusernames()

user1 = usernames.split('|')[0]
user2 = usernames.split('|')[1]

print (user1 + '  ' + user2)

starttime = datetime.datetime.now()
print ('Game started by ' + user1 + ' & ' + user2 + ' at ' + str(starttime))

result = PlayTicTacToe.playtictactoe(user1,user2)

if result == '':
    print ('It is a Tie !!')
else:
    print (result)

end_time = datetime.datetime.now()
print ('Game ended at: ' + str(end_time))
total_time = end_time - starttime
print ('The game took ' + str(total_time) + ' of time to complete.')
print ('Thanks for Playing')