import cv2
import numpy as np

def measure_object(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    
    # Perform edge detection
    edged = cv2.Canny(blurred, 50, 100)
    
    # Find contours
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort contours by area (largest to smallest)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    # Loop over the contours
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Draw the bounding box on the original image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Compute the center of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        
        # Draw the center of the contour
        cv2.circle(image, (cX, cY), 5, (0, 255, 0), -1)
        
        # Print the dimensions of the object
        print(f"Object dimensions: Width={w} px, Height={h} px")
        
        # For demonstration, let's only process the largest contour
        break
    
    # Show the output image
    cv2.imshow("Image with measured object", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
measure_object(r"C:\Users\sonal\OneDrive\Desktop\cg\images1.jpg")
