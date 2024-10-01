# Real-Time-Face-Detection-and-Recognition

# Project Description
This project implements Real-Time Face Detection and Recognition using OpenCV and the face_recognition library. The system encodes known faces from a folder of images and detects/recognizes faces in real-time via a webcam feed, displaying the recognized names on-screen.

# Features
Real-time face detection using OpenCV.
Face recognition from a live webcam feed.
Supports encoding of known faces from a specified directory.
Labels recognized faces with their names, and unknown faces are labeled as "Unknown."

# Requirements
To run this project, install the following dependencies:
Python 3.x
OpenCV (opencv-python)
face_recognition (face-recognition)
NumPy

# Installation
Install the required Python packages using pip:
pip install opencv-python face-recognition numpy

# Usage
Clone this repository or download the project files.
Place the images of known faces in a folder named IMAGES/. Each image should be named after the person in the image (e.g., john.jpg).

# Run the following command:
python your_script.py
The system will open the webcam feed and start detecting faces, displaying names of recognized faces.

# File Structure
|-- Real-Time Face Detection and Recognition
    |-- IMAGES/
        |-- [Images of known faces]
    |-- simple_facerecognition.py  # Contains the face recognition logic
    |-- your_script.py             # Main file to run the recognition system
    
# How it Works
The SimpleFacerecognition class loads and encodes known face images from the IMAGES/ directory.
It captures frames from the webcam, detects faces, and compares them with known faces.
Recognized faces are labeled with their names, and unknown faces are marked as "Unknown."
