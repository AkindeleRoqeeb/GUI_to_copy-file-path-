import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():
    filename = filedialog.askopenfilenames(initialdir="/", title="Select File",
                                           filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)


canvas = tk.Canvas(root, height=620, width=670, bg="#263D42")
canvas.pack()

frame = tk.Canvas(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(
    root, text="Open File", padx=10,
    pady=5, fg="white", bg="#263D42", command=addApp
)
openFile.pack()

runApps = tk.Button(
    root, text="Run Apps", padx=10,
    pady=5, fg="white", bg="#263D42", command=addApp
)
runApps.pack()

root.mainloop()