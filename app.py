import pyaudio
from flask import Flask, render_template, request, redirect, url_for ,session
from utils.pdf_helper import extract_text_from_pdf
from utils.speech_helper import speech_to_text, text_to_speech
from utils.image_helper import recognize_image,extract_text_from_image
import google.generativeai as genai
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
app.config['IMAGE_UPLOAD_FOLDER'] = os.getenv("IMAGE_UPLOAD_FOLDER")
# Configure API Key
# Directly assigning the API key in the code
load_dotenv()
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)


@app.route('/')
def home():
    session.pop("pdf_mode", None)
    return render_template('index.html')

# General Questions route
@app.route('/general_questions')
def general_questions():
    return render_template('general_questions.html')

# PDF Questions route
@app.route('/pdf_questions', methods=['GET', 'POST'])
def pdf_questions():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']

        if pdf_file and pdf_file.filename.endswith('.pdf'):
            # Ensure the uploads directory exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)

            # ✅ Save the uploaded file
            pdf_file.save(pdf_path)

            # ✅ Extract text from the saved PDF
            resume_text = extract_text_from_pdf(pdf_path)

            if not resume_text.strip():
                return "Error: The uploaded PDF contains no readable text!", 400

            # ✅ Store resume_text in session for later use
            session['resume_text'] = resume_text
            session['pdf_mode'] = True

            return render_template('general_questions.html')

    return render_template('pdf_questions.html')

@app.route('/image_processing')
def image_processing():
    return render_template('image_upload.html')

# Image Upload Route
@app.route('/image_upload', methods=['POST'])
def image_upload():
    if 'image_file' not in request.files:
        return "No file part", 400

    image_file = request.files['image_file']
    
    if image_file.filename == '':
        return "No selected file", 400

    image_path = os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], image_file.filename)
    image_file.save(image_path)
    
    session['image_path'] = image_path  # Store path for processing
    return render_template('image_options.html')

@app.route('/image_options')
def image_options():
    return render_template('image_options.html')
# Main route

# Text-to-Text interaction
@app.route('/text_to_text', methods=['GET', 'POST'])
def text_to_text_route():
    if request.method == 'POST':
        question = request.form.get('question', '').strip()

        if not question:
            return "Error: Question cannot be empty!", 400

        # Ensure resume_text is retrieved properly
        resume_text = session.get('resume_text', '').strip() if session.get("pdf_mode") else ""

        answer = generate_ai_response(question, resume_text)  # Call AI response function
        return render_template('text_to_text.html', question=question, answer=answer)

    return render_template('text_to_text.html')

# Text-to-Speech interaction
@app.route('/text_to_speech', methods=['GET', 'POST'])
def text_to_speech_route():
    if request.method == 'POST':
        question = request.form.get('question', '').strip()

        if not question:
            return "Error: Question cannot be empty!", 400

        # Retrieve resume text if in PDF mode
        resume_text = session.get('resume_text', '').strip() if session.get("pdf_mode") else ""

        # Generate AI response
        answer = generate_ai_response(question, resume_text)

        # Convert answer to speech
        text_to_speech(answer)

        return render_template('text_to_speech.html', question=question, answer=answer)

    return render_template('text_to_speech.html')

# Speech-to-Text interaction
@app.route('/speech_to_text', methods=['GET', 'POST'])
def speech_to_text_route():
    if request.method == 'GET':
        # Get available microphones
        p = pyaudio.PyAudio()
        mic_list = [p.get_device_info_by_index(i)['name'] for i in range(p.get_device_count())]
        return render_template('speech_to_text.html', mic_list=mic_list)

    if request.method == 'POST':
        selected_mic = request.form.get('mic')
        result = speech_to_text(selected_mic)  # Convert speech to text

        if "error" in result:
            return render_template('speech_to_text.html', mic_list=[], error=result["error"])

        question = result.get("question", "").strip()  # Extract recognized speech

        if not question:
            return "Error: Could not recognize any speech. Please try again.", 400

        # Retrieve resume text if in PDF mode
        resume_text = session.get('resume_text', '').strip() if session.get("pdf_mode") else ""

        # Generate AI response
        answer = generate_ai_response(question, resume_text)

        return render_template('speech_to_text.html', mic_list=[], question=question, answer=answer)

    return render_template('speech_to_text.html')

