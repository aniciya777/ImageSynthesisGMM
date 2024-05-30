import math
from os import mkdir
from os.path import join, exists

import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import joblib

from loader import load_images
from config import SIZE, RESULT_DIR, SEED, MAX_ITERATIONS, N_COMPONENTS, IS_GRAYSCALE

# Загрузка набора данных с изображениями
data = load_images()
print(data.shape)

# Обучение GMM
filename = f"{SIZE}x{SIZE}_{N_COMPONENTS}_components{'' if IS_GRAYSCALE else '_colored'}"
model_filename = join(RESULT_DIR, f"gmm_{filename}.pkl")
if not exists(RESULT_DIR):
    mkdir(RESULT_DIR)
if exists(model_filename):
    gmm = joblib.load(model_filename)
else:
    gmm = GaussianMixture(
        n_components=N_COMPONENTS,
        covariance_type='full',
        random_state=SEED,
        max_iter=MAX_ITERATIONS,
        verbose=True,
        verbose_interval=1
    )
    gmm.fit(data)
    joblib.dump(gmm, model_filename)
print('score: ', gmm.score(data))
print('aic: ', gmm.aic(data))
print('bic: ', gmm.bic(data))

# Генерация новых данных
n_samples = 64
generated_data, _ = gmm.sample(n_samples)

# Визуализация сгенерированных изображений
n_rows = math.ceil(math.sqrt(n_samples))
n_cols = math.ceil(n_samples / n_rows)
fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_rows, n_cols))
for i, row_axes in enumerate(axes):
    for j, ax in enumerate(row_axes):
        ind = i * n_cols + j
        if ind < n_samples:
            if IS_GRAYSCALE:
                ax.imshow(generated_data[ind].reshape(SIZE, SIZE), cmap='gray')
            else:
                ax.imshow(generated_data[ind].reshape(SIZE, SIZE, 3))
        ax.axis('off')

fig.suptitle(f'{SIZE}x{SIZE} изображения\nКомпонент GMM: {N_COMPONENTS}', fontsize=25)
image_filename = join(RESULT_DIR, f"generated_{filename}.png")
plt.savefig(image_filename, pad_inches=0.0, dpi=200.0)
plt.show()
