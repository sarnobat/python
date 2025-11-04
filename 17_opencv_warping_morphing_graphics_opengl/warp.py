import cv2
import numpy as np

canvas_size = 400
padding = 50
frames = 60
sides = 32  # target polygon edges

img = np.zeros((canvas_size, canvas_size), dtype=np.uint8)

# Square vertices expanded to match 'sides'
square = np.zeros((sides, 2), dtype=np.float32)
points_per_side = sides // 4
square_min = padding
square_max = canvas_size - padding
for i in range(points_per_side):
    t = i / points_per_side
    # Top edge
    square[i] = [square_min + t*(square_max - square_min), square_min]
    # Right edge
    square[i + points_per_side] = [square_max, square_min + t*(square_max - square_min)]
    # Bottom edge
    square[i + 2*points_per_side] = [square_max - t*(square_max - square_min), square_max]
    # Left edge
    square[i + 3*points_per_side] = [square_min, square_max - t*(square_max - square_min)]

# Target polygon: 32-gon approximating a circle, scaled to fit square bbox
center = (square_min + square_max)/2
half_width = (square_max - square_min)/2
angles = np.linspace(0, 2*np.pi, sides, endpoint=False)
target = np.zeros((sides, 2), dtype=np.float32)
for i, a in enumerate(angles):
    target[i] = [center + half_width*np.cos(a), center + half_width*np.sin(a)]

# Morph loop
for t in np.linspace(0, 1, frames):
    shape = (1-t)*square + t*target

    img.fill(0)
    cv2.fillPoly(img, [shape.astype(np.int32)], 255)

    cv2.imshow(f"Square → {sides}-gon Morph", img)
    key = cv2.waitKey(50)
    if key & 0xFF == 27:
        break

cv2.imshow(f"Square → {sides}-gon Morph", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