# Speech-to-Speech Interaction
@app.route('/speech_to_speech', methods=['GET', 'POST'])
def speech_to_speech_route():
    if request.method == 'GET':
        # Get the list of available microphones
        p = pyaudio.PyAudio()
        mic_list = [p.get_device_info_by_index(i)['name'] for i in range(p.get_device_count())]
        return render_template('speech_to_speech.html', mic_list=mic_list)
    
    if request.method == 'POST':
        selected_mic = request.form.get('mic')
        result = speech_to_text(selected_mic)  # Convert speech to text
        
        if "error" in result:
            return render_template('speech_to_speech.html', error=result["error"])
        
        question = result.get("question", "").strip()  # Extract recognized text

        if not question:
            return "Error: Could not recognize any speech. Please try again.", 400

        # Retrieve resume text if in PDF mode
        resume_text = session.get('resume_text', '').strip() if session.get("pdf_mode") else ""

        # Generate AI response
        answer = generate_ai_response(question, resume_text)

        # Convert AI response to speech
        text_to_speech(answer)

        return render_template('speech_to_speech.html', question=question, answer=answer)

    return render_template('speech_to_speech.html')


# Helper function to generate AI responses
def generate_general_ai_response(question):
    chat_session = genai.GenerativeModel(model_name="gemini-2.0-flash-exp").start_chat(history=[])
    response = chat_session.send_message(question)
    return response.text
def generate_pdf_ai_response(question, resume_text):
    chat_session = genai.GenerativeModel(model_name="gemini-2.0-flash-exp").start_chat(history=[{
      "role": "user",
      "parts": [
        f"Here is my resume text:\n{resume_text}\n\nPlease answer the following question based on this resume: {question}"
      ]
    }])
    response = chat_session.send_message(question)
    return response.text

mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client[os.getenv("MONGO_DB_NAME")]
collection = db[os.getenv("MONGO_COLLECTION_NAME")]

import time

cache = {}

def generate_ai_response(question, resume_text=None):
    cache_key = (question, resume_text)
    
    if cache_key in cache:
        return cache[cache_key]  # Return cached response

    time.sleep(1)  # Prevent excessive requests

    if session.get("pdf_mode"):
        resume_text = session.get("resume_text", "").strip()
        response = generate_pdf_ai_response(question, resume_text)
    else:
        response = generate_general_ai_response(question)

    cache[cache_key] = response 
    document = {
        "question": question,
        "response": response,
        "timestamp": datetime.utcnow()  # Add a timestamp
    }

    # Insert the document into the collection
    collection.insert_one(document)
    print(f"Data stored in MongoDB with ID: {document['_id']}")# Store response
    return response
@app.route('/general_image_recognition', methods=['GET','POST'])
def general_image_recognition():
    image_path = session.get('image_path')
    if not image_path or not os.path.exists(image_path):
        return "No uploaded image found", 400

    result = recognize_image(image_path)
    return render_template('general_image_recognition.html', result=result)  # Placeholder response

@app.route('/text_recognition', methods=['GET', 'POST'])
def text_recognition():
    if request.method == 'POST':
        # Extract text from the uploaded image
        image_path = session.get('image_path')
        if not image_path or not os.path.exists(image_path):
            return "No uploaded image found", 400

        extracted_text = extract_text_from_image(image_path)

        # Display the extracted text in the result page
        return render_template('text_extraction_result.html', extracted_text=extracted_text)

    return render_template('text_recognition.html')


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
