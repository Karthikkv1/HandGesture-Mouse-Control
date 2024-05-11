

# Handgesture Mouse Control using Python with OpenCV, MediaPipe, and PyAutoGUI

This Python project enables users to control their mouse cursor using hand gestures captured through a webcam. It utilizes OpenCV for video capture, MediaPipe for hand tracking, and PyAutoGUI for controlling the mouse cursor.

## Features

- **Hand Gesture Detection**: Detects hand gestures in real-time using a webcam.
- **Mouse Cursor Control**: Maps hand movements to mouse cursor movements on the screen.
- **Click Event**: Performs a click event when the distance between specified hand landmarks is less than a certain threshold.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```
   pip install opencv-python mediapipe pyautogui
   ```
3. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```

## Usage

1. Run the main program using Python:
   ```
   python handgesture_mouse_control.py
   ```
2. Place your hand in front of the webcam to start controlling the mouse cursor.
3. Move your hand to move the mouse cursor on the screen.
4. Click by bringing specific fingers close together.
5. Press the 'Esc' key to exit the application.



## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

