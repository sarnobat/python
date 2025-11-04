import cv2
import numpy as np

canvas_size = 400
padding = 50
frames = 60

img = np.zeros((canvas_size, canvas_size), dtype=np.uint8)

# Square vertices (clockwise, inside padded region)
square = np.array([
    [padding, padding],
    [canvas_size-padding, padding],
    [canvas_size-padding, canvas_size-padding],
    [padding, canvas_size-padding]
], dtype=np.float32)

# Octagon vertices (clockwise, inside padded region)
a = padding + 0.3*(canvas_size-2*padding)
b = canvas_size - padding - 0.3*(canvas_size-2*padding)
octagon = np.array([
    [a, padding],
    [b, padding],
    [canvas_size-padding, a],
    [canvas_size-padding, b],
    [b, canvas_size-padding],
    [a, canvas_size-padding],
    [padding, b],
    [padding, a]
], dtype=np.float32)

# Expand square to 8 points to match octagon
square8 = np.zeros((8, 2), dtype=np.float32)
square8[0] = square[0]
square8[1] = square[0]
square8[2] = square[1]
square8[3] = square[1]
square8[4] = square[2]
square8[5] = square[2]
square8[6] = square[3]
square8[7] = square[3]

for t in np.linspace(0, 1, frames):
    shape = (1-t)*square8 + t*octagon

    img.fill(0)
    cv2.fillPoly(img, [shape.astype(np.int32)], 255)

    cv2.imshow("Square → Octagon Morph", img)
    key = cv2.waitKey(50)
    if key & 0xFF == 27:
        break

cv2.imshow("Square → Octagon Morph", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
