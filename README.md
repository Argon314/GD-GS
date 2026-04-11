# GD-GS: Geometry-Guided and Depth-Adaptive 3D Gaussian Splatting for Sparse View Synthesis

<p align="center">
  <img src="assets/teaser.png" alt="GD-GS Teaser" width="90%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square"/>
</p>

---
---

## 📌 Status

> ⚠️ **Code is currently being prepared for public release.**
> It will be made publicly available upon paper acceptance / after the review process.

---

## 📌 News

- **[2026.04]** Paper submitted to *DISPLAYS* for review.

---

## Overview

3D Gaussian Splatting (3DGS) has become the mainstream paradigm for real-time novel view synthesis. However, under sparse input views, standard 3DGS suffers from severe geometric instability — floating artifacts near the camera and background collapse in distant regions. **GD-GS** addresses these challenges with a dual-branch optimization framework:

- **PCGR (Pearson Correlation Geometric Regularization)**: Introduces monocular depth priors via a scale-invariant Pearson correlation loss, directly aligning the spatial distribution of Gaussian primitives with the relative scene structure — without requiring metric depth supervision.
- **DAIP (Depth-Adaptive Importance Pruning)**: Dynamically removes redundant Gaussian primitives using gradient-free physical importance scores combined with a spatial depth decay factor, suppressing floaters near the camera while protecting distant background geometry.

<p align="center">
  <img src="assets/pipeline.png" alt="Pipeline" width="85%"/>
  <br>
  <em>Figure: Overview of the proposed GD-GS dual-branch optimization framework.</em>
</p>

---

## Quantitative Results

### LLFF Dataset (3 / 6 / 9 views)

| Method      | 3-view PSNR | SSIM   | LPIPS   | 6-view PSNR | SSIM   | LPIPS   | 9-view PSNR | SSIM   | LPIPS   |
|-------------|-------------|--------|---------|-------------|--------|---------|-------------|--------|---------|
| FreeNeRF    | 19.63       | 0.612  | 0.308   | 23.73       | 0.779  | 0.195   | 25.13       | 0.827  | 0.160   |
| 3DGS        | 19.22       | 0.649  | 0.229   | 23.80       | 0.814  | 0.125   | 25.44       | 0.860  | 0.096   |
| DNGaussian  | 19.12       | 0.591  | 0.294   | 22.18       | 0.755  | 0.198   | 23.17       | 0.788  | 0.180   |
| Scaffold-GS | 19.08       | 0.657  | 0.263   | 23.94       | 0.763  | 0.176   | 25.28       | 0.852  | 0.114   |
| PUP-3DGS    | 19.85       | 0.694  | 0.252   | 24.17       | 0.819  | 0.145   | 25.37       | 0.863  | 0.109   |
| DropGaussian| 20.76       | 0.713  | 0.200   | 24.74       | 0.837  | 0.117   | 26.21       | 0.874  | 0.088   |
| **Ours**    | **21.32**   | **0.739** | **0.182** | **25.56** | **0.868** | **0.122** | **26.54** | **0.893** | **0.085** |

### Mip-NeRF360 Dataset (12 / 24 views)

| Method       | 12-view PSNR | SSIM   | LPIPS   | TNGP     | 24-view PSNR | SSIM   | LPIPS   | TNGP     |
|--------------|-------------|--------|---------|----------|--------------|--------|---------|----------|
| 3DGS         | 18.52       | 0.523  | 0.415   | 1420K    | 22.80        | 0.708  | 0.276   | 1150K    |
| FSGS         | 18.80       | 0.531  | 0.418   | 485K     | 23.70        | 0.745  | 0.230   | 370K     |
| Scaffold-GS  | 19.12       | 0.561  | 0.394   | 683K     | 23.74        | 0.731  | 0.254   | 526K     |
| CoR-GS       | 19.52       | 0.558  | 0.418   | 520K     | 23.39        | 0.727  | 0.271   | 425K     |
| DropGaussian | 19.74       | 0.577  | 0.364   | 550K     | 24.13        | 0.762  | 0.225   | 450K     |
| **Ours**     | **20.36**   | **0.592** | **0.379** | **460K** | **24.49** | **0.795** | **0.212** | **390K** |

*Full results including SSIM, LPIPS, and additional baselines are provided in the paper.*


---

## Visual Comparisons

## Visual Comparisons

<p align="center">
  <img src="assets/comparisons.png" alt="Visual Comparisons" width="90%"/>
  <br>
  <em>Qualitative comparisons on LLFF datasets.
  GD-GS eliminates floating artifacts and preserves distant background geometry.</em>
</p>


---

## Installation



### Requirements

- Python 3.8+
- CUDA 11.7+
- NVIDIA GPU (12GB+ recommended)

### Dependencies

```bash
# Clone the repository
git clone https://github.com/Argon314/GD-GS.git
cd GD-GS

# Create conda environment
conda create -n gdgs python=3.9
conda activate gdgs

# Install PyTorch
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Install dependencies
pip install -r requirements.txt

