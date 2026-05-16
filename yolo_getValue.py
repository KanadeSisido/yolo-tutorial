import cv2
from ultralytics import YOLO
import pickle


# YOLOモデルを読み込む
model = YOLO('yolo11n.pt')

# バスの画像を認識する
bus_image_url = 'https://ultralytics.com/images/bus.jpg'

# pickleがあればそれを利用
try:
    with open('result.pkl', 'rb') as f:
        result = pickle.load(f)
        print("\n\npickleファイルから読み込みました\n")
except FileNotFoundError:
    # 推論実行
    print("\n\n推論を実行します\n")
    results = model(bus_image_url)
    result = results[0]
    # pickle保存
    with open('result.pkl', 'wb') as f:
        pickle.dump(result, f)



print("======= result ==========\n")
print(result)
print("\n")

print("======= result.boxes ==========\n")
print(result.boxes)
print("\n")

print("======= result.boxes.xyxy ==========\n")
print(result.boxes.xyxy)
print("\n")

print(f"Bounding Box: 左上({result.boxes.xyxy[0][0]}, {result.boxes.xyxy[0][1]}), 右下({result.boxes.xyxy[0][2]}, {result.boxes.xyxy[0][3]})")
