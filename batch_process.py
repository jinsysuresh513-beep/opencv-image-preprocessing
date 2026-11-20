import cv2
import os

input_folder = "raw_images"
output_folder = "clean_images"

# Loop through every file inside the raw_images folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is not None:
            # Resize to 224x224 (Standard size for AI models)
            resized = cv2.resize(img, (224, 224))
            
            # Convert to Grayscale
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

            # Save the processed image into the clean_images folder
            save_path = os.path.join(output_folder, "clean_" + filename)
            cv2.imwrite(save_path, gray)
            print(f"Processed: {filename}")

print("All images cleaned and saved!")

