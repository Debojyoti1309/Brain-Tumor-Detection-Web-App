from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
import os
import cv2
import numpy as np
from keras.models import load_model
from dotenv import load_dotenv

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'your_secret_key'

# Connect to MongoDB
#client = MongoClient('mongodb://localhost:27017')
#db = client['brain_tumor']
#contacts_collection = db['contacts']
#users_collection = db['users']

# Connect to MongoDB Atlas
mongo_uri = os.getenv('mongodb+srv://odas1450:152535556@cluster0.nn5zaky.mongodb.net/')
client = MongoClient(mongo_uri)
db = client['brain_tumor']
contacts_collection = db['contacts']
users_collection = db['users']

# Load the trained model
model = load_model('model(98.96%).h5')

# Function to preprocess the image
def preprocess_image(image):
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=-1)
    return image

# Route to render the upload form
@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Route to handle file upload and tumor detection
@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        # Handle file upload and tumor detection
    #    def upload_files():
   # if request.method == 'POST':
        files = request.files.getlist('files')
        results = []
        for file in files:
            filename = os.path.join('static', 'uploads', file.filename)
            file.save(filename)
            image = cv2.imread(filename)
            processed_img = preprocess_image(image)
            class_probabilities = model.predict(processed_img)
            predicted_class = np.argmax(class_probabilities)
            results.append({
                'filename': file.filename,
                'tumor_detected': bool(predicted_class),
                'image_url': filename
            })
        return render_template('result.html', results=results)
    else:
        # Render upload form or perform other GET request logic
        return render_template('upload.html')

# contact form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        contacts_collection.insert_one({'name': name, 'email': email, 'message': message})
        return redirect('/')
    return render_template('contact.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            flash('Username already exists, please choose a different one.', 'error')
            return redirect('/register')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            users_collection.insert_one({'username': username, 'password': hashed_password})
            flash('Registration successful! Please log in.', 'success')
            return redirect('/login')
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            return redirect('/')
        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect('/login')
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
