import os, tkinter
from tkinter import filedialog

home = os.path.expanduser('~')
root = tkinter.Tk()
root.withdraw()
print('Select A Super Mario Maker 2 Binary File.')
binary_path = filedialog.askopenfilename(initialdir = home + "/Desktop",title = "Select A Super Mario Maker 2 Binary File",filetypes = ([("All Files","*.*")]))
game_version = input('Please Enter A Supported Game Version: ')
os.system('py -i smm2patcher.py ' + binary_path + ' ' + game_version)
