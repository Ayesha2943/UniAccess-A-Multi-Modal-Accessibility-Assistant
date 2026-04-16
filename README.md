
# 🌐 UniAccess: A Multi-Modal Accessibility Assistant

A smart assistive system designed to help individuals with motor, speech, or neurological disabilities interact with computers using **eye tracking, hand gestures, and voice commands**.

---

## 🚀 Project Overview

UniAccess is a **multi-modal accessibility platform** that overcomes the limitations of traditional assistive systems that rely on a single input method.

This system integrates:

* 👁️ Eye Tracking (for cursor navigation)
* ✋ Hand Gesture Recognition (for actions like clicking & scrolling)
* 🎤 Voice Commands (for system control)

By combining these modalities, UniAccess provides a **flexible, adaptive, and user-friendly interface** for people with diverse abilities.

---

## 🎯 Problem Statement

Most existing assistive technologies:

* Depend on a **single interaction mode**
* Fail in real-world conditions (lighting, noise, etc.)
* Are often **expensive and not adaptive**

UniAccess solves this by offering a **low-cost, multi-modal, and reliable accessibility solution**.

---

## 🧠 Core Concept

The system works in the following pipeline:

1. Capture input (camera + microphone)
2. Process input using AI models
3. Interpret user intent
4. Convert into system actions

---

## 🏗️ System Architecture

The system consists of:

* 👁️ Eye Tracking Module
* ✋ Hand Gesture Recognition Module
* 🎤 Voice Command Module
* 🧩 Multi-Modal Decision Engine
* 💻 Application Control Layer

All modules work together to provide seamless interaction.

---

## 🛠️ Tech Stack

### 🐍 Programming Language

* Python

### 📷 Computer Vision

* OpenCV
* MediaPipe

### 🎤 Speech Processing

* SpeechRecognition

### 🖱️ Automation

* PyAutoGUI

### 🔢 Supporting Libraries

* NumPy
* Math
* Time

---

## ⚙️ Key Features

* 👁️ Cursor control using eye gaze
* 👆 Click actions using blink detection
* ✋ Gesture-based navigation and scrolling
* 🎤 Voice-based commands for system control
* 🔄 Seamless switching between input modes
* 🎯 Real-time processing with high responsiveness
* 💡 Low-cost system (no special hardware required)

---

## 🧾 Modules Explanation

### 👁️ Eye Tracking Module

* Uses MediaPipe Face Mesh
* Tracks gaze direction for cursor movement
* Blink detection for clicking

### ✋ Hand Gesture Module

* Detects hand landmarks
* Recognizes gestures like:

  * Click
  * Scroll
  * Navigation

### 🎤 Voice Command Module

* Converts speech to text
* Executes commands like:

  * Open apps
  * Control system functions

---

## 🧪 How It Works (Technical)

* MediaPipe detects facial & hand landmarks
* SpeechRecognition converts voice → text
* Multi-modal engine:

  * Combines inputs
  * Resolves conflicts
  * Executes actions

---

## 📊 Evaluation Metrics

* Cursor accuracy
* Response time (latency)
* Stability (smooth interaction)
* Gesture recognition accuracy
* Voice command accuracy

---

## ▶️ Installation

```bash
git clone https://github.com/your-username/uniaccess.git
cd uniaccess
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

Ensure:

* Webcam is enabled
* Microphone is accessible

---

## 🌍 Applications

* Accessibility for disabled users
* Education (inclusive learning)
* Workplace productivity
* Rehabilitation systems
* Smart home interaction

---

## ✅ Advantages

* Multi-modal interaction
* Flexible and adaptive
* Low-cost solution
* Promotes independence
* Works in real-time

---

## ⚠️ Limitations

* Sensitive to lighting conditions
* Affected by background noise
* Requires initial user adaptation
* Performance depends on hardware

---

## 🔮 Future Scope

* Improve accuracy and performance
* Add mobile & IoT integration
* Support more gestures and commands
* Enhance UI/UX

---

## 🌱 SDG Impact

This project supports:

* Good Health & Well-being
* Quality Education
* Reduced Inequalities
* Industry Innovation

---

## 🙋‍♀️ Author

Ayesha Siddiqa
B.E. in Artificial Intelligence & Data Science

---

## 📜 License

This project is open-source and available under the MIT License.
