import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
import command_handler


def log_transform(image: np.ndarray) -> np.ndarray:
    """
    Aplica transformação logarítmica:
    s = c * log(1 + r), onde c = 255 / log(1 + 255)
    """
    img = image.astype(np.float64)
    c = 255 / np.log1p(255)
    result = c * np.log1p(img)
    return np.clip(result, 0, 255).astype(np.uint8)


def gamma_transform(image: np.ndarray, gamma: float) -> np.ndarray:
    """
    Aplica transformação de potência (gamma):
    s = (r/255)^gamma * 255
    """
    img = image.astype(np.float64) / 255.0
    result = np.power(img, gamma) * 255
    return np.clip(result, 0, 255).astype(np.uint8)


def threshold_transform(image: np.ndarray, thresh: int = 128) -> np.ndarray:
    """
    Aplica limiarização simples:
    s = 255 se r >= thresh, caso contrário 0
    """
    return np.where(image >= thresh, 255, 0).astype(np.uint8)


# Tentar carregar imagem real; se não existir, usa um gradiente de exemplo
file_name = command_handler.parse_asset_index()
file_path = 'assets/' + file_name

if os.path.exists(file_path):
    img = np.array(Image.open(file_path))
else:
    img = np.tile(np.linspace(0, 255, 256, dtype=np.uint8), (256, 1))

# Aplicar transformações
log_img = log_transform(img)
gamma_img = gamma_transform(img, gamma=0.5)
thr_img = threshold_transform(img, thresh=128)

# Exibir resultados
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
titles = ['Original', 'Transformação logarítmica (c=255)',
          'Transformação exponencial (γ=0.5)', 'Limiarização (128)']
images = [img, log_img, gamma_img, thr_img]

for ax, im, title in zip(axs.flatten(), images, titles):
    ax.imshow(im, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

new_file_name = file_name.replace('.jpg', '_transformed.png')

plt.tight_layout()
plt.savefig('results/' + new_file_name)

print(f"\033[32m[ok] {new_file_name} foi gerado!\033[0m")
