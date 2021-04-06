#!/usr/bin/env python
# coding: utf-8

# In[36]:



"""
Timer GUI application using tkinter.

Author: Jui Mistry
updated: 04/04/2021
"""

# Third-party imports

import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):
        
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):
        """The interface function."""
        
        self.time_entry = tk.Entry(self,fg='white',bg='grey')
        self.time_entry.grid(row=0, column=1)

        self.clock = tk.Label(self, text="00:00:00", font=("Arial", 35),fg='light green',bg='black',width=15)
        self.clock.grid(row=1, column=1, stick="N")

        self.time_label = tk.Label(self, text="hour min sec", font=("Arial",35),fg='light green',bg='black', width=15)
        self.time_label.grid(row=2, column=1, sticky="N")

        self.power_button = tk.Button(self, text="Start",font=("Arial", 10,'bold'),fg='light green',bg='green', command=lambda: self.start())
        self.power_button.grid(row=3, column=0, sticky="NE")

        self.reset_button = tk.Button(self, text="Reset", font=("Arial", 10,'bold'),fg='light green',bg='black',command=lambda: self.reset())
        self.reset_button.grid(row=3, column=1, sticky="NE")

        self.quit_button = tk.Button(self, text="Quit", font=("Arial", 10,'bold'),fg='light green',bg='red',command=lambda: self.quit())
        self.quit_button.grid(row=3, column=3, sticky="NE")

        self.master.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
        """Calculates the time"""
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):
        """Checks if valid time entered and updates the timer"""
        
        self.time = int(self.time_entry.get())
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")
            
   

    def timer(self):
        """Calculates the time to be displayed"""
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Time's up!")
            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        """Begins the timer"""
        try:
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.power_button.configure(text="Stop",bg='green',command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        """Stops the timer"""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 0."""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"

    def quit(self):
        """Ask user if they want to close program."""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()



if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Timer')
    
    root.configure(bg="black")
    Application(root).pack(side="top", fill="x", expand=True)
    root.geometry('500x200')
    root.resizable(0,0)
    root.mainloop()


# ## 

# In[ ]:




