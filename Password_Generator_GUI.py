import tkinter as tk
import random
import string

def password_generator():
    try :
        length = int(length_input.get())
        chars = ""
        if use_uppercase.get():
            chars +=string.ascii_uppercase
        if use_lowercase.get():
            chars +=string.ascii_lowercase
        if use_digits.get():
            chars +=string.digits
        if use_punctuations.get():
            chars +=string.punctuation
        
        if not chars :
            result_label.config(text="Please select atleast one charcter set!")
            return
        password = "".join(random.choice(chars) for _ in range (length))
        result_label.config(text = password)

    except ValueError:
        result_label.config(text="Please enter a valid number!")




#create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x450")

#create a label
length_entry =tk.Label(root, text="Password Length: ",font=("Arial", 12)).pack(pady=10)

#Input from the user
length_input= tk.Entry(root,font=("Arial", 12))
length_input.pack()

# Add Checkboxes
use_uppercase = tk.BooleanVar(value = True)
use_lowercase = tk.BooleanVar(value = True)
use_digits = tk.BooleanVar(value = True)
use_punctuations = tk.BooleanVar(value = True)

tk.Checkbutton(root, text ="Include Uppercase",variable=use_uppercase).pack()
tk.Checkbutton(root, text ="Include lowercase",variable=use_lowercase).pack()
tk.Checkbutton(root, text ="Include digits",variable=use_digits).pack()
tk.Checkbutton(root, text ="Include symbols",variable=use_punctuations).pack()

#Add a button
button = tk.Button(root, text ="Genearate Password", command = password_generator, bg = "blue", fg="orange",bd = 4).pack(pady =10)

# output
result_label = tk.Label(root,text="",font=("Courier", 14), wraplength=450)
result_label.pack(pady=20)

#start the main loop
root.mainloop()

