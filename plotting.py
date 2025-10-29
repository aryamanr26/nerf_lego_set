import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def plot_images_grid(image_paths, rows=6, cols=5, figsize=(15, 18), col_titles=None, save_path="grid_plot.png"):
    """
    Plot images in a column-wise grid and label each column.

    Args:
        image_paths (list[str]): List of image file paths.
        rows (int): Number of rows in grid.
        cols (int): Number of columns in grid.
        figsize (tuple): Figure size.
        col_titles (list[str]): Optional column titles.
        save_path (str): Where to save the figure.
    """
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.flatten()

    total_slots = rows * cols
    n_imgs = min(len(image_paths), total_slots)

    for idx in range(n_imgs):
        col = idx // rows
        row = idx % rows
        ax = axes[row * cols + col]
        img = mpimg.imread(image_paths[idx])
        ax.imshow(img)
        ax.axis("off")

    # Add titles per column (top row)
    if col_titles:
        for col in range(min(cols, len(col_titles))):
            ax_top = axes[col]  # top of each column
            ax_top.set_title(col_titles[col], fontsize=14, pad=15)

    plt.tight_layout(pad=0.3)
    plt.savefig(save_path, bbox_inches="tight", dpi=300)
    print(f"✅ Grid with column titles saved at: {save_path}")
    plt.close(fig)


# Example usage
folders = ["testset_000500", "testset_002000", "testset_005000", "testset_010000", "testset_020000"]
images = []

for folder in folders:
    base = f"/scratch/eecs542f25_class_root/eecs542f25_class/aryamanr/hw4nvs/logs/blender_lego_fine/{folder}"
    images.extend([
        f"{base}/000_depth.png",
        f"{base}/000_rgb.png",
        f"{base}/001_depth.png",
        f"{base}/001_rgb.png",
        f"{base}/002_depth.png",
        f"{base}/002_rgb.png"
    ])

col_titles = ["500 iters", "2000 iters", "5000 iters", "10000 iters", "20000 iters"]

plot_images_grid(images, rows=6, cols=5, col_titles=col_titles, save_path="plots/lego_column_titles.png")
