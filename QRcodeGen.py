import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import qrcode
import re
import os
import sys

# Global variables for images to prevent garbage collection
bg_photo = None
background_label = None
generated_qr_image = None
bg_image = None

def resize_bg_image(event):
    global bg_photo, background_label, bg_image
    
    if bg_image is None:
        return

    # Get the updated window size
    window_width = event.width
    window_height = event.height

    # Calculate the aspect ratio of the image
    image_width, image_height = bg_image.size
    aspect_ratio = image_width / image_height

    # Calculate the new size of the image while maintaining aspect ratio
    if (window_width / window_height) > aspect_ratio:
        new_width = window_width
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = window_height
        new_width = int(new_height * aspect_ratio)

    # Resize the image
    try:
        # Use Image.Resampling.LANCZOS for newer Pillow versions
        resampling = getattr(Image, 'Resampling', Image).LANCZOS if hasattr(Image, 'Resampling') else Image.ANTIALIAS
        resized_bg = bg_image.resize((new_width, new_height), resampling)
        bg_photo = ImageTk.PhotoImage(resized_bg)

        # Update the image on the background label
        background_label.configure(image=bg_photo)
    except Exception as e:
        print(f"Error resizing background: {e}")

def generate_qr():
    """Generates QR code based on user input and displays it."""
    global generated_qr_image
    
    name = name_entry.get().strip()
    student_id = student_id_entry.get().strip()
    phone = phone_entry.get().strip()
    email_id = email_id_entry.get().strip()
    location = location_entry.get().strip()
    branch = branch_entry.get().strip()
    message = message_entry.get().strip()

    # Basic data validation (check if all required fields are filled)
    if not all([name, student_id, email_id, phone]):
        messagebox.showerror("Error", "Please fill in all required fields (Name, Student ID, Email, Phone)")
        return

    if not re.match(r'^[a-zA-Z\s]+$', name):
        messagebox.showerror("Error", "Please enter a valid name (letters and spaces only)!")
        return

    # Validate phone number format
    phone_pattern = re.compile(r'^[0-9]\d{9}$') # Indian phone number format
    if not phone_pattern.match(phone):
        messagebox.showerror("Error", "Please enter a valid 10-digit phone number!")
        return

    # Validate email ID format
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not email_pattern.match(email_id):
        messagebox.showerror("Error", "Please enter a valid email address!")
        return

    # Concatenate information
    data = f"Name: {name}\nStudent ID: {student_id}\nPhone: {phone}\nEmail: {email_id}\nLocation: {location}\nBranch: {branch}\nMessage: {message}"
    
    try:
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=qr_size.get(), border=5)
        qr.add_data(data)
        qr.make(fit=True)

        # Generate QR code image
        img = qr.make_image(fill_color="red", back_color="white").convert('RGB')

        # Get the path to the directory containing the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'vishal.png')

        # Load and paste logo if it exists
        if os.path.exists(file_path):
            logo = Image.open(file_path)
            # Adjust size as needed (keep it reasonably small)
            qr_w, qr_h = img.size
            logo_size = int(qr_w * 0.2) 
            resampling = getattr(Image, 'Resampling', Image).LANCZOS if hasattr(Image, 'Resampling') else Image.ANTIALIAS
            logo = logo.resize((logo_size, logo_size), resampling)
            
            # Position the logo in the center
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            img.paste(logo, pos)

        # Convert QR code to a tkinter image
        qr_image = ImageTk.PhotoImage(img)
        qr_label.config(image=qr_image)
        qr_label.image = qr_image # Keep a reference to avoid garbage collection
        
        # Store the generated QR image
        generated_qr_image = img
        messagebox.showinfo("Success", "QR Code generated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code: {e}")

def save_qr():
    """Saves the generated QR code image to a chosen file."""
    if generated_qr_image is None:
        messagebox.showerror("Error", "Please generate a QR code first!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                           filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        generated_qr_image.save(file_path)
        messagebox.showinfo("Success", f"QR code saved successfully at:\n{file_path}")

def clear_all():
    """Clears all entry fields."""
    name_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_id_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    qr_label.config(image="") 
    qr_label.image = None
    global generated_qr_image
    generated_qr_image = None

# Create the main window
root = tk.Tk()
root.title("Premium QR Code Generator")
root.geometry("800x600")

# Load the background image
script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, "backg.jpg")

if os.path.exists(bg_path):
    bg_image = Image.open(bg_path)
    bg_photo = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(root, image=bg_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.bind("<Configure>", resize_bg_image)
else:
    # Fallback background
    root.configure(bg="#2c3e50")
    background_label = tk.Label(root, bg="#2c3e50")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# UI Styling
label_style = {"bg": "white", "fg": "#333", "font": ("Arial", 10, "bold")}
entry_style = {"font": ("Arial", 10)}

# Labels and Entry Fields
fields = [
    ("Name:", 50),
    ("Student ID:", 80),
    ("Phone:", 110),
    ("Email ID:", 140),
    ("Location:", 170),
    ("Branch:", 200),
    ("Message:", 230)
]

entries = {}
for text, y in fields:
    lbl = tk.Label(root, text=text, **label_style)
    lbl.place(x=50, y=y)
    
    ent = tk.Entry(root, **entry_style)
    ent.place(x=150, y=y, width=200)
    entries[text] = ent

name_entry = entries["Name:"]
student_id_entry = entries["Student ID:"]
phone_entry = entries["Phone:"]
email_id_entry = entries["Email ID:"]
location_entry = entries["Location:"]
branch_entry = entries["Branch:"]
message_entry = entries["Message:"]

# QR Code Size Option
qr_size = tk.IntVar(value=10) # Default size
size_label = tk.Label(root, text="QR Code Size:", **label_style)
size_label.place(x=50, y=270)

size_radio_small = tk.Radiobutton(root, text="Small", variable=qr_size, value=5, bg="white")
size_radio_small.place(x=150, y=270)

size_radio_medium = tk.Radiobutton(root, text="Medium", variable=qr_size, value=10, bg="white")
size_radio_medium.place(x=250, y=270)

size_radio_large = tk.Radiobutton(root, text="Large", variable=qr_size, value=15, bg="white")
size_radio_large.place(x=360, y=270)

# Buttons
btn_style = {"font": ("Arial", 10, "bold"), "cursor": "hand2", "width": 15}

generate_button = tk.Button(root, text="Generate QR", command=generate_qr, bg="#27ae60", fg="white", **btn_style)
generate_button.place(x=150, y=320)

save_button = tk.Button(root, text="Save QR", command=save_qr, bg="#2980b9", fg="white", **btn_style)
save_button.place(x=150, y=360)

clear_button = tk.Button(root, text="Clear All", command=clear_all, bg="#e74c3c", fg="white", **btn_style)
clear_button.place(x=150, y=400)

# QR code display frame/label
qr_display_frame = tk.Label(root, text="QR Code Preview", bg="white", relief="sunken", bd=2)
qr_display_frame.place(x=450, y=50, width=300, height=300)

qr_label = tk.Label(qr_display_frame, bg="white")
qr_label.pack(expand=True, fill="both")

# Run the Tkinter event loop
root.mainloop()
