import cv2 as cv
import argparse

# Komut satırından video dosyası al
parser = argparse.ArgumentParser()
parser.add_argument('--video', default='people.mp4', help='Path to video file')
args = parser.parse_args()

video = cv.VideoCapture(args.video)
subtractor = cv.createBackgroundSubtractorMOG2(20, 50)

print(f"Processing video: {args.video}")
print("Press 'x' to exit")

while True:
    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        
        # FPS göster
        fps = video.get(cv.CAP_PROP_FPS)
        cv.putText(frame, f'FPS: {int(fps)}', (10, 30), 
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv.imshow('Mask', mask)
        cv.imshow('Original', frame)

        if cv.waitKey(5) == ord('x'):
            break
    else:
        video.set(cv.CAP_PROP_POS_FRAMES, 0)

cv.destroyAllWindows()
video.release()