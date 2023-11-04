import tkinter as tk
import time
import math
t=time.localtime()
m=('0','January','February','March','April','May','June','July','August','September','October','November','December')
r=m[t.tm_mon]

# Create a function to update the clock hands
def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour  

    # Calculate angles for the clock hands
    sec_angle = math.radians(90 - seconds * 6)
    min_angle = math.radians(90 - (minutes + seconds / 60) * 6)
    hour_angle = math.radians(90 - (hours + minutes / 60) * 15)

    # Update the clock hands
    canvas.delete("hands")
    canvas.create_line(350, 380, 350 + 140* math.cos(hour_angle), 380 - 140* math.sin(hour_angle), width=3, fill="white", tags="hands")
    canvas.create_line(350, 380, 350 + 200* math.cos(min_angle), 380 - 200* math.sin(min_angle), width=3, fill="white", tags="hands")
    canvas.create_line(350, 380, 350 + 290* math.cos(sec_angle), 380 - 290* math.sin(sec_angle), width=2, fill="red", tags="hands")
    canvas.create_text(280,800,text=r,font=("Times new roman", 9),fill='white',tags='hands')

    # Update the clock every 1000ms (1 second)
    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Analog Clock")

# Create a canvas for the clock face
canvas = tk.Canvas(root, width=800, height=1750, bg="black")
canvas.pack()

# Create the clock face
#canvas.create_oval(0, 0, 700, 700, width=5,fill='black')
#canvas.create_oval(350-250, 350+250, 350+250, 350-250, fill= 'white')
canvas.create_oval(350-170, 380+170,350+170,380-170, fill= 'grey')
canvas.create_oval(345, 375, 355, 385, fill="black")

for i in range(0,60):
	angle=math.radians(90-i*6)
	x=350+295*math.cos(angle)
	y=380-295*math.sin(angle)
	canvas.create_text(x,y,text='•',font=("arial",4),fill='white')
for i in range(0,60,5):
	angle=math.radians(90-i*6)
	x=350+235*math.cos(angle)
	y=380-235*math.sin(angle)
	canvas.create_text(x,y,text=str(i),font=("arial",8),fill='white')
for i in range(0,60):
	angle=math.radians(90-i*6)
	x=350+210*math.cos(angle)
	y=380-210*math.sin(angle)
	canvas.create_text(x,y,text='•',font=("arial",4),fill='white')
for i in range(0,24):
	angle=math.radians(90-i*15)
	x=350+150*math.cos(angle)
	y=380-150*math.sin(angle)
	canvas.create_text(x,y,text=str(i),font=("arial",5),fill='white')
for i in range(0,60):
	angle=math.radians(90-i*6)
	x=350+320*math.cos(angle)
	y=380-320*math.sin(angle)
	canvas.create_text(x,y,text=str(i),font=("arial",5),fill='white')
canvas.create_text(390,800,text=t.tm_mday,font=("arial",9),fill='white')
canvas.create_text(350,350,text='24 Hr',font=("arial",15),fill='black')
canvas.create_text(470,800,text=t.tm_year,font=("arial",9),fill='white')
canvas.create_text(350,430,text='R.P Clocks',font=("arial",7),fill='black')

# Start the clock update loop
update_clock()

root.mainloop()
