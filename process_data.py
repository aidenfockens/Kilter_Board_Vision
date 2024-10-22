import cv2
import numpy as np
import matplotlib.pyplot as plt

matrix_size = (17, 18)
base_matrix = np.zeros(matrix_size, dtype=int)

# Takes in a screenshot of the climb from the app and creates the initial matrix for it 
# (5 for starts, 6 for finishes, 7 for hand holds, 8 for foot holds)
def process_image(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Calculate the cropping boundaries (removing top 20% and bottom 20%)
    top_crop = int(height * 0.2)  # Crop 20% from the top
    bottom_crop = int(height * 0.8)  # Keep up to 80% (i.e., remove the bottom 20%)

    # Crop the image (from top_crop to bottom_crop along the height, keep the full width)
    cropped_image = image[top_crop:bottom_crop, :]

    hsv_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)

    color_ranges = {
        "green": ((35, 50, 50), (85, 255, 255)),  # Hue range for green
        "purple": ((130, 50, 50), (160, 255, 255)),  # Hue range for purple
        "blue": ((90, 50, 50), (130, 255, 255)),    # Hue range for blue
    }

    all_contours = []

    # Create a copy of the cropped image to draw the contours on
    contour_image = cropped_image.copy()
    
    cropped_height, cropped_width = cropped_image.shape[:2]

    # Calculate the size of each grid cell
    cell_height = cropped_height // 18
    cell_width = cropped_width // 17

    # Draw the grid on the image for visualization
    for i in range(1, 18):  # Draw vertical lines
        cv2.line(contour_image, (i * cell_width, 0), (i * cell_width, cropped_height), (255, 255, 255), 1)
    for j in range(1, 17):  # Draw horizontal lines
        cv2.line(contour_image, (0, j * cell_height), (cropped_width, j * cell_height), (255, 255, 255), 1)

    # Initialize an empty matrix to hold the grid-based results
    matrix = np.zeros((17, 18), dtype=int)


    # Loop through each color range and find contours for each
    for color, (lower_bound, upper_bound) in color_ranges.items():
        # Create a mask for the current color
        mask = cv2.inRange(hsv_image, np.array(lower_bound), np.array(upper_bound))

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw contours on the cropped image (different color for each mask)
        if color == "green":
            cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Green contours
        elif color == "purple":
            cv2.drawContours(contour_image, contours, -1, (255, 0, 255), 2)  # Purple contours
        elif color == "blue":
            cv2.drawContours(contour_image, contours, -1, (0, 0, 255), 2)  # Blue contours

        # Collect the contours for further use if needed
        all_contours.extend(contours)

    # Plot the cropped image (without contours) and the image with contours
    plt.figure(figsize=(10, 5))

    # Plot the cropped image (without contours)
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for proper color display
    plt.title('Cropped Image')
    plt.axis('off')

    # Plot the cropped image with contours
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for proper color display
    plt.title('Cropped Image with Blue, Green, and Purple Contours')
    plt.axis('off')

    # Show the plots
    plt.show()

# Example usage
process_image("IMG_1048.png")
