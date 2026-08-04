<div align="center">

# Intelligent AI Attendance System

### AI-Powered Smart Attendance using Face Recognition, Voice Recognition & Computer Vision

A modern attendance management system that automates classroom attendance using Artificial Intelligence. The system combines Face Recognition, Voice Recognition, Computer Vision, and Cloud Database integration to provide an accurate, secure, and efficient attendance experience for teachers and students.

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge&logo=supabase">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-orange?style=for-the-badge&logo=opencv">
<img src="https://img.shields.io/badge/scikit--learn-Machine%20Learning-yellow?style=for-the-badge&logo=scikitlearn">

</div>

---

# 🌐 Live Demo

🚀 **Try the Intelligent AI Attendance System**

**Live Application:**



---

# 📖 Project Overview

The Intelligent AI Attendance System is a smart classroom solution designed to automate attendance using Artificial Intelligence.

Instead of relying on traditional manual attendance, the system leverages **Face Recognition**, **Voice Recognition**, and **Computer Vision** to identify students accurately and record attendance automatically.

The platform provides dedicated dashboards for both teachers and students, enabling efficient classroom management, secure authentication, subject enrollment, attendance tracking, and AI-assisted attendance verification.

Built with **Python**, **Streamlit**, **Supabase**, **OpenCV**, **dlib**, **Resemblyzer**, and **Scikit-Learn**, the application demonstrates how multiple AI technologies can be integrated into a practical, real-world solution.

---

# ✨ Key Features

## 👨‍🏫 Teacher Portal

- Secure teacher authentication
- Create and manage classroom subjects
- Generate QR codes for student enrollment
- Upload classroom images for attendance
- Capture images using a live camera
- Face Recognition based attendance
- Voice Recognition based attendance
- View attendance history
- Manage enrolled students

---

## 🎓 Student Portal

- Secure Face ID login
- Student registration
- Face embedding generation
- Optional voice enrollment
- Join subjects using enrollment codes
- Attendance statistics dashboard
- Attendance history
- Manage enrolled courses

---

## 🤖 AI Features

- Face Detection
- Face Recognition
- Face Embedding Generation
- Speaker Recognition
- Voice Embedding Generation
- Automatic Attendance Prediction
- Multi-face Detection
- AI-based Student Verification

---

# 🧠 AI Pipeline

```text
Student Registration
        │
        ▼
Face Image + Voice Recording
        │
        ▼
Generate Face Embeddings
Generate Voice Embeddings
        │
        ▼
Store Embeddings in Supabase
        │
        ▼
Teacher Uploads Classroom Images
        │
        ▼
Face Detection
        │
        ▼
Face Recognition
        │
        ▼
Attendance Prediction
        │
        ▼
Attendance Stored in Database
```

---

# ⚙️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Database | Supabase |
| Face Recognition | dlib |
| Face Embeddings | face_recognition_models |
| Voice Recognition | Resemblyzer |
| Audio Processing | Librosa |
| Machine Learning | Scikit-Learn |
| Classifier | Support Vector Machine (SVM) |
| Image Processing | OpenCV, Pillow |
| Authentication | bcrypt |
| QR Code Generation | Segno |

---

# 🚀 Core Functionalities

### 👤 Face Recognition Attendance

- Detects faces from classroom images
- Generates facial embeddings
- Matches embeddings with registered students
- Automatically records attendance

---

### 🎙️ Voice Recognition Attendance

- Records classroom audio
- Generates speaker embeddings
- Identifies registered students
- Marks attendance using voice similarity

---

### 📚 Subject Management

- Create classroom subjects
- Generate enrollment codes
- QR Code based enrollment
- Manage enrolled students

---

### 📊 Attendance Dashboard

- Attendance statistics
- Attendance history
- Present/Absent records
- Subject-wise attendance reports

---

# 🏗️ System Architecture

```text
Teacher / Student
        │
        ▼
 Streamlit Frontend
        │
        ▼
Authentication Layer
        │
        ▼
AI Processing Layer
 ├── Face Recognition
 ├── Voice Recognition
 └── Attendance Prediction
        │
        ▼
Supabase Database
```

---

# 🎯 Project Highlights

- AI-powered attendance automation
- Face Recognition authentication
- Voice Recognition authentication
- Multi-face classroom attendance detection
- QR Code based subject enrollment
- Dedicated Teacher & Student dashboards
- Secure cloud database integration
- End-to-end attendance management workflow

---

# 📂 Project Structure

```text
Intelligent-AI-Attendance-System/
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
├── requirements.txt
├── .gitignore
├── .env.example
├── app.py
└── README.md
```

---

# 🖥️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/harsh-v16/Intelligent-AI-Attendance-System.git

cd Intelligent-AI-Attendance-System
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root and add the required API keys and database credentials.

Example:

```text
SUPABASE_URL=your_supabase_url

SUPABASE_KEY=your_supabase_key
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

Install all required Python packages using:

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database

The project uses **Supabase** as the backend database for storing:

- Student information
- Teacher information
- Face embeddings
- Voice embeddings
- Subject records
- Attendance history
- Enrollment data

---

# 🎓 Learning Outcomes

Through this project, I gained hands-on experience with:

- Face Recognition using Computer Vision
- Speaker Recognition using Voice Embeddings
- AI-based Attendance Automation
- Streamlit application development
- Supabase cloud database integration
- Authentication systems
- QR Code based enrollment
- Building end-to-end AI applications
- Integrating multiple AI pipelines into a single platform

---

# 🔮 Future Improvements

- 📱 Mobile application support
- ☁️ Cloud deployment
- 📷 Real-time webcam attendance
- 🎙️ Live classroom voice attendance
- 📈 Attendance analytics dashboard
- 🔔 Automated attendance notifications
- 📄 PDF attendance report generation
- 🧠 LLM-powered attendance insights

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository, create a feature branch, and submit a pull request.

---

# 👤 Author

<div align="center">

**Harsh Chaudhary**

AI Engineer | Machine Learning • Deep Learning • Generative AI Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-harsh--v16-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/harsh-v16)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harsh%20Chaudhary-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harsh-chaudhary-6ba5b8395)

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

It motivates me to continue building practical AI applications and sharing them with the community.

**Thank you for visiting this repository! 🚀**

</div>
