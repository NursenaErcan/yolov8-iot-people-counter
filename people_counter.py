from ultralytics import YOLO
import cv2
from paho.mqtt import client as mqtt

# ======================
# CONFIG
# ======================
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883

MQTT_TOPIC = "iot/room/occupancy"   # Final occupancy
MQTT_CLIENT_ID = "yolo-counter-client"

VIDEO_PATH = "data/office.mp4"
MODEL = "yolov8n.pt"

# ======================
# YOLO INIT
# ======================
print("[INFO] Loading YOLO model...")
model = YOLO(MODEL)

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("[ERROR] Cannot open video.")
    exit()

# ======================
# MQTT CONNECT
# ======================
mqtt_client = mqtt.Client(client_id=MQTT_CLIENT_ID)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()

def send_occ(value):
    mqtt_client.publish(MQTT_TOPIC, str(value), qos=1)
    print(f"[MQTT] occupancy = {value}")

# ======================
# MAIN LOOP
# ======================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO DETECTION (no tracking needed)
    results = model(frame, classes=[0], verbose=False)

    people_now = 0

    # Count number of people
    if results[0].boxes is not None:
        people_now = len(results[0].boxes)

        # Draw boxes
        for box in results[0].boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)),
                          (0,255,255), 2)

    # Publish to MQTT
    send_occ(people_now)

    # Show video
    cv2.putText(frame, f"People: {people_now}", (20,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("People Counter", cv2.resize(frame, (960,540)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
mqtt_client.loop_stop()
mqtt_client.disconnect()

print("[INFO] Program finished.")
