# OpenCV Image Preprocessing

A collection of Python scripts using OpenCV (`cv2`) and the `os` module to clean, filter, and standardize image datasets for Machine Learning models.

## Features
- **Single Image Filtering (`filter_resize.py`):** Resizes images to uniform dimensions and applies Gaussian blur to reduce visual noise.
- **Automated Batch Processing (`batch_process.py`):** Loops through directories of raw images, resizes them to `224x224` pixels, converts them to grayscale, and exports training-ready datasets.

## Technologies Used
- Python
- OpenCV (`opencv-python`)
- NumPy
