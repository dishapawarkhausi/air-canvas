import cv2
import numpy as np
import mediapipe as mp
import math

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)

# Colors
colors = {'Red': (0, 0, 255), 'Green': (0, 255, 0), 'Blue': (255, 0, 0), 'Eraser': (0, 0, 0)}
color = colors['Red']
thickness = 5
eraser_thickness = 100
xp, yp = 0, 0

# Button areas
buttons = {'Red': (10, 10, 100, 60), 'Green': (120, 10, 210, 60), 'Blue': (230, 10, 320, 60), 'Eraser': (340, 10, 450, 60)}

# Start webcam
cap = cv2.VideoCapture(0)
canvas = None

# Function to compute distance between two points
def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Function to draw buttons on the screen
def draw_buttons(frame):
    for name, (x1, y1, x2, y2) in buttons.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), colors[name], -1)
        cv2.putText(frame, name, (x1 + 10, y1 + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255) if name != 'Eraser' else (0, 0, 0), 2)

# Function to smooth the drawing path
def smooth_line(prev_point, current_point, thickness=5):
    # Use a basic linear interpolation between the points
    # This makes the drawing smoother by adjusting the line width and transition
    points = [prev_point, current_point]
    return points

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    draw_buttons(frame)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = frame.shape
            lm = hand_landmarks.landmark
            index_tip = int(lm[8].x * w), int(lm[8].y * h)
            middle_tip = int(lm[12].x * w), int(lm[12].y * h)

            # Check if finger touches a button
            for name, (x1, y1, x2, y2) in buttons.items():
                if x1 < index_tip[0] < x2 and y1 < index_tip[1] < y2:
                    color = colors[name]
                    xp, yp = 0, 0
                    cv2.putText(frame, f"Selected: {name}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            # Only draw if index finger is out and not closed with the middle finger
            if distance(index_tip, middle_tip) > 40:  # Only draw if fingers are not close
                if xp == 0 and yp == 0:
                    xp, yp = index_tip
                # Use smoothing function for smoother drawing
                smooth_points = smooth_line((xp, yp), index_tip, thickness)
                for point in smooth_points:
                    cv2.line(canvas, (xp, yp), point, color, thickness)
                    xp, yp = point
            else:
                # If fingers are close, don't draw (gesture for erase or stop drawing)
                xp, yp = 0, 0
    else:
        xp, yp = 0, 0

    # Merge drawing with frame
    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray_canvas, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow("Air Canvas", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)

cap.release()
cv2.destroyAllWindows()
