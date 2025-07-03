import cv2
import mediapipe as mp
import numpy as np
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)


def euclidean_distance(p1, p2):
    return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def count_fingers(hand_landmarks, label):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if label == "Left":
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x else 0)

    # Other four fingers
    for i in range(1, 5):
        if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

# Recognize gestures based on both hands
def detect_gesture(hand1_data, hand2_data):
    (hand1, label1), (hand2, label2) = hand1_data, hand2_data
    f1 = count_fingers(hand1, label1)
    f2 = count_fingers(hand2, label2)
    dist = euclidean_distance(hand1.landmark[8], hand2.landmark[8])  # index tips

    # Operator gestures
    if f1 == 1 and f2 == 1:
        if dist < 0.06:
            return "exit"
        return "+"
    elif (f1, f2) in [(1, 2), (2, 1)]:
        return "-"
    elif (f1, f2) in [(1, 3), (3, 1)]:
        return "*"
    elif (f1, f2) in [(1, 4), (4, 1)]:
        return "/"
    
    # Digit gestures (6–9)
    if (f1 == 5 and f2 in [1, 2, 3, 4]) or (f2 == 5 and f1 in [1, 2, 3, 4]):
        return str(5 + min(f1, f2))

    # Special gestures
    if f1 == 0 and f2 == 0:
        return "="
    if f1 == 2 and f2 == 2:
        return "del"
    if f1 == 5 and f2 == 5:
        return "clear"
    
    return None

# Initialize webcam
cap = cv2.VideoCapture(0)
expression = ""
result = ""
last_update_time = 0
delay = 1.25

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    current_time = time.time()
    hand_data = []

    # Process hands
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_lm, hand_type in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_type.classification[0].label
            hand_data.append((hand_lm, label))
            mp_drawing.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)

        # One hand for digits 0–5
        if len(hand_data) == 1:
            hand_lm, label = hand_data[0]
            count = count_fingers(hand_lm, label)
            if 0 <= count <= 5 and current_time - last_update_time > delay:
                expression += str(count)
                last_update_time = current_time

        # Two hands for gestures
        elif len(hand_data) == 2:
            gesture = detect_gesture(hand_data[0], hand_data[1])
            if gesture and current_time - last_update_time > delay:
                if gesture == "clear":
                    expression = ""
                    result = ""
                elif gesture == "del":
                    expression = expression[:-1]
                elif gesture == "=":
                    try:
                        result = str(eval(expression))
                    except:
                        result = "Error"
                elif gesture == "exit":
                    break
                else:
                    expression += gesture
                last_update_time = current_time

    # Display on screen
    cv2.putText(frame, f"Expression: {expression}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, f"Result: {result}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

    cv2.imshow("Gesture Math Solver", frame)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break
    elif key == ord('c'):
        expression = ""
        result = ""

cap.release()
cv2.destroyAllWindows()
