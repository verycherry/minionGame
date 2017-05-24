#----------------------------------------------
# Stay Alive!
# More programs at UsingPython.com/programs
#----------------------------------------------

#import the modules we need, for creating a GUI
import tkinter
import random

#only press return once
okToPressReturn = True

#the player's attributes.
hunger = 100
boredom = 10
day = 0

#-------------------------------------------------------------------

def startGame(event):

	global okToPressReturn

	if okToPressReturn == False:
		pass
	
	else:
		#update the time left label.
		startLabel.config(text="")
		#start updating the values
		updateHunger()
		updateDay()
		updateDisplay()

		okToPressReturn = False

#-------------------------------------------------------------------

def updateDisplay():

	#use the globally declared variables above.
	global hunger
	global day

	if hunger <= 50:
		minionPic.config(image = minion1)
	else:
		minionPic.config(image = minion1)

	#update the time left label.
	hungerLabel.config(text="Hunger: " + str(hunger))

	#update the day' label.
	dayLabel.config(text="Day: " + str(day))   

	#update the boredom label.
	boredomLabel.config(text="Boredom: " + str(boredom))   

	#run the function again after 100ms.       
	minionPic.after(100, updateDisplay)

#-------------------------------------------------------------------
 
def updateHunger():

	#use the globally declared variables above.
	global hunger

	#decrement the hunger.
	hunger -= 1

	if isAlive():
		#run the function again after 30s.
		hungerLabel.after(30000, updateHunger)

#-------------------------------------------------------------------

def updateDay():

	#use the globally declared variables above.
	global day

	#increment the day.
	day += 1

	if isAlive():
		#run the function again after 1 hour.
		dayLabel.after(3600000, updateDay)

#-------------------------------------------------------------------

def updateBoredom():

	#use the globally declared variables above.
	global boredom

	#decrement the boredom.
	boredom -= 1

	if isAlive():
		#run the function again after 1 min.
		boredomLabel.after(60000, updateDay)

#-------------------------------------------------------------------

def feed():

	global hunger
	
	if hunger <= 95:
		hunger += 20
	else:
		hunger -=20
		
#-------------------------------------------------------------------

def play():

	global boredom
	
	if boredom <= 9:
		boredom += 1
	else:
		boredom -=1

#-------------------------------------------------------------------

def isAlive():

	global hunger
	
	if hunger <= 0:
		#update the start info label.
		startLabel.config(text="GAME OVER! YOU KILLED HIM/HER/IT!")     
		return False
	else:
		return True
		
#-------------------------------------------------------------------


#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Stay Alive!")
#set the size.
root.geometry("500x500")

#add a label for the start text.
startLabel = tkinter.Label(root, text="Press 'Return' to start!", font=('Helvetica', 12))
startLabel.pack()

#add the labels
hungerLabel = tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica', 12))
hungerLabel.pack()

boredomLabel = tkinter.Label(root, text="Boredom: " + str(boredom), font=('Helvetica', 12))
boredomLabel.pack()

dayLabel = tkinter.Label(root, text="Day: " + str(day), font=('Helvetica', 12))
dayLabel.pack()

# the different minions
minion1 = tkinter.PhotoImage(file="minion1.gif")

#add a minion image
minionPic = tkinter.Label(root, image=minion1)
minionPic.pack()

#add the buttons
btnFeed = tkinter.Button(root, text="Feed Me", command=feed)
btnFeed.pack()
btnPlay = tkinter.Button(root, text="Play With Me", command=play)
btnPlay.pack()

#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)

#start the GUI
root.mainloop()
