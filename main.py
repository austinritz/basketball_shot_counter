import cv2


def main():
    path = "//wsl.localhost/Ubuntu/home/austritz/projects/yolo_v8_testing/photos/"
    cap = cv2.VideoCapture("photos/basketball_park.jpg")

    while True:
        ret, frame = cap.read()
        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27):
            break


if __name__ == "__main__":
    main()