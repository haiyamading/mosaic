import os
import Image
import ImageFont
import ImageDraw


img_list   = []
img_text   = []
img_path   = "./data/"
width      = 176 #684
height     = 187 #1024
text_pos_x = 3   #10
text_pos_y = 3   #10
text_size  = 10  #50
rows       = 2
columns    = 0


for file in os.listdir( img_path ):
    # Search images
    if file.endswith(".jpg"):
        # open images
        img_list.append( Image.open( img_path + file ) )
        # Extract text to render on the image from the file name
        img_text.append( file.split("-")[1].split(".")[0] )
        # Print info
        print 'File:', file, ' => ', img_text[-1]


for image in img_list:
    # resize images
    image.thumbnail( (width, height) )

columns = len(img_list)/rows

#creates a new empty image, RGB mode
mosaic = Image.new( 'RGB', (  columns * width, rows * height ) )

# Prepare draw and font objects to render text
draw   = ImageDraw.Draw(mosaic)
font   = ImageFont.truetype("C:/Windows/Fonts/arial.ttf",text_size)

k=0
for j in xrange( 0, rows * height, height ):
    for i in xrange( 0, columns * width, width ):
        # paste the image at location i,j:
        mosaic.paste( img_list[k], (i,j) )
        # render text at location i,j:
        draw.text((i + text_pos_x, j + text_pos_y), img_text[k], font=font)
        # Select next image and text
        k = k + 1

# Save image to file
mosaic.save('mosaic.jpg')
