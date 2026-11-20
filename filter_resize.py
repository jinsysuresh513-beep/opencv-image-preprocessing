import cv2

# 1. Load the image from your folder
img = cv2.imread("sample.jpg")

# Check if the image was found
if img is None:
    print("Error: Could not find 'sample.jpg'. Make sure it is in the same folder!")
else:
    # 2. Resize the image to 300x300 pixels (Standard size for ML models)
    resized = cv2.resize(img, (300, 300))

    # 3. Apply a Gaussian Blur filter (Removes noise/grain from images)
    blurred = cv2.GaussianBlur(resized, (7, 7), 0)

    # 4. Save the cleaned, resized image as a new file
    cv2.imwrite("cleaned_sample.jpg", blurred)

    print("Success! Saved 'cleaned_sample.jpg' in your folder.")

    # Show original and processed images side-by-side
    cv2.imshow("Original", img)
    cv2.imshow("Resized & Filtered", blurred)

    # Wait for any key press to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
