
# Face Detection Using MTCNN and OpenCV

![Screenshot 2024-04-23 at 4 47 34 AM](https://github.com/vanshksingh/PeopleCountMTCNN/assets/114809624/6d6ec0b7-1f7b-4f0a-9f4c-59ffe7d59b30)



This script demonstrates how to use the MTCNN face detector and OpenCV to perform face detection in a live video stream from a webcam. The script continuously captures frames from the webcam, detects faces using MTCNN, and overlays rectangles around the detected faces. Additionally, it displays the count of detected faces on the frame.

## Prerequisites

- Python 3.x
- OpenCV
- MTCNN

## Installation

1. Install the required packages:

    ```bash
    pip install opencv-python mtcnn
    ```

2. Make sure your webcam is connected and functioning properly.

## Usage

1. Save the script to a file, e.g., `face_detection.py`.

2. Run the script:

    ```bash
    python face_detection.py
    ```

3. The script will start capturing video from your default webcam (camera index `0`). If you have multiple cameras, you may need to change the camera index in the script.

4. The script will display a video feed with rectangles around detected faces and a count of faces in the frame.

5. Press `q` to stop the script and close the video feed.

## Code Description

- The script initializes a face detector using the MTCNN library and captures video from the webcam using OpenCV.

- It converts each frame to RGB (as MTCNN expects RGB images) and performs face detection using MTCNN.

- For each detected face, the script draws a green rectangle around the face on the frame.

- It also overlays the count of detected faces as text on the video feed.

- The script runs in a loop, processing frames continuously until the `q` key is pressed to exit.

- When exiting, the script releases the webcam and closes all OpenCV windows.

## Notes

- You may need to adjust the `font` parameters (e.g., font size, color) to suit your preferences.

- The script currently uses the default camera index (`0`) for video capture. Adjust the index as needed for different camera setups.

---

That's the README for the script! Let me know if you need any more information or assistance.
