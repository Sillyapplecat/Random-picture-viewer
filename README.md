# Random Picture Viewer

## Overview
The Random Picture Viewer is a simple Python script that randomly selects an image from a specified folder and opens it using the default image viewer on your system. This project is designed for those who want a fun way to view random pictures.

## Features
- Randomly selects an image from a designated folder.
- Opens the selected image using the system's default image viewer.
- Supports common image formats: JPG, JPEG, PNG, and GIF.
- Error logging for troubleshooting.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd random-picture-viewer
   ```

2. **Install Python**:
   Ensure you have Python 3.6 or higher installed on your system.

3. **Prepare your images**:
   - Create a folder named `Cats` on your desktop at: `C:\Users\kasutaja\Desktop\Cats`
   - Add your favorite images in JPG, JPEG, PNG, or GIF format to this folder.
   - **Note**: You can change the folder path by editing line 8 in `src/randompicture.py`

## Usage
### Option 1: Using the batch file (Windows)
Double-click `startup.bat` to run the script.

### Option 2: Using command line
1. Open a terminal or command prompt.
2. Navigate to the `src` directory:
   ```
   cd src
   ```
3. Run the script:
   ```
   python randompicture.py
   ```

The script will randomly select an image from the folder and open it in your default image viewer.

## Troubleshooting
- If you see "Folder does not exist", make sure you created the `Cats` folder at the correct location.
- Check `src/error.log` for detailed error messages.

## License
This project is open-source and available for anyone to use and modify. Enjoy your random pictures!