import sys
import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.viewer
from PIL import Image
from PIL import ImageOps
import PIL.Image
import matplotlib.pyplot as plt

#take the arguments
filename = sys.argv[1]
outputName = sys.argv[2]


a1 = float(sys.argv[3])
a2 = float(sys.argv[4])
a3 = float(sys.argv[5])
a4 = float(sys.argv[6])
a5 = float(sys.argv[7])
a6 = float(sys.argv[8])


#Reading the input Image

image = skimage.io.imread(fname=filename)
viewer = skimage.viewer.ImageViewer(image)


#taking the values
pix_valRows = image.shape[0]
pix_valCols = image.shape[1]


newImage = np.zeros((pix_valRows,pix_valCols))

t=0
for i in range(pix_valRows):
    t= t+1

    for j in range(pix_valCols):

        #x0 = 0.5 *(float(pix_valRows) - 1) #index for middle pixel
        #y0 = 0.5 *(float(pix_valCols) - 1)

        x0=i-pix_valRows * 0.5
        y0=j-pix_valCols * 0.5

        x0 = int(x0)
        y0 = int(y0)

        #multiply with the affine array(transformation x,y)
        xindex=a1*x0+a2*y0+a3*1
        yindex=a4*x0+a5*y0+a6*1

        #nearest neighbor interpolation x,y
        par_i=xindex+pix_valRows/2
        par_j=yindex+pix_valCols/2

        par_i=round(par_i)
        par_j=round(par_j)

        if(par_i<pix_valRows and par_j<pix_valCols):

            newImage[i][j]=image[par_i][par_j]


print(t)

#display and save the new image

#output = skimage.io.imread(fname=outputName)
#viewer = skimage.viewer.ImageViewer(output)
#viewer.show()


plt.imshow(newImage,cmap="gray")

plt.show()

Image.fromarray(newImage.astype(np.uint8)).save(outputName)
