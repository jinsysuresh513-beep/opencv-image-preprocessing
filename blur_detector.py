import cv2
import os

input_folder = "raw_images"

print("Checking image quality...\n")

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is not None:
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Calculate sharpness score using Laplacian variance
            sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

            # If sharpness is below 100, the image is blurry
            if sharpness < 100:
                print(f"[REJECTED - Blurry] {filename} (Score: {int(sharpness)})")
            else:
                print(f"[ACCEPTED - Clear]  {filename} (Score: {int(sharpness)})")
