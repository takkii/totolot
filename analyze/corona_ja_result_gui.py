import tkinter as tk

root = tk.Tk()
root.title("Coronavirus Tracker")
root.geometry("1063x464")
corosuke = tk.PhotoImage(file="../images/corona_image.gif")
canvas = tk.Canvas(bg="black", width=1063, height=464)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=corosuke, anchor=tk.NW)
root.mainloop()
