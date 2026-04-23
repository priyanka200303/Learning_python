import numpy as np
from PIL import Image

img=np.array(Image.open("/home/mdl/priyanka/snap_1080p_11-15-43-016.png"))

Image.fromarray(img).show()

