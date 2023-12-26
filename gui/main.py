import tkinter as tk
from PIL import Image, ImageTk
import os

# Define the function to display the selected image
def display_image():
    # Get the filename of the selected image
    filename = var.get()
    # Open the image using PIL
    image = Image.open(filename)
    # Resize the image to fit the GUI window
    image = image.resize((400, 400))
    # Convert the image to a format that Tkinter can display
    photo = ImageTk.PhotoImage(image)
    # Set the image in the label
    label.config(image=photo)
    label.image = photo

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("Image Viewer")

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Create a dropdown menu to select the image
var = tk.StringVar(root)
choices = [f for f in os.listdir(".") if f.endswith(".jpg") or f.endswith(".png")]
var.set(choices[0])
dropdown = tk.OptionMenu(root, var, *choices)
dropdown.pack()

# Create a button to display the selected image
button = tk.Button(root, text="Display", command=display_image)
button.pack()

# Run the GUI
root.mainloop()
