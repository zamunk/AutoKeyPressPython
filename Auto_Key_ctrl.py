# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:58:38 2019

@author: ZAMunk1
"""

from pynput.keyboard import Key, Controller 
import time
import tkinter as tk
    
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.run_key_ctrl = tk.Button(self)
        self.run_key_ctrl["text"] = "Run Auto Key 'ctrl'"
        self.run_key_ctrl["command"] = self.key_ctrl
        self.run_key_ctrl.pack(side="top")
        
        self.infolabel = tk.Label(self)
        self.infolabel.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def key_ctrl(self):
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        keyboard.release(Key.ctrl)
        self.infolabel["text"] = time.ctime()
        self.delay()
        
    def delay(self):
        self.master.after(60000,self.key_ctrl)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
