#pip install tkinter
#run the code either from terminal or IDLE 

import Tkinter as tk

root = tk.Tk()
root.title('Simple Program')

input_label = tk.Label(root, text="Enter the text")
input_label.pack()

text_box = tk.Entry(root)
text_box.pack()
text_box.focus_set()
 
root.mainloop()
