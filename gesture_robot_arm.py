import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# Initialize hand detector
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip and convert to RGB
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process image
        results = hands.process(rgb)

        finger_count = 0
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get landmarks
                landmarks = hand_landmarks.landmark

                # Thumb
                if landmarks[4].x < landmarks[3].x:
                    finger_count += 1
                # Other fingers
                tips = [8, 12, 16, 20]
                for tip in tips:
                    if landmarks[tip].y < landmarks[tip - 2].y:
                        finger_count += 1

        # Simulated robotic arm action
        if finger_count == 0:
            action = "Arm is Idle"
        elif finger_count == 1:
            action = "Arm moves Right"
        elif finger_count == 2:
            action = "Arm moves Left"
        elif finger_count == 3:
            action = "Arm moves Up"
        elif finger_count == 4:
            action = "Arm moves Down"
        elif finger_count == 5:
            action = "Arm Grabs Object"
        else:
            action = "Unknown Action"

        # Show info on screen
        cv2.putText(frame, f'Fingers: {finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f'Action: {action}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Gesture Controlled Robotic Arm", frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()