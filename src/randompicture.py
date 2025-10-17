# File: /random-picture-viewer/random-picture-viewer/src/randompicture.py

import os
import sys
from ui import main as ui_main

# Path to the folder containing cat pictures
cat_folder = r"C:\Users\kasutaja\Desktop\Cats"

try:
    # Launch the UI with the default folder
    ui_main(initial_folder=cat_folder)
    
except Exception as e:
    # Log errors to a file for debugging
    import time
    error_log = os.path.join(os.path.dirname(__file__), 'error.log')
    with open(error_log, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Error: {str(e)}\n")
    print(f"An error occurred. Check {error_log} for details.")
    sys.exit(1)