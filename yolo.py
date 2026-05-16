import cv2
from ultralytics import YOLO



# YOLOモデルを読み込む
model = YOLO('yolo11n.pt')

# バスの画像を認識する
bus_image_url = 'https://ultralytics.com/images/bus.jpg'

# 推論実行
results = model(bus_image_url)

# 推論結果を表示
annotated_frame = results[0].plot()
cv2.imshow('bus', annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()