#
# https://algorithm.joho.info/programming/python/opencv-videocapture-mp4-movie-py/
#

import cv2

def main():

    # 動画の読み込み
    cap = cv2.VideoCapture("/home/user01/Download/SampleVideo_1280x720_20mb.mp4")

    # 動画終了まで繰り返し
    while(cap.isOpened()):

        # フレームを取得
        ret, frame = cap.read()

        # フレームを表示
        cv2.imshow("Frame", frame)

        # qキーが押されたら途中で終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

main()