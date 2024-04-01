import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()

window.title("Widgets Practice I guess")

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)

frame1.pack(pady=10)
frame2.pack(pady=10)

label_frame1 = tk.Label(frame1, text="ANYTHING")
button_frame1 = tk.Button(frame1, text="Do NOT Click Me")
entry_frame1 = tk.Entry(frame1)

label_frame1.pack()
button_frame1.pack()
entry_frame1.pack()

label_frame2 = tk.Label(frame2, text="Please type literally anything")
text_frame2 = tk.Text(frame2, height=5, width=30)

label_frame2.pack()
text_frame2.pack()

window.mainloop()

