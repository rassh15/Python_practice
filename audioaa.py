'''from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("C:\\Users\\Ars\\Documents\\python\\Git\\Python Practice\\07_Exercise_Data\\water.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:
	
	print("Press 'p' to pause, 'r' to resume")
	print("Press 'e' to exit the program")
	query = input(" ")
	
	if query == 'p':

		# Pausing the music
		mixer.music.pause()	
	elif query == 'r':

		# Resuming the music
		mixer.music.unpause()
	elif query == 'e':

		# Stop the mixer
		mixer.music.stop()
		break
'''

import collections

dd = collections.defaultdict(list)


print(dd)

dd['a'].append(3)
dd['a'].append(4)
dd['a'].append(6)
dd['c'].append(3)
dd['b'].append(3)




# print('yes') if i == 'e' i for i in dd.keys()