# Images to PDF Converter

This project is a Python-based application that converts multiple images into a single PDF file. It uses the **Tkinter** library for graphical user interface components and **Pillow (PIL)** for image manipulation.

## Features
- Select multiple images from your computer.
- Rearrange the selected images in the desired order.
- Save the selected images as a PDF file.
- Supports common image formats like PNG, JPG, JPEG, BMP, and TIFF.

## Requirements
- Python 3.6 or later
- Required Python libraries:
  - `Pillow`
  - `tkinter` (usually included with Python)

## Installation

1. Clone this repository or download the script directly:
   ```bash
   git clone https://github.com/your-repository/images-to-pdf
   cd images-to-pdf
   ```
2. Install the required libraries using pip:
   ```bash
   pip install Pillow
   pip install python-tk
   ```
3. Run the script:
   ```bash
   python images_to_pdf.py
   ```

## How to Use
- When you run the script, a file dialog will appear.
- Select the images you want to convert to a PDF. You can select multiple images at once.
- Specify the name and location for the output PDF file in the next dialog.
- The application will convert the images into a PDF in the order you selected them.
- A message will appear indicating success or failure.

## Supported Image Formats
- PNG
- JPG / JPEG
- BMP
- TIFF

## Example Output
If you select images named image1.png, image2.jpg, and image3.bmp, and save the PDF as output.pdf, the script will create a PDF named output.pdf containing these images in the specified order.

## Troubleshooting
### Common Issues
1. No Images Selected: If you do not select any images, the program will exit without creating a PDF.
2. Output File Name Not Provided: If you cancel the dialog to save the PDF, the program will not proceed.
3. File Dialog Error: If you encounter issues on macOS with file dialogs, ensure you are using the latest version of Python and Tkinter.

### Debugging Steps
1. Ensure all required libraries are installed.
2. Run the script from the terminal to view error messages.
3. Update Python and libraries to the latest versions.
   
## Contribution
Feel free to contribute to this project by submitting issues or pull requests. If you encounter any bugs or have feature requests, please let us know.

## Author
Aman Derwal
