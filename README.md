# ✋ Gesture-Based Math Solver

A real-time, webcam-powered math solver that lets you perform calculations using only your **hands**. No mouse, no keyboard — just **Python magic + gestures**!

---

## 🚀 What is a Gesture-Based Math Solver?

A Gesture-Based Math Solver is an interactive Python app that:

- 📷 Tracks your hand movements
- ✌️ Recognizes how many fingers you show
- ➕ Converts those into numbers or operations
- 🧮 Evaluates the expression in real-time  
All using just your webcam, hands, and some Python awesomeness!

---

## 🎯 What You Will Learn

✅ Real-time webcam input using OpenCV  
✅ Hand gesture recognition using MediaPipe  
✅ Finger counting logic with Python  
✅ Building and evaluating expressions  
✅ Gesture commands like `delete`, `clear`, `exit`

---

## 🧰 Tech Stack Used

| Tool      | Purpose                                      |
|-----------|----------------------------------------------|
| Python    | Main programming language                    |
| OpenCV    | Capture and display webcam input             |
| MediaPipe | AI-powered hand tracking (21 keypoints/hand) |
| NumPy     | Math calculations (e.g., finger distance)    |
| eval()    | Built-in Python method to evaluate math      |

---

## 📷 How It Works – Behind the Scenes

### 🪜 Step-by-Step Process:

1. **Start Webcam**  
   OpenCV captures your video feed in real-time.

2. **Detect Hands**  
   MediaPipe finds and tracks 21 hand landmarks.

3. **Count Fingers**  
   Logic checks which fingers are up or down to detect:
   - Numbers (0–9)
   - Operators (`+`, `−`, `×`, `÷`)
   - Commands (`=`, `delete`, `clear`, `exit`)

4. **Build Math Expression**  
   Each gesture adds a part to the expression.

5. **Evaluate Expression**  
   Show the "equal" gesture to solve it.

---

## 🧠 Hand Gesture Reference Guide

| Gesture (Fingers)     | Action   | Meaning         |
|------------------------|----------|------------------|
| 0 fingers (1 hand)     | Add 0    | Digit            |
| 1–5 fingers (1 hand)   | Add 1–5  | Digit            |
| 5 + 1 fingers          | Add 6    | Digit            |
| 5 + 2 fingers          | Add 7    | Digit            |
| 5 + 3 fingers          | Add 8    | Digit            |
| 5 + 4 fingers          | Add 9    | Digit            |
| 1 + 1 fingers (2 hands)| Add `+`  | Addition         |
| 1 + 2 fingers          | Add `−`  | Subtraction      |
| 1 + 3 fingers          | Add `×`  | Multiplication   |
| 1 + 4 fingers          | Add `÷`  | Division         |
| 0 + 0 fingers          | `=`      | Evaluate         |
| 2 + 2 fingers          | `del`    | Delete last      |
| 5 + 5 fingers          | `clear`  | Clear input      |
| Index fingers close    | `exit`   | Quit app         |

---

## 🔨 How to Build and Run the Project

### 1️⃣ Create a Project Folder

```bash
mkdir GestureMathSolver
cd GestureMathSolver
python -m venv venv
2️⃣ Activate the Virtual Environment
# For Windows
.\venv\Scripts\activate
3️⃣ Install Required Libraries
bash
pip install opencv-python mediapipe numpy
4️⃣ Create the Python File
Save the main script as gesture_math_solver.py.
(Include the full code in this repo)
5️⃣ Run the App
python gesture_math_solver.py

