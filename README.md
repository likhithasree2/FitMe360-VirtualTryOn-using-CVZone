# FitMe360 Virtual Try-On App

Experience a virtual fitting room with the FitMe360 Virtual Try-On App! This application allows users to try on different shirts in real time using their webcam.

## Features

- Real-time pose detection for accurate shirt overlay
- Interactive GUI for easy user interaction
- Supports both male and female shirt selections

## Technologies Used

- OpenCV for webcam access and image processing
- Mediapipe for real-time pose detection
- Tkinter for creating the interactive GUI
- CVzone library for overlaying images on the webcam feed

## Installation

1. Clone this repository to your local machine.
2. Run the main script:
    ```
    python - Virtualtryon.py
    ```

## Usage

1. Launch the application by running the script.
2. Select your gender from the dropdown menu.
3. Click the "Start" button to begin trying on shirts.
4. Use hand gestures to navigate through shirt options.
5. Press 'q' to exit the application.

## Requirements

- Python 3.10
- cvzone 1.5.6
- mediapipe 0.9.0.1
- opencv-python 4.5.4.60

## Credits

- This project utilizes the [cvzone](https://github.com/cvzone/cvzone) library for overlaying images on the webcam feed.
- Pose detection is powered by [Mediapipe](https://google.github.io/mediapipe/).
  
## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.
