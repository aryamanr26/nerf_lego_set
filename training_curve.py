import re
import matplotlib.pyplot as plt

# Paste your log text here or read from file
log_path = "eecs542_hw4_1.log"  # <- save your text above to this file first

# Parse data
iters, losses, psnrs = [], [], []
with open(log_path, "r") as f:
    for line in f:
        match = re.search(r"\[TRAIN\]\s+Iter:\s*(\d+)\s+Loss:\s*([\d\.eE+-]+)\s+PSNR:\s*([\d\.eE+-]+)", line)
        if match:
            iters.append(int(match.group(1)))
            losses.append(float(match.group(2)))
            psnrs.append(float(match.group(3)))

# Plot Loss and PSNR
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(iters, losses, color='red', linewidth=2)
plt.xlabel("Iteration")
plt.ylabel("Training Loss")
plt.title("Training Loss Curve")
plt.grid(True, linestyle="--", alpha=0.6)

plt.subplot(1,2,2)
plt.plot(iters, psnrs, color='blue', linewidth=2)
plt.xlabel("Iteration")
plt.ylabel("Training PSNR (dB)")
plt.title("Training PSNR Curve")
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("plots/train_loss_psnr_curves.png", dpi=300, bbox_inches='tight')
plt.show()

print(f"✅ Parsed {len(iters)} points. Saved plot as train_loss_psnr_curves.png")
