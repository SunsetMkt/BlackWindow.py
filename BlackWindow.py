# A fullscreen black window.
# Close on click.
import tkinter
root = tkinter.Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Button-1>", lambda event: root.destroy())
root.mainloop()
