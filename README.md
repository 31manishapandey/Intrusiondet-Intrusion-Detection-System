# Multi-Scale Transformer & AI-Based Intelligent Network Intrusion Detection System

This project presents an **AI-powered Network Intrusion Detection System (IDS)** designed to identify malicious network traffic using deep learning techniques.  
The system analyzes **41 network traffic features** and predicts whether the traffic is **normal or an intrusion attack**.

The project also includes a **web-based interface** built using Flask that allows users to input network traffic data and receive real-time predictions.

----

## Features

- Deep Learning based Intrusion Detection Model
- Web Application using Flask
- Real-time network traffic prediction
- Detects **Normal vs Intrusion traffic**
- Interactive user interface
- Scalable architecture for cybersecurity applications

---

## Technologies Used

- Python
- TensorFlow / Keras
- Scikit-learn
- Flask
- HTML
- CSS

---

## Dataset

The model is trained using a **network intrusion dataset containing 41 features representing network traffic characteristics**.

These features include attributes such as:

- Protocol type
- Service
- Flag status
- Source bytes
- Destination bytes
- Connection statistics
- Traffic behavior patterns

The dataset is used to classify traffic into **Normal or Intrusion categories**.

---

## Project Structure

```
IDS_Project
│
├── app.py
├── IDS_Intrusiondet_model.h5
├── scaler.pkl
├── requirements.txt
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
└── README.md
```

---

## Installation and Setup

### 1 Clone the repository

```
git clone https://github.com/31manishapandey/Intrusiondet-Intrusion-Detection-System.git
```

### 2 Navigate to project directory

```
cd Intrusiondet-Intrusion-Detection-System
```

### 3 Install dependencies

```
pip install -r requirements.txt
```

### 4 Run the Flask application

```
python app.py
```

### 5 Open the application in your browser

```
http://127.0.0.1:5000
```

---

## Web Application Interface
app_screenshot.png
![Web App](app_screenshot.png)

The web application allows users to:

- Enter network traffic feature values
- Submit data for analysis
- Receive **intrusion detection results instantly**

Example output:

```
Prediction: Intrusion Detected
Confidence: 95%
```

---

## Applications

This project can be used in:

- Network Security Monitoring
- Cybersecurity Research
- Intrusion Detection Systems
- Security Operations Centers (SOC)
- AI-based Threat Detection

---
  
## Web Application Deployment

The trained deep learning model is deployed using a Flask web application.

Users can input network traffic features through a web interface and the model predicts whether the traffic is normal or malicious.

Steps:

1 Run the Flask server

python app.py

2 Open the browser

http://127.0.0.1:5000
---

## Future Improvements

- Multi-class attack classification (DoS, Probe, R2L, U2R)
- Real-time packet capture integration
- Dashboard for network traffic visualization
- Cloud deployment for live monitoring
- Integration with security monitoring tools

---

## Author

Manisha Pandey  
MSc IT – Artificial Intelligence Project

---

## License
This project is developed for **academic and research purposes**.
