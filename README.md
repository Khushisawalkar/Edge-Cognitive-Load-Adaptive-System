# Edge Cognitive Load Adaptive System

## 🚀 Overview

This project detects cognitive load using multi-modal sensor data (temperature, light, motion) and performs adaptive decision-making on an ESP32 edge device.

## 🧠 Key Idea

Simulates cognitive load estimation using environmental proxies and performs real-time classification on edge hardware.

## ⚙️ Features

* Multi-sensor fusion (Temperature, Light, Motion)
* Real-time stress classification (LOW / MEDIUM / HIGH)
* Adaptive alert system (LED + Buzzer)
* Edge-based processing (low latency)

## 🏗️ System Architecture

(Add your circuit image later)

## 🧪 Working Logic

* High temperature + low light + no motion → HIGH stress
* Moderate conditions → MEDIUM stress
* Otherwise → LOW stress

## 📊 Output

| Condition | Output          |
| --------- | --------------- |
| HIGH      | LED + Buzzer ON |
| MEDIUM    | LED ON          |
| LOW       | OFF             |

## 🔮 Future Scope

* Machine Learning integration
* IoT dashboard
* Cloud analytics

## 🛠️ Tech Stack

* ESP32
* Arduino
* Wokwi Simulation

## 🔗 Wokwi Simulation

[▶️ Run Simulation on Wokwi](https://wokwi.com/projects/YOUR-PROJECT-LINK)
