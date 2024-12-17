from PIL import Image
from tkinter import Tk, filedialog

def images_to_pdf():
    root = Tk()
    root.withdraw()

    try:
        image_files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
        )

        if not image_files:
            print("No images selected.")
            return

        output_pdf = filedialog.asksaveasfilename(
            title="Save PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not output_pdf:
            print("No output file name provided.")
            return

        images = [Image.open(image).convert('RGB') for image in image_files]
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF created successfully: {output_pdf}")

    except Exception as e:
        print(f"An error occurred: {e}")

images_to_pdf()
