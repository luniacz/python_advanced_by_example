import numpy as np
from PIL import Image

# create 3d numpy array of zeros, then replace zeors with yellow pxls
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')