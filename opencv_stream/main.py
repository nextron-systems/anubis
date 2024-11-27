import cv2

# Replace with the IP address of your ESP32-CAM
ESP32_URL = "http://192.168.179.208/"

# Open a connection to the ESP32-CAM stream
cap = cv2.VideoCapture(ESP32_URL)

if not cap.isOpened():
    print("Error: Unable to open video stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame
    cv2.imshow("ESP32-CAM Stream", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()