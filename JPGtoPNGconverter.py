import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists; if not, create it
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

for filename in os.listdir(image_folder):
  if filename != '.DS_Store':
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
# loop through Pokedex

# convert images to png

# save to the new folder