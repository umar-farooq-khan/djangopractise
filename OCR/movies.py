
import imageio
import os
folder_path = r'C:\Users\umaRf\OneDrive\Desktop\Transfer'
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]
print(image_paths)

with imageio.get_writer(r'movie.gif', mode='I') as writer:
    for filename in image_paths:
        image = imageio.imread(filename)
        writer.append_data(image)