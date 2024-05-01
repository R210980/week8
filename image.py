from PIL import image
image_path=''
image=image.open('/home/rguktrkvalley/Downloads/cross.jpg')
x,y=100,100
rgb=image.getpixel((x,y))
print(f'RGB values at position ({x},{y}): {rgb}')
new_rgb=(255,0,0)
image.putpixel((x,y),new_rgb)
output_path='/home/rguktrkvalley/Downloads/cross.jpg'
image.save(output_path)
image.close()
