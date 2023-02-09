
import cv2
import os

folder_path = r'C:\Users\umaRf\OneDrive\Desktop\Transfer'
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]
print(image_paths)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1920, 1080))


for image_path in image_paths:
    image = cv2.imread(image_path)
    out.write(image)
    print('gfdg')

out.release()
