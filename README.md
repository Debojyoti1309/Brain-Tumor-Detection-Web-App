# Brain-Tumor-Detection-Web-App

## Overview

This project is focused on building a web application for detecting brain tumors using a Convolutional Neural Network (CNN). The application is built using Flask for the web interface and MongoDB for the database. The project is part of my final year work as a Master of Computer Application (MCA) student at Maulana Abul Kalam Azad University of Technology.

## Author

Debojyoti Das  
Final Year Student,  
Master of Computer Application (MCA),  
Maulana Abul Kalam Azad University of Technology

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Flask App Structure](#flask-app-structure)
- [Database](#database)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

## Project Description

The goal of this project is to develop an automated system for detecting brain tumors from MRI images. The system uses a Convolutional Neural Network (CNN) to analyze MRI images and determine the presence of a tumor. The web application allows users to upload MRI images, processes them through the trained CNN model, and returns the results.

## Technologies Used

- Python
- Flask
- TensorFlow/Keras (for CNN)
- MongoDB
- HTML/CSS/JavaScript

## Setup Instructions

### Prerequisites

- Python 3.x
- MongoDB
- Git

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Debojyoti1309/Brain-Tumor-Detection-Web-App.git
   cd Brain-Tumor-Detection-Web-App
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up MongoDB:
   - Ensure MongoDB is installed and running.
   - Create a database named `brain_tumor_db`.

5. Run the Flask app:
   ```sh
   python app.py
   ```

6. Open your browser and go to `http://127.0.0.1:5000`.

## Usage

1. Navigate to the web application.
2. Upload an MRI image using the provided form.
3. Click on the 'Submit' button to get the prediction results.
4. The results page will display whether a brain tumor is detected or not.

## Dataset

The dataset used for training the CNN model consists of MRI images labeled as either having a tumor or being tumor-free. The dataset should be preprocessed and split into training and validation sets.

## Model Training

The CNN model is trained using TensorFlow/Keras. The training script (`train_model.py`) includes data preprocessing, model architecture definition, compilation, and training steps.

## Flask App Structure

```
Brain-Tumor-Detection-Web-App/
│
├── app.py              # Main Flask application
├── model.py            # CNN model definition and loading
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── utils/              # Utility functions
├── requirements.txt    # Python dependencies
├── train_model.py      # Script to train the CNN model
└── README.md           # Project README
```

## Database

MongoDB is used to store user data and MRI image metadata. The database connection is handled in the `app.py` file.

## Future Work

- Enhance the CNN model for better accuracy.
- Implement user authentication for a more secure application.
- Add more comprehensive error handling.
- Expand the dataset for training with more diverse images.

## Acknowledgements

I would like to thank my professors and peers at Maulana Abul Kalam Azad University of Technology for their support and guidance throughout this project.

---
