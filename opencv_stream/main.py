import cv2
import requests
import numpy as np

# Replace with the IP address of your ESP32-CAM
ESP32_URL = "http://192.168.179.208/"

while True:
    # Fetch the JPEG frame
    response = requests.get(ESP32_URL, stream=True)
    if response.status_code == 200:
        np_arr = np.frombuffer(response.content, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Display the frame
        cv2.imshow("ESP32-CAM Stream", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to fetch the frame")

cv2.destroyAllWindows()
