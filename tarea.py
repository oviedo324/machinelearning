'''importar libreria scipy y matplotlib '''
from scipy import ndimage
import matplotlib.pyplot as plt

'''np no existia, por eso no funcionaba'''
import numpy as np

'''Le damos el tamaño que van a tener las imagenes np.zeros((alto,ancho))'''
im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')

'''coordenadas'''
sob = np.hypot(sx, sy)

'''Tamaño de la ventana'''
plt.figure(figsize=(16, 5))

'''subplot de imagen 1'''

plt.subplot(141)
'''mostramos la imagen 1'''
plt.imshow(im, cmap=plt.cm.gray)
'''con el axis('off') desactivamos los marcos que determinan el ancho y alto de la imagen'''
plt.axis('off')
'''damos el titulo y el tamaño de letra'''
plt.title('square', fontsize=20)


'''subplot de imagen 2'''

plt.subplot(142)
plt.imshow(sx)
plt.axis('off')
plt.title('Sobel (x direction)', fontsize=20)

'''subplot de imagen 3'''

plt.subplot(143)
plt.imshow(sob)
plt.axis('off')
plt.title('Sobel filter', fontsize=20)



'''esto causa el cambio en la imagen 4'''
im += 0.07*np.random.random(im.shape)

'''se actualiza im entonces tambien se cambian las variables sx y sy,
    de esta fmanera se muestra la nueva imagen'''
sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

'''subplot de imagen 4'''


plt.subplot(144)
plt.imshow(sob)
plt.axis('off')
plt.title('Sobel for noisy image', fontsize=20)

'''wspace la es la distancia entre cada imagen'''
plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9)

'''mostramos la ventana'''
plt.show()