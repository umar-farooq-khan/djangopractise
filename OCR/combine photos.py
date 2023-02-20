from PIL import Image
import glob
# iOpen the four images
import glob
from PIL import Image, ImageDraw, ImageFont


# Get a list of all image files in the directory
image_files = glob.glob(r"C:\Users\umaRf\OneDrive\Desktop\Transfer\shani bhai 4 pics\*.jpeg")
print(image_files)
# Define the number of images to use for the collage
num_images = 4

# Open the first four images
images = []
for i in range(num_images):
    images.append(Image.open(image_files[i]))

# Resize the images
for i in range(num_images):
    images[i] = images[i].resize((500, 500))

# Create a new image with the dimensions of two images side by side
collage_width = 2 * images[0].width
collage_height = 2 * images[0].height
collage = Image.new("RGB", (collage_width, collage_height))

# Paste the images onto the collage
collage.paste(images[0], (0, 0))
collage.paste(images[1], (images[0].width, 0))
collage.paste(images[2], (0, images[0].height))
collage.paste(images[3], (images[0].width, images[0].height))

# Resize the collage
collage = collage.resize((1000, 1000))
# Add a description to the image
draw = ImageDraw.Draw(collage)
font = ImageFont.truetype("calibri.ttf", 30)
description = "Shani sb. reciting Naat at Azerbaijaan"
text_width, text_height = draw.textsize(description, font)
x = (collage.width - text_width) // 2
y = collage.height - text_height - 10
draw.text((x, y), description, fill=(255, 255, 255), font=font)

# Save the collage as a JPEG image
collage.save("output.jpg")

