
import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Set up webcam
cap = cv2.VideoCapture(0)

# Get the screen width and height for mouse movement
screen_width, screen_height = pyautogui.size()

# Variables for drag and drop (both fingers pressed)
dragging = False
last_click_time = 0  # To track time between clicks
click_threshold = 0.5  # Time threshold for double-click (seconds) - increase this if double-click is too sensitive
click_count = 0  # Track the number of clicks

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for better user experience
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the position of the index and middle fingers (landmark IDs 8 for index, 12 for middle)
            index_finger_tip = hand_landmarks.landmark[8]
            middle_finger_tip = hand_landmarks.landmark[12]

            # Convert the normalized values to pixel values
            index_x, index_y = int(index_finger_tip.x * screen_width), int(index_finger_tip.y * screen_height)
            middle_x, middle_y = int(middle_finger_tip.x * screen_width), int(middle_finger_tip.y * screen_height)

            # Move the mouse to the index finger position
            pyautogui.moveTo(index_x, index_y)

            # Check if both index and middle fingers are close to each other (for drag or click)
            distance = ((index_x - middle_x) ** 2 + (index_y - middle_y) ** 2) ** 0.5

            # If the distance between the fingers is small, consider it as clicking
            if distance < 50:
                current_time = time.time()

                # If it's close enough to a previous click (within click_threshold), consider it as a double click
                if current_time - last_click_time < click_threshold:
                    click_count += 1
                    if click_count == 2:
                        pyautogui.doubleClick()  # Perform double click
                        click_count = 0  # Reset after double click
                        last_click_time = 0  # Reset last click time after double-click
                else:
                    click_count = 1  # Start tracking new click
                    last_click_time = current_time  # Update the last click time

                # Handle dragging (if fingers are held down close together)
                if not dragging:
                    pyautogui.mouseDown()  # Press the mouse button down
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()  # Release the mouse button
                    dragging = False

    # Display the frame
    cv2.imshow("Hand Gesture Control", frame)

    # Exit condition on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
