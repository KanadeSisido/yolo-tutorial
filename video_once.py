import cv2


# Webカメラに接続
cap = cv2.VideoCapture(0)

# webカメラの画像を読み込む
ret, frame = cap.read()

# 映像を表示
cv2.imshow('webcam', frame)
cv2.waitKey(0)

# カメラを解放
cap.release()
cv2.destroyAllWindows()