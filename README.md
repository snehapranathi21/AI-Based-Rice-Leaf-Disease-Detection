# 🌾 AI-Based Rice Leaf Disease Detection Web App

This project is a **deep learning-based web application** designed to detect **rice leaf diseases** using **Convolutional Neural Networks (CNN)** and **MobileNetV2** with **transfer learning**. The app allows users to **register, log in, and upload images** of rice leaves to receive real-time disease predictions.

---

## 🚀 Features

* 🏠 **Home Page** – Overview and introduction to the system
* 🧑‍💻 **User Registration Page** – New users can create accounts
* 🔐 **User Login Page** – Secure authentication system
* 🌿 **Prediction Page** – Upload rice leaf images to predict disease type
* 📊 **Database Integration** – User data stored securely using **SQL**
* 🤖 **AI Model** – Trained using **CNN (MobileNetV2)** with **transfer learning** in Google Colab

---

## 🧐 Model Information

* **Architecture:** MobileNetV2 (Pre-trained on ImageNet)
* **Approach:** Transfer Learning
* **Framework:** TensorFlow / Keras
* **Training Environment:** Google Colab
* **Input:** Rice leaf image
* **Output:** Predicted disease category

---

## 🔧 Tech Stack

| Component       | Technology Used       |
| --------------- | --------------------- |
| **Frontend**    | HTML, CSS, JavaScript |
| **Backend**     | Flask (Python)        |
| **Database**    | SQL                   |
| **Model**       | CNN with MobileNetV2  |
| **Environment** | Conda                 |
| **Development** | Google Colab, VS Code |

---

## ⚙️ How to Run Locally

Follow the steps below to set up and run the project on your local system:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rice-leaf-disease-detection.git
cd rice-leaf-disease-detection
```

### 2️⃣ Create and Activate Virtual Environment

```bash
conda create -n env python=3.9
conda activate env
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

Visit:
🔗 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧬 Folder Structure

```
rice-leaf-disease-detection/
│
├── static/                  # CSS, JS, and Images
├── templates/               # HTML Templates
├── model/                   # Trained MobileNetV2 Model
├── app.py                   # Flask App Entry Point
├── requirements.txt         # Python Dependencies
├── database.sql             # SQL Database Schema
└── README.md                # Project Documentation
```

---

## 🧑‍� Future Enhancements

* Deploy the model on **Raspberry Pi** for real-time field detection
* Improve accuracy using **data augmentation** and **ensemble models**
* Add **disease treatment recommendations**
* Enable **multi-language support** for farmers

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify for learning purposes.
