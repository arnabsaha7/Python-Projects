import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, UnidentifiedImageError

# Initialize main application window
root = tk.Tk()
root.title("PNG to JPG Converter")  # Set window title
root.geometry("400x300")  # Set fixed window size
root.configure(bg='#f0f0f0')  # Set a light neutral background

# Create a frame for content
frame = tk.Frame(root, bg='#ffffff', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window

# Title label
label1 = tk.Label(frame, text="Image Converter", bg='#ffffff', fg='#333333', font=('Helvetica', 20, 'bold'))
label1.pack(pady=10)

# Function to get and load a PNG file
def getPNG():
    global im1
    try:
        # Open file dialog to select the PNG file
        import_file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if not import_file_path:
            return  # If no file is selected, exit the function

        # Open the selected image file using PIL
        im1 = Image.open(import_file_path)

        # Check if the image is indeed in PNG format
        if im1.format != 'PNG':
            raise ValueError("Selected file is not a valid PNG image.")

        # Confirmation message
        messagebox.showinfo("File Selected", "PNG file loaded successfully!")
    
    except (FileNotFoundError, ValueError, UnidentifiedImageError) as e:
        messagebox.showerror("Error", f"Failed to load image: {str(e)}")

# Button to select PNG file
browse_png = tk.Button(frame, text="Select PNG file", command=getPNG, bg="#3498db", fg='white', 
                       font=('Helvetica', 12, 'bold'), padx=10, pady=5, bd=0)
browse_png.pack(pady=10, fill='x')

# Function to convert the PNG to JPG and save it
def convert():
    try:
        # Ensure the image is loaded first
        if im1 is None:
            messagebox.showerror("Error", "No PNG file loaded.")
            return
        
        # Open save dialog to specify the output file
        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])
        if not export_file_path:
            return  # If no save path is selected, exit the function

        # Convert and save the image as JPG
        rgb_im = im1.convert('RGB')  # Convert PNG (which may have transparency) to RGB before saving as JPG
        rgb_im.save(export_file_path)

        # Success message
        messagebox.showinfo("Success", "Image successfully converted to JPG!")
    
    except NameError:
        messagebox.showerror("Error", "Please load a PNG file before converting.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {str(e)}")

# Button to convert PNG to JPG
saveasbutton = tk.Button(frame, text="Convert PNG to JPG", command=convert, bg="#2ecc71", fg='white', 
                         font=('Helvetica', 12, 'bold'), padx=10, pady=5, bd=0)
saveasbutton.pack(pady=10, fill='x')

# Start the GUI event loop
root.mainloop()
