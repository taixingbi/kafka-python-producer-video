import cv2

video_file= 'input/2.jpg'
video = cv2.VideoCapture(video_file)

success, frame = video.read()

print(success, frame )