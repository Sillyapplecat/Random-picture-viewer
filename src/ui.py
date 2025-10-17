import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class RandomPictureViewer:
    def __init__(self, root, initial_folder=None):
        self.root = root
        self.root.title("Random Picture Viewer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        self.folder_path = initial_folder
        self.image_files = []
        self.current_index = 0
        self.image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
        
        # Create UI elements
        self.create_widgets()
        
        # Load initial folder if provided
        if self.folder_path and os.path.exists(self.folder_path):
            self.load_images()
            self.show_random_image()
    
    def create_widgets(self):
        # Top frame for folder selection - fixed height
        top_frame = tk.Frame(self.root, height=40)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        top_frame.pack_propagate(False)
        
        tk.Button(top_frame, text="Select Folder", command=self.select_folder).pack(side=tk.LEFT, padx=5)
        
        self.folder_label = tk.Label(top_frame, text="No folder selected", fg="gray")
        self.folder_label.pack(side=tk.LEFT, padx=5)
        
        # Filename label - fixed height
        filename_frame = tk.Frame(self.root, height=30)
        filename_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 5))
        filename_frame.pack_propagate(False)
        
        self.filename_label = tk.Label(filename_frame, text="", font=("Arial", 10))
        self.filename_label.pack()
        
        # Bottom frame for controls - fixed height
        bottom_frame = tk.Frame(self.root, height=50)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        bottom_frame.pack_propagate(False)
        
        tk.Button(bottom_frame, text="Previous", command=self.previous_image, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text="Random", command=self.show_random_image, width=10, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(bottom_frame, text="Next", command=self.next_image, width=10).pack(side=tk.LEFT, padx=5)
        
        self.counter_label = tk.Label(bottom_frame, text="0 / 0")
        self.counter_label.pack(side=tk.RIGHT, padx=5)
        
        # Image display area - fills remaining space
        self.image_frame = tk.Frame(self.root, bg="black")
        self.image_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.image_label = tk.Label(self.image_frame, bg="black")
        self.image_label.pack(expand=True)
    
    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Image Folder")
        if folder:
            self.folder_path = folder
            self.load_images()
            if self.image_files:
                self.show_random_image()
    
    def load_images(self):
        if not os.path.exists(self.folder_path):
            messagebox.showerror("Error", f"Folder does not exist:\n{self.folder_path}")
            return
        
        self.image_files = [f for f in os.listdir(self.folder_path) 
                           if f.lower().endswith(self.image_extensions)]
        
        if not self.image_files:
            messagebox.showwarning("No Images", "No images found in the selected folder.")
            self.folder_label.config(text="No images in folder")
            return
        
        self.folder_label.config(text=f"{self.folder_path} ({len(self.image_files)} images)")
        self.update_counter()
    
    def show_image(self, index):
        if not self.image_files:
            return
        
        self.current_index = index
        image_path = os.path.join(self.folder_path, self.image_files[self.current_index])
        
        try:
            # Load and resize image to fit window
            img = Image.open(image_path)
            
            # Get frame dimensions
            frame_width = self.image_frame.winfo_width()
            frame_height = self.image_frame.winfo_height()
            
            # Use default size if frame not yet rendered
            if frame_width <= 1:
                frame_width = 760
                frame_height = 450
            
            # Calculate scaling factor to fit image in frame
            img_ratio = img.width / img.height
            frame_ratio = frame_width / frame_height
            
            if img_ratio > frame_ratio:
                new_width = frame_width
                new_height = int(frame_width / img_ratio)
            else:
                new_height = frame_height
                new_width = int(frame_height * img_ratio)
            
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
            self.filename_label.config(text=self.image_files[self.current_index])
            self.update_counter()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")
    
    def show_random_image(self):
        if self.image_files:
            random_index = random.randint(0, len(self.image_files) - 1)
            self.show_image(random_index)
    
    def next_image(self):
        if self.image_files:
            next_index = (self.current_index + 1) % len(self.image_files)
            self.show_image(next_index)
    
    def previous_image(self):
        if self.image_files:
            prev_index = (self.current_index - 1) % len(self.image_files)
            self.show_image(prev_index)
    
    def update_counter(self):
        if self.image_files:
            self.counter_label.config(text=f"{self.current_index + 1} / {len(self.image_files)}")
        else:
            self.counter_label.config(text="0 / 0")

def main(initial_folder=None):
    root = tk.Tk()
    app = RandomPictureViewer(root, initial_folder)
    root.mainloop()

if __name__ == "__main__":
    main()
