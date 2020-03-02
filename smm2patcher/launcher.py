import os, tkinter
from tkinter import filedialog

home = os.path.expanduser('~')
root = tkinter.Tk()
root.withdraw()
print('Select A Super Mario Maker 2 Binary File.')
binary_path = filedialog.askopenfilename(initialdir = home + "/Desktop",title = "Select A Super Mario Maker 2 Binary File",filetypes = ([("All Files","*.*")]))
os.system('nsnsotool.exe ' + binary_path + ' ' + binary_path + '_uncompressed')
os.system('py -i smm2patcher.py ' + binary_path)
os.system('nsnsotool.exe ' + binary_path + '_uncompressed ' + binary_path)
os.remove(binary_path + '_uncompressed')