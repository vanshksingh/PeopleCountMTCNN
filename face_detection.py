from mtcnn import MTCNN
import cv2

# Initialize MTCNN face detector
detector = MTCNN()

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change 0 to the appropriate camera index if multiple cameras are available

# Initialize empty list to store detected faces
detected_faces = []

# Initialize font and position for text overlay
font = cv2.FONT_HERSHEY_SIMPLEX
text_position = (10, 30)
font_scale = 0.8
font_thickness = 2

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to RGB (MTCNN expects RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the frame
    faces = detector.detect_faces(rgb_frame)

    # Clear the list of detected faces
    detected_faces.clear()

    # Add detected faces to the list
    for result in faces:
        x, y, w, h = result['box']
        detected_faces.append((x, y, w, h))

    # Draw rectangles around detected faces
    for (x, y, w, h) in detected_faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display count of faces as overlay
    cv2.putText(frame, f'Faces Count: {len(detected_faces)}', text_position, font, font_scale, (0, 255, 0),
                font_thickness)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
