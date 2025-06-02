# 🤖ChatFusion - Web Based AI ChatBot
ChatFusion is an intelligent, multimodal chatbot that seamlessly blends text, speech, PDF, and image understanding. Powered by Google Gemini AI, it enables dynamic interactions like resume-based Q&A, voice conversations, and image text recognition — all through a unified web interface.
# 📌 Project Overview

This project is a Flask-based AI-powered chatbot that enables users to interact in multiple ways including:

- 📄 **PDF Q&A:** Ask questions based on uploaded resume or document PDFs.  
- 🎤 **Voice Input:** Use speech-to-text and text-to-speech for voice interaction.  
- 🖼️ **Image Input:** Upload images for either general recognition or text extraction.  
- 🤖 **Gemini AI Integration:** Uses Google's Gemini API (Generative AI) to process queries and provide intelligent responses.  
- 🧠 **MongoDB Integration:** Stores all questions and AI-generated responses for historical tracking and analysis.
# 🚀 Features of ChatFusion

| **Category**              | **Feature**                         | **Description**                                                                 |
|---------------------------|-------------------------------------|---------------------------------------------------------------------------------|
| 🧠 AI-Powered Interactions | General Q&A                         | Ask open-ended questions and get intelligent answers via Google Gemini API.    |
|                           | Resume-Based Q&A                    | Upload a resume (PDF) and receive answers based on its content.                |
| 🔤 Multimodal Input/Output | Text-to-Text                        | Classic chat interaction using typed input and text response.                  |
|                           | Text-to-Speech                      | Converts AI answers to spoken audio using text-to-speech technology.           |
|                           | Speech-to-Text                      | Speak your question and get transcribed + answered automatically.              |
|                           | Speech-to-Speech                    | Full voice interaction — speak and hear the AI respond.                        |
| 📄 PDF Integration         | Resume Upload                       | Accepts and stores uploaded PDF resumes securely.                              |
|                           | PDF Text Extraction                 | Extracts text from PDF files for contextual understanding.                     |
| 🖼️ Image Processing        | Image Upload                        | Upload images for recognition or text extraction.                              |
|                           | General Image Recognition           | Identifies objects or elements in the uploaded image.                          |
|                           | Text Recognition (OCR)              | Extracts readable text from images using Optical Character Recognition.        |
| 📦 Backend & Management    | MongoDB Integration                 | Stores all questions and responses with timestamps.                            |
|                           | Session Management                  | Remembers session states (like PDF mode).                                      |
|                           | Caching                             | Speeds up responses for previously asked questions.                            |
| 🔐 Secure Configuration    | `.env` Configuration                | All API keys and DB URLs are hidden via environment variables.                 |
|                           | Upload Folder Isolation             | Uploads and images are ignored by Git and stored locally.                      |
| 🧪 Developer Friendly      | Modular Utilities                   | PDF, speech, and image helpers split into separate modules for clarity.        |
|                           | Easily Extendable                   | Designed to allow easy feature additions or upgrades.                          |
#  📁Folder Structure
```
ChatFusion/
├── app.py
├── .env.example # Example environment variables file
├── .gitignore
├── requirements.txt
├── README.md
├── service_account.json # Service account credentials (usually for cloud APIs)
│
├── utils/
│   ├── pdf_helper.py
│   ├── speech_helper.py
│   ├── image_helper.py
│   └── pycache/ # Python cache files folder (auto-generated)
│
├── templates/
│   ├── index.html
│   ├── general_questions.html
│   ├── pdf_questions.html
│   ├── text_to_text.html
│   ├── text_to_speech.html
│   ├── speech_to_text.html
│   ├── speech_to_speech.html
│   ├── image_upload.html
│   ├── image_options.html
│   ├── general_image_recognition.html
│   └── text_extraction_result.html
│
├── static/
│   └── styles.css # CSS styling for the web app
│
├── uploads/
│   └── README.txt # Folder placeholder to keep uploads visible in git
│
└── images/
    └── README.txt # Folder placeholder to keep images visible in git
```
# Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DHIKSHAMP/chatfusion.git
   cd chatfusion
   ```
2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
   ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:

    Rename .env.example to .env.

    Update the variables inside .env with your own values (API keys, database URL, etc.).

5. **Run the Flask application:**

   ```bash
   flask run
   ```
6. **Open your browser and go to:**

    ```bash
    Open your browser and go to:
    ```
Optional:

To run the app with debug mode on (for development):
```bash
flask run --debug
```

# 🛠️ Tech Stack

| Technology       | Description                                         |
|------------------|-----------------------------------------------------|
| **Python**       | Core programming language                          |
| **Flask**        | Web framework for building the app                 |
| **HTML/CSS**     | Frontend templating and styling                    |
| **JavaScript**   | Enhances interactivity in UI                       |
| **MongoDB**      | Database to store questions and responses          |
| **Google Gemini API** | AI-powered responses using generative models      |
| **SpeechRecognition** | Used for converting speech to text                |
| **gTTS / pyttsx3**| Used for converting text to speech                 |
| **OpenCV / pytesseract** | For image recognition and text extraction        |
| **dotenv**       | Manage environment variables securely              |

# 🎬 Output Video: 

📽️Watch here: [@chatfusion](https://sites.google.com/view/dhikshacyber/other-projects)

# 📌 Use Case Scenarios

| Scenario | Description |
|----------|-------------|
| **Job Seekers** | Upload resumes and ask questions like "What are my key skills?" or "Which experience is most relevant for a data science role?" |
| **Students** | Upload academic documents or notes and interact via questions to revise content. |
| **Business Users** | Convert voice queries into intelligent answers and extract insights from PDFs and images. |
| **Accessibility Support** | Visually impaired users can benefit from speech-to-text and text-to-speech features. |
| **Research Assistance** | Quickly scan documents or images for important content and interact via natural language. |

---

# 🚀 Future Enhancements

| Feature | Description |
|---------|-------------|
| **User Authentication** | Enable user login/signup for personalized experience and data security. |
| **History Dashboard** | Provide a UI to view all previous queries and responses from MongoDB. |
| **Multi-Language Support** | Extend speech/text capabilities to support other languages. |
| **Cloud Storage Integration** | Store uploaded files securely on cloud platforms like AWS S3 or Firebase. |
| **Mobile App Version** | Develop a cross-platform mobile app for on-the-go interaction. |
| **AI Voice Assistant Mode** | Turn ChatFusion into a real-time voice assistant with continuous conversation. |

# 👤 Author

**DHIKSHA M P**  

🌐 GitHub: [@DHIKSHAMP](https://github.com/DHIKSHAMP)

🔗 LinkedIn: [linkedin.com/in/dhikshamp](https://linkedin.com/in/dhiksha-m-p-095028257)

🌍 Portfolio: [Portfolio](https://sites.google.com/view/dhikshacyber/about)

## ⚖️ License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) – see the [LICENSE](./LICENSE) file for details.

## 🌟 Contributing

💡 Got suggestions or new ideas?  
🛠️ Pull Requests are welcome!  
📧 Contact me if you'd like to collaborate.

