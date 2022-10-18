# Who's That Pokemon

Author: BenderBot

## Description

We've intercepted an encrypted message, can you decrypt it? Flag Submission format: uscg{[a-z]+}

Some forms seem to appear more often than others.

## Solution

The pokemon depectied in the image is unown. The different forms represent different letters. It can be assummed that this is either in plaintext or a substitution cipher because unown can only represent characters from a-z. This means that the real value of each form doesn't matter as long as all of the same form are mapped to the same letter.

To accomplish this task, each unown can be cropped individually and the cropped images can then be hashed to map matching unown to the same letter. The python script below uses PILLOW to crop the images.

```python
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
```

This will print the equivalent of a substitution cipher and can be deciphered accordingly. The flag is at the end of the resulting cleartext data.

