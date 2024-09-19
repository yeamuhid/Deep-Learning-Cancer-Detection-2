pip install pillow

from PIL import Image, ImageFilter
# Open an image file
img = Image.open ("example.jpg" )
# Display the original image
img. show()
# Resize the image
img_ resized - img-resize((300, 300))
img_ resized. show()
# Rotate the image
img_rotated = img-rotate (45)
img_rotated. show()
# Apply a filter (BLUR)
img blurred = img-filter (ImageFilter.BLUR)
img blurred.show()
# Convert image to grayscale
img_gray = img-convert("L")
img_gray.show()
# Save the modified image
img resized. save ("resized
example. jpg")
img_ rotated. save("rotated _example.jpg")
ing blurred. save("blurred _example.jpg")
img gray. save ("gray_example.jpg")