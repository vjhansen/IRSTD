import numpy as np
import matplotlib.pyplot as plt
import cv2


IMG_NAME = "my_mod_CNRS.onnxconv4_block1_2_conv_wght"

img1 = cv2.imread(IMG_NAME + ".jpg", 0)
img1 = img1 / 255


# create the x and y coordinate arrays (here we just use pixel indices)
xx, yy = np.mgrid[0 : img1.shape[0], 0 : img1.shape[1]]
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(xx, yy, img1, cmap="Blues", linewidth=0, antialiased=False)

ax.azim = 0
ax.dist = 8
ax.elev = 40
ax.axis("off")

plt.savefig("surf_plot_" + IMG_NAME + ".pdf", pad_inches=0, bbox_inches="tight")
plt.show()
