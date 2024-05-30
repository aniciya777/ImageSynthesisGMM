from os import listdir, mkdir
from os.path import isfile, join, exists

import numpy as np
from PIL import Image

from config import IMAGES_DIR, SIZE, DATA_DIR, IS_GRAYSCALE


def load_images() -> np.ndarray:
    if not exists(DATA_DIR):
        mkdir(DATA_DIR)
    data_filename = join(DATA_DIR, f"images_{SIZE}x{SIZE}{'' if IS_GRAYSCALE else '_colored'}.npy")
    if exists(data_filename):
        return np.load(data_filename)

    images = []
    for file in listdir(IMAGES_DIR):
        filename = join(IMAGES_DIR, file)
        if not isfile(filename):
            continue
        if not file.endswith(".jpg"):
            continue
        img = Image.open(filename)
        width, height = img.size
        min_size = min(width, height)
        left_shift = (width - min_size) // 2
        top_shift = (height - min_size) // 2
        img = img.crop((left_shift, top_shift, left_shift + min_size, top_shift + min_size))
        img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
        if IS_GRAYSCALE:
            img = img.convert('L')
        images.append(np.array(img).flatten())
        img.close()
    data = np.array(images)
    np.save(data_filename, data)
    return data
