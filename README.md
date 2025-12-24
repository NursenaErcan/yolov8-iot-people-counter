# Smart Office People Counter
AI-based room occupancy detection using YOLOv8, MQTT, Node-RED, and ESP32 (Wokwi)

## 📌 Project Overview
This project detects human presence in a room and calculates real-time occupancy using video analysis and IoT technologies. The system visually monitors people entering and exiting a room and triggers IoT-based alerts when occupancy exceeds a defined limit.

The project was developed as part of an IoT course and is fully simulation-based.

### 🔹 `IOT_Proje/`
This folder contains the **IoT implementation** of the project, including:
- ESP32 logic
- Wokwi simulation setup
- MQTT-based communication
- IoT control mechanisms (LED ON/OFF based on room occupancy)

### 🔹 `report.pdf`
This file provides the **comprehensive academic explanation** of the project, including:
- System architecture
- Methodology
- Technologies used
- Simulation results
- Comparison with related works
- Conclusion and future improvements

📄 **For full technical and theoretical details, please refer to `report.pdf`.**

---
---

## 🧠 System Architecture
1. Video input (camera or pre-recorded video)
2. YOLOv8-based human detection and tracking
3. Virtual line crossing for ENTRY / EXIT detection
4. Real-time occupancy calculation
5. MQTT data transmission to cloud
6. Node-RED dashboard visualization
7. ESP32 (Wokwi) simulation for LED control

---

## 🛠️ Technologies Used
- **YOLOv8** – Human detection
- **Python (OpenCV, NumPy)** – Video processing
- **MQTT** – Data communication
- **Node-RED** – Dashboard & logic control
- **ESP32 (Wokwi)** – IoT device simulation

---

## ⚙️ Methodology
- Each video frame is analyzed using YOLOv8
- Detected persons are tracked with bounding boxes
- A virtual line determines entry and exit direction
- Occupancy count updates in real time
- MQTT sends data to Node-RED
- Node-RED triggers ESP32 LED when limit is exceeded

---

## 📊 Results
- Accurate people detection in simulated environments
- Real-time occupancy visualization via Node-RED dashboard
- LED turns ON when room is full, OFF when available

---

## 🎯 Conclusion
This project demonstrates how AI-based computer vision can be integrated with IoT infrastructure to build a scalable and low-cost smart environment solution. The simulation-based approach allows testing without physical hardware while maintaining realistic system behavior.

---
