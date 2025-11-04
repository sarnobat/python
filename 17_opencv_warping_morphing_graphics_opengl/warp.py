import cv2
import numpy as np

size = 300
square = np.zeros((size, size), dtype=np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -1)

# Create coordinates grid
Y, X = np.indices((size, size))
center = size / 2
radius = 100

# Normalize coordinates relative to center
Xn = (X - center) / (size / 2)
Yn = (Y - center) / (size / 2)

# Distance from center (for circular warp)
R = np.sqrt(Xn**2 + Yn**2)
angle = np.arctan2(Yn, Xn)

for t in np.linspace(0, 1, 100):  # animate from square (t=0) to circle (t=1)
    # Interpolate between square coordinates and circular coordinates
    Xw = (1-t) * X + t * (center + radius * R * np.cos(angle))
    Yw = (1-t) * Y + t * (center + radius * R * np.sin(angle))

    # Map coordinates back to original image
    warped = cv2.remap(square.astype(np.float32), Xw.astype(np.float32), Yw.astype(np.float32),
                       interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Warping", warped.astype(np.uint8))
    cv2.waitKey(30)

cv2.destroyAllWindows()
