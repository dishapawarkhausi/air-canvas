
# AirCanvas

**AirCanvas** is an innovative project that enables users to draw on a virtual canvas using hand gestures, specifically focusing on drawing with the index finger. The application uses **OpenCV** and **MediaPipe** to detect hand gestures and translate them into real-time drawing actions on the screen. The project also features additional functionalities such as adjustable pen thickness, color options, and an eraser tool to enhance the drawing experience.

## Features
- **Gesture-based Drawing**: Draw with your index finger, just like a real-world pen.
- **Pen Thickness**: Adjust the thickness of the pen to make your strokes bold or fine.
- **Color Options**: Choose different colors for drawing to make your artwork vibrant.
- **Eraser Tool**: Erase unwanted parts of the drawing easily.
- **Real-Time Feedback**: See the drawing instantly as you move your hand.
- **Air Gesture Detection**: Detect gestures with high accuracy using MediaPipe and OpenCV.

## Requirements

Make sure you have Python installed on your system. Then, install the necessary libraries:

```bash
pip install opencv-python mediapipe numpy
```

## Installation & Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/dishapawarkhausi/aircanvas.git
    ```

2. Navigate to the project folder:

    ```bash
    cd aircanvas
    ```

3. Install required dependencies (as shown above).

4. Run the main Python script:

    ```bash
    python main.py
    ```

## How It Works

- The application uses **OpenCV** to capture video feed from your camera.
- **MediaPipe** is used to detect hand gestures and the position of your fingers.
- Based on the position of your index finger, the application draws lines on the screen.
- You can change the pen color and thickness using on-screen controls, and use the eraser tool to remove parts of your drawing.

## Demo

You can find a demo of the project here (add demo link if available).

## Contributing

Contributions are welcome! If you'd like to contribute, feel free to fork the repository, submit issues, or open pull requests. Please make sure your code passes the quality checks before submitting.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **OpenCV**: For real-time computer vision processing.
- **MediaPipe**: For hand gesture recognition.
- **Python**: For building the application.
