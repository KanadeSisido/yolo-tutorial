import cv2
from ultralytics import YOLO

# YOLOモデルを読み込む
model = YOLO('yolo11n.pt')

# Webカメラに接続
cap = cv2.VideoCapture(0)

# 無限ループ
while True:
    # カメラから現在のフレームを読み込む
    ret, frame = cap.read()
    if not ret:
        break

    # 推論実行
    results = model(frame)

    # 検出結果を表示
    annotated_frame = results[0].plot()
    cv2.imshow('webcam', annotated_frame)

    # qキーが押されたらループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラを解放
cap.release()
cv2.destroyAllWindows()
