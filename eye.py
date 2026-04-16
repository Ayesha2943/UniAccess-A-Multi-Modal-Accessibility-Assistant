import cv2
import mediapipe as mp
import pyautogui

# Initialize Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Start webcam
cam = cv2.VideoCapture(0)

# Get screen size
screen_w, screen_h = pyautogui.size()

# For smoothing
prev_x, prev_y = 0, 0
smoothening = 5  # higher = smoother but slower

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)

    frame_h, frame_w, _ = frame.shape

    if output.multi_face_landmarks:
        landmarks = output.multi_face_landmarks[0].landmark

        # Eye point (stable iris landmark)
        eye_point = landmarks[475]

        x = int(eye_point.x * frame_w)
        y = int(eye_point.y * frame_h)

        screen_x = eye_point.x * screen_w
        screen_y = eye_point.y * screen_h

        # Smooth movement
        curr_x = prev_x + (screen_x - prev_x) / smoothening
        curr_y = prev_y + (screen_y - prev_y) / smoothening

        pyautogui.moveTo(curr_x, curr_y)
        prev_x, prev_y = curr_x, curr_y

        # Blink detection (left eye)
        left_eye_top = landmarks[145]
        left_eye_bottom = landmarks[159]

        if (left_eye_top.y - left_eye_bottom.y) < 0.01:
            pyautogui.click()
            pyautogui.sleep(1)

        # Draw pointer
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow("Eye Controlled Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cam.release()
cv2.destroyAllWindows()