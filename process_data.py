import cv2
import numpy as np
import matplotlib.pyplot as plt



#5 for starting, 6 for ending, 7 for normal holds
def process_image(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Calculate the cropping boundaries (removing top 25% and bottom 25%)
    top_crop = int(height * 0.305)  # Crop 25% from the top
    bottom_crop = int(height * 0.77)  # Keep up to 75% (i.e., remove the bottom 25%)
    left_crop = int(width *.03)
    right_crop= int(width *.97)
    # Crop the image (from top_crop to bottom_crop along the height, keep the full width)
    cropped_image = image[top_crop:bottom_crop,left_crop:right_crop]

    hsv_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)

    color_ranges = {
        "green": ((50, 50, 50), (75, 255, 255)),  # Hue range for green
        "blue": ((90, 50, 50), (125, 255, 255)),
        "purple": ((148, 50, 50), (152, 255, 255)),  # Hue range for purple
            # Hue range for blue
    }

    all_contours = []

    # Create a copy of the cropped image to draw the contours and the grid on
    contour_image = cropped_image.copy()

    # Get the height and width of the cropped image
    cropped_height, cropped_width = cropped_image.shape[:2]

    # Calculate the size of each grid cell
    cell_height = cropped_height // 18  # 18 rows (height)
    cell_width = cropped_width // 17  # 17 columns (width)

    # Draw the grid on the image for visualization
    for i in range(1, 17):  # Draw vertical lines (17 columns)
        cv2.line(contour_image, (i * cell_width, 0), (i * cell_width, cropped_height), (0, 0, 0), 2)  # Black lines, thicker (2 px)
    for j in range(1, 18):  # Draw horizontal lines (18 rows)
        cv2.line(contour_image, (0, j * cell_height), (cropped_width, j * cell_height), (0, 0, 0), 2)

    # Initialize an empty matrix to hold the grid-based results
    matrix = np.zeros((18, 17), dtype=int)

    # Loop through each color range and find contours for each
    for color, (lower_bound, upper_bound) in color_ranges.items():
        # Create a mask for the current color
        mask = cv2.inRange(hsv_image, np.array(lower_bound), np.array(upper_bound))

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:       
            area = cv2.contourArea(contour)
            if area < 300:
                continue
            M = cv2.moments(contour)
            if M["m00"] != 0:
                # Calculate the center of the contour
                center_x = int(M["m10"] / M["m00"])
                center_y = int(M["m01"] / M["m00"])

                # Map the center of the contour to the grid
                grid_x = center_x // cell_width
                grid_y = center_y // cell_height

            # Assign the corresponding matrix value based on the color
            if color == "green":
                matrix[grid_y, grid_x] = 5
            elif color == "purple":
                matrix[grid_y, grid_x] = 6
            elif color == "blue":
                matrix[grid_y, grid_x] = 7

            # Draw contours on the cropped image (different color for each mask)
            if color == "green":
                cv2.drawContours(contour_image, [contour], -1, (0, 255, 0), 2)  # Green contours
            elif color == "purple":
                cv2.drawContours(contour_image, [contour], -1, (255, 0, 255), 2)  # Purple contours
            elif color == "blue":
                cv2.drawContours(contour_image, [contour], -1, (0, 0, 255), 2)  # Blue contours

    # Plot the cropped image with contours and the grid
    plt.figure(figsize=(10, 5))

    # Plot the cropped image with contours and the grid
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for proper color display
    plt.title('Cropped Image with Grid and Contours')
    plt.axis('off')

    # Display the matrix
    plt.subplot(1, 2, 2)
    plt.imshow(matrix, cmap='viridis')
    plt.title('Grid-based Matrix')
    plt.axis('off')

    # Show the plots
    plt.show()

    # Return the matrix for further use
    return matrix


#SHOWS IMPLEMENTATION

#matrix = process_image("IMG_1048.png")
#print(matrix)






# FOR TESTING THE COLOR VALUES:

def get_hsv_value(image_path):
    image = cv2.imread(image_path)
    
    # Convert to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Click on a pixel and get the HSV value
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel_hsv = hsv_image[y, x]
            print(f'HSV value at ({x},{y}): {pixel_hsv}')

    # Show the image and set up the mouse callback
    cv2.imshow('image', image)
    cv2.setMouseCallback('image', click_event)

    # Wait until a key is pressed, then close
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with your image
#get_hsv_value('IMG_1048.png')