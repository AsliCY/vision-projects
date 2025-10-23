# Face Recognition Project

Real-time face recognition application using OpenCV and face_recognition library.

## Features

- Real-time face recognition via webcam
- Face matching with reference image
- Lightweight and fast performance

## Requirements

- Python 3.11 (Python 3.13 is not supported)
- Webcam

## Installation

1. Clone the repository:
```bash
git https://github.com/AsliCY/vision-projects.git
cd face-recognition
```

2. Create a virtual environment:
```bash
python3.11 -m venv cv-venv
source cv-venv/bin/activate  # Windows: cv-venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add your reference image:
- Save your photo as `reference.jpg` in the project root directory

## Usage
```bash
python3 main.py
```

- Press `q` to quit

## Notes

- The face_recognition library will download model files on first run
- You can adjust the tolerance value to change sensitivity (default: 0.6)
- Lower tolerance = stricter matching
- Higher tolerance = more lenient matching

## Troubleshooting

**ImportError with NumPy:**
```bash
pip install "numpy<2"
```

**Camera not working on macOS:**
- Make sure to grant camera permissions in System Settings

## Credits

This project was built following the tutorial by [NeuralNine](https://www.youtube.com/watch?v=pQvkoaevVMk)

## License

MIT