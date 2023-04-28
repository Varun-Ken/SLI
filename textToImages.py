import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
import os

# Define the function to play the images
def play_images():
    # Disable the input field and the play button
    input_entry.configure(state=tk.DISABLED)
    play_button.configure(state=tk.DISABLED)

    # Get the sentence from the input field
    sentence = input_entry.get()

    # Split the sentence into words
    words = sentence.split()

    # Define the path to the images directory
    images_dir = ""

    # Define the size of the images
    image_size = (250, 250)

    # Create the frame for the images
    images_frame = tk.Frame(root, bg="#222")
    images_frame.pack(padx=20, pady=15)

    # Define the function to display the next image
    def display_image(i):
        if i < len(words):
            # Get the image path for the word
            image_path = os.path.join(images_dir, words[i] + ".jfif")

            # Load the image and resize it
            try:
                image = Image.open(image_path)
                image = image.resize(image_size, Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
            except:
                # If the image is not found, display a placeholder image
                photo = ImageTk.PhotoImage(Image.new("RGB", image_size, "#333"))

            # Create the label for the image and add it to the frame
            image_label = tk.Label(images_frame, image=photo, bg="#222")
            image_label.photo = photo
            image_label.pack(side=tk.LEFT, padx=10)

            # Start a timer to remove the image after 3 seconds
            threading.Timer(3.0, lambda: image_label.pack_forget()).start()

            # Display the next image after a delay of 3 seconds
            threading.Timer(3.0, lambda: display_image(i+1)).start()
        else:
            # Enable the input field and the play button
            input_entry.configure(state=tk.NORMAL)
            play_button.configure(state=tk.NORMAL)

    # Start the display function with the first image
    display_image(0)

# Create the main window
root = tk.Tk()
root.title("Enter a Sentence")
root.geometry("500x500")
root.configure(bg="#222")

# Create the input field
input_frame = tk.Frame(root, bg="#222")
input_frame.pack(padx=20, pady=50)
input_label = tk.Label(input_frame, text="Enter a sentence:", fg="#fff", bg="#222")
input_label.pack(side=tk.LEFT)
input_entry = tk.Entry(input_frame, width=40, fg="#fff", bg="#333", bd=0, insertbackground="#fff")
input_entry.pack(side=tk.LEFT, padx=10)
input_entry.focus()

# Create the button to play the images
button_frame = tk.Frame(root, bg="#222")
button_frame.pack(padx=20, pady=20)
play_button = tk.Button(button_frame, text="Play Images", bg="#ff9900", fg="#fff", bd=0, command=play_images)
play_button.pack(side=tk.LEFT)
stop_button = tk.Button(button_frame, text="Stop", bg="#ff3b3b", fg="#fff", bd=0, state=tk.DISABLED)
stop_button.pack(side=tk.LEFT, padx=10)

# Start the GUI event loop
root.mainloop()
