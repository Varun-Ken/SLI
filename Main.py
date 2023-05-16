import tkinter as tk
import os

# Create a new tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Sign Language Interpreter")

# Set the background color of the window
window.configure(bg='#222222')

# Set the font style and size of the title label
title_font = ("Consolas", 24, "bold")

# Create a label widget to display the logo image
logo_image = tk.PhotoImage(file="logo.png").subsample(6)
logo_label = tk.Label(window, image=logo_image, bg="#222222")
logo_label.pack(pady=(70,0))

# Create a label widget to display the title
title_label = tk.Label(window, text="Sign Language Interpreter", font=title_font, fg="white", bg="#222222")
title_label.pack(pady=(0,20))

# Function to open dataCollection.py file
def open_sign_to_text():
    os.system("python signToText.py")

# Function to open test.py file
def open_text_to_sign():
    os.system("python textToSign.py")

# Create a button widget to open dataCollection.py file
button1 = tk.Button(window, text="Sign Language to Text", font=("Consolas", 14), fg="white", bg="#0099ff", command=open_sign_to_text)
button1.pack(pady=15)

# Create a button widget to open test.py file
button2 = tk.Button(window, text="Text to Sign Language", font=("Consolas", 14), fg="white", bg="#0099ff", command=open_text_to_sign)
button2.pack(pady=10)

# Set the window size and position
window.geometry("600x450")

# Run the main loop to display the window
window.mainloop()
