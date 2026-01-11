
## Installation & Usage

### Prerequisites

Ensure you have the following installed:

* Python 3.8+
* Git
* Virtual environment tool (optional but recommended)

---

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

### Create and Activate Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Database Migrations

```bash
python manage.py migrate
```

---

### Start the Django Server

```bash
python manage.py runserver
```

---

 Use the Application

1. Open a web browser and go to:
   `http://127.0.0.1:8000/`
2. Upload an eye image through the web interface
3. The system processes the image and displays the predicted cataract stage



## Model Note

The trained deep learning model is loaded by the Django application for inference.
Model training and experimentation were performed using Google Colab.

###
Automatic Cataract Detection System
Final Year Project – Bachelor of Engineering (Computer Engineering)

Overview
This project implements an automatic cataract detection system using deep learning.
The system analyzes eye images and classifies them into normal and different cataract stages

A Django-based web interface is used to upload images and display prediction results.

Classification Categories

* Normal
* Early-stage cataract
* Immature cataract
* Mature cataract

Technology Stack

* Python
* Django
* TensorFlow & Keras
* Convolutional Neural Networks (CNN)
* Google Colab

System Workflow

1. User uploads an eye image through the Django web interface
2. Image is preprocessed
3. CNN model performs classification
4. Predicted cataract stage is displayed

Objective

The objective of this project is to demonstrate the application of deep learning and web technologies in automating the classification of cataract stages from eye images for academic and experimental purposes.

Project Status

Academic project developed as part of the Final Year requirements for the Bachelor of Engineering in Computer Engineering.

 Notes (Optional – You can include or omit)
* This system is intended for academic use only
* Not a replacement for professional medical diagnosis

