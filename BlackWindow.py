# A fullscreen black window.
# Close on click. Hide cursor.
import tkinter
root = tkinter.Tk()
# Make the window fullscreen.
root.attributes("-fullscreen", True)
# Make the window black.
root.configure(background='black')
# Close the window on click.
root.bind("<Button-1>", lambda event: root.destroy())
# Hide cursor.
root.config(cursor="none")
# Start the window.
root.mainloop()
