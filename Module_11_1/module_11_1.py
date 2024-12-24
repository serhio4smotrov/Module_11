import random
from PIL import Image
import numpy as np


with Image.open('example.jpg') as im:
    im = im.rotate(18).resize((400,450)).convert('L')
    im.save('example.jpg')
    im.save('example.png')


massiv = np.array([[1,2,3],[4,5,6]],int)
print(massiv[1,2])
print(massiv.shape)
rand = random.randint(0,10)
f = True if rand in massiv else False
print(rand)
print(f)
zero_massiv = np.zeros(7,int)
print(zero_massiv)
rand_massiv = np.random.randint(0,10,3)
rand_massiv1 = np.random.randint(0,10,3)
print(rand_massiv)
print(rand_massiv1)
print(rand_massiv1+rand_massiv)