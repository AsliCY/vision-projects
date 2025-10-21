# Motion Filtering

Motion detection in videos using background subtraction with OpenCV's MOG2 algorithm.

## Technologies Used
- OpenCV
- Python 3.13
- MOG2 Background Subtractor

## Source
This project was created following the [OpenCV Python Tutorial](https://www.youtube.com/watch?v=6xIVlduljl4&list=PL7yh-TELLS1FDEQmmfzwSKOqFMEPLtz6) with additional modifications.

## Features
- Background subtraction using MOG2
- Real-time motion detection
- Video looping
- Command-line argument support for video input
- FPS display

## Test Video
Test video used: [People Walking](https://youtu.be/YzcawvDGe4Y)

## Installation
```bash
pip install opencv-python
```

## Usage
```bash
# Use default video file (temp_video.mp4)
python3 main.py

# Specify a custom video file
python3 main.py --video your_video.mp4
```

Press `x` to exit.

## Notes
- Video files are excluded from the repository via `.gitignore`
- You can use any `.mp4` video file
- The video will loop automatically when it reaches the end