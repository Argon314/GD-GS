# Eliminating Visual Artifacts in 3D Gaussian Splatting for High-Fidelity Novel View Displays

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

<p align="center">
  <img src="assets/pipeline.png" alt="Pipeline" width="85%"/>
  <br>
  <em>Figure: Overview of the proposed dual-branch optimization framework.</em>
</p>

---


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

