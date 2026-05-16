import cv2

# Webカメラに接続
cap = cv2.VideoCapture(0)

# 無限ループ
while True:
    # カメラから現在の映像（フレーム）を読み込む
    ret, frame = cap.read()
    if not ret:
        break
    
    # 映像を表示
    cv2.imshow('webcam', frame)

    # qキーが押されたらループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラを解放
cap.release()
cv2.destroyAllWindows()