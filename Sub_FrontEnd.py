from tkinter import *

def NewFile():
    print("New File!")
def OpenFile():
    name = filedialog.askopenfilename()
    print (name)
def About():
    print ("Simple menu example.")
def TBC():
    print ("Menu coming soon...")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu = filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

Subsmenu = Menu(menu)
menu.add_cascade(label="Submissions", menu = Subsmenu)
Subsmenu.add_command(label="Add New", command=TBC)
Subsmenu.add_command(label="Amend Existing", command=TBC)

Extmenu = Menu(menu)
menu.add_cascade(label="Extensions", menu = Extmenu)
Extmenu.add_command(label="Add Extension", command=TBC)
Extmenu.add_command(label="Amend Existing", command=TBC)

Reportsmenu = Menu(menu)
menu.add_cascade(label="Reports", menu = Reportsmenu)
Reportsmenu.add_command(label="View Submission Dates", command=TBC)
Reportsmenu.add_command(label="View Submission Results", command=TBC)
Reportsmenu.add_command(label="View Non-Submission List", command=TBC)
Reportsmenu.add_command(label="View Summaries", command=TBC)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
