import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import csv
import json

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getCSV ():
    global csvfile
    #global read_file
    
    import_file_path = filedialog.askopenfilename()
    csvfile = open(import_file_path, 'r')
    #read_file = pd.read_csv (import_file_path)
    
browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)

def convertToJSON ():
    global csvfile
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.json')
    jsonfile = open(export_file_path, 'w')
    reader = csv.DictReader( csvfile)
    out = json.dumps( [ row for row in reader ] )
    jsonfile.write(out)

saveAsButton_JSON = tk.Button(text='Convert CSV to JSON', command=convertToJSON, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JSON)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
