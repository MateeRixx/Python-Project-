#for this we need to time moduel and tkiner module 


from tkinter import Tk
from tkinter import Label
import time

#tk is use for making window 
#label is use to write text in the windows 
#here root stoes the window title 
root =Tk()
#text that will apear on the top of the window 

root.title("Digital Clock")

# a function is need is needed to display font and time 
#strf gives times and can display in 24 and 12 hour time 
# %I --- hours and M -- mintues S-- seconds and %p for showing am or pm 

def display_time():
    display=time.strftime("%I:%M:%S %p")
    #config is telling what we need to write to the function of digital_clock 
    digital_clock.config(text=display)
    #here 200 slow that after every 200ms my present time function will run and show us time 
    digital_clock.after(200,display_time)



#makign a label 

digital_clock=Label(root,font=("Courier New",120),bg="#FCC014",fg="#212121")
#jo kuch bhi ligh rahe ho wo kitne space main aayega basically dimension ki baath ho rahi hai 

digital_clock.pack()

display_time()

#after writing whole code need to mention this line for displaying the output

root.mainloop()




