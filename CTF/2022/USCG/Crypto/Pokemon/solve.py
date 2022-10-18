from PIL import Image

img = Image.open('ciphertext.png')

width, height = img.width/88, img.height/128

alphabet = list('abcdefghijklmnopqrstuvwxyz')
hashes = {}

def hash_img(img):
    return hash(tuple(img.getdata()))

text = ''
for y in range(128):
    for x in range(88):
        cropped = img.crop((x*width,y*height,(x+1)*width,(y+1)*height))

        if hash_img(cropped) not in hashes:
            hashes[hash_img(cropped)] = alphabet.pop()

        text += hashes[hash_img(cropped)]

print(text)

