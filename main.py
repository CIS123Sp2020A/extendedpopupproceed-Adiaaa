#Adia Haynes 
import tkinter
import tkinter.messagebox as box 
#The first step after imports is create a window
window = Tk()
#This shows up at the top of the frame
window.title("Message Box Eample")


def dialog():
    var = box.askyesno("Message Box", "Proceed?")
    if var == 1:
        box.showinfo("Yes Box", "Proceeding...")
    else:
        box.showwarning("No Box", "Cancelling...")


#creating a button:
btn = Button(window, text = 'Click', command=dialog)
#i have to pack the button

btn.pack(padx=150, pady=50)
#start the action to keep it gooing
window.mainloop() 
