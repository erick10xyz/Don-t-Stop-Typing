from tkinter import *

delay = 5000
after_id = None

# If user stop typing within 5 secs, it delete all the user typed.
def not_typing(event=None):
   global after_id
   if not event:
      text.delete("1.0", "end")
   else:

      if after_id:
         window.after_cancel(after_id)
      after_id = window.after(delay, not_typing)

# Restart the program
def refresh():
   text.delete("1.0", "end")

#  User Interface
window = Tk()
window.title("Don't Stop Typing!")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg="yellow")

label = Label(text="Don't stop writing, it will disappear!", fg="red", bg="yellow", font=('Romans', 30))
label.grid(column=1, row=0)


text = Text(height=25, width=50, bg='skyblue', fg="white", font=('Arial', 15))
text.bind("<Key>", not_typing)
text.place(x=0, y=0)
text.focus()
text.grid(column=1, row=1)


button = Button(window, text='Refresh', highlightthickness=0, bg='white', fg='green', font=('Arial', 15), command=refresh)
button.grid(column=1, row=3)


window.mainloop()