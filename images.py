from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.convert('L')

# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))
filtered_img.save("grey.png", 'png')