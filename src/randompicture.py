# File: /random-picture-viewer/random-picture-viewer/src/randompicture.py

import os
import random
import subprocess
import sys
import time

# Path to the folder containing cat pictures
cat_folder = r"C:\Users\kasutaja\Desktop\Cats"

try:
    # Check if folder exists
    if not os.path.exists(cat_folder):
        print(f"Error: Folder '{cat_folder}' does not exist.")
        print("Please create the folder and add some images.")
        sys.exit(1)
    
    # Get list of image files (jpg, png, jpeg, gif)
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    cat_images = [f for f in os.listdir(cat_folder) if f.lower().endswith(image_extensions)]

    if not cat_images:
        print(f"No images found in '{cat_folder}'.")
        print("Please add some JPG, PNG, or GIF images to the folder.")
        sys.exit(1)

    # Pick a random image
    random_image = random.choice(cat_images)
    image_path = os.path.join(cat_folder, random_image)

    # Open the image with the default viewer
    subprocess.run(['start', '', image_path], shell=True)
    
except Exception as e:
    # Log errors to a file for debugging
    error_log = os.path.join(os.path.dirname(__file__), 'error.log')
    with open(error_log, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Error: {str(e)}\n")
    print(f"An error occurred. Check {error_log} for details.")
    sys.exit(1)