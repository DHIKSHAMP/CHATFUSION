# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:27:29 2025

@author: ACER
"""

import pyttsx3
import speech_recognition as sr
import pyaudio
# Initialize Text-to-Speech engine


def text_to_speech(text):
    tts_engine = pyttsx3.init(driverName='sapi5')
    tts_engine.say(text)
    tts_engine.runAndWait()

'''def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your question...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "There was an error with the speech recognition service."'''

'''def speech_to_text(selected_mic):
    import pyaudio
    import speech_recognition as sr

    recognizer = sr.Recognizer()
    p = pyaudio.PyAudio()

    # Get the mic index
    mic_index = None
    for i in range(p.get_device_count()):
        if selected_mic in p.get_device_info_by_index(i)['name']:
            mic_index = i
            break

    if mic_index is None:
        return {"error": "Microphone not found! Please select a valid microphone."}

    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=5)
            print("Listening...")
            audio = recognizer.listen(source)
            print("Processing audio...")

        question = recognizer.recognize_google(audio)
        print(f"Recognized Text: {question}")
        return {"question": question}

    except sr.UnknownValueError:
        return {"error": "Sorry, I couldn't understand the audio. Please try again."}
    except sr.RequestError as e:
        return {"error": f"Error connecting to the Speech Recognition service: {e}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}'''
    
  # To select the right microphone



def speech_to_text(selected_mic):
    recognizer = sr.Recognizer()

    # Get the mic index using the selected microphone
    mic_index = None
    for i in range(pyaudio.PyAudio().get_device_count()):
        if selected_mic in pyaudio.PyAudio().get_device_info_by_index(i)['name']:
            mic_index = i
            break

    if mic_index is None:
        return {"error": "Microphone not found! Please select a valid microphone."}

    with sr.Microphone(device_index=mic_index) as source:
        # Adjust for ambient noise for 3 seconds (adjust to your needs)
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust ambient noise for 3 seconds
        print("Listening for your question...")

        try:
            # We will increase the timeout and phrase_time_limit further to avoid premature timeout
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=10)  # Increased timeout and phrase time limit
            print("Processing your input...")

            # Recognize speech using Google's speech recognition
            question = recognizer.recognize_google(audio)
            print(f"Recognized Text: {question}")
            return {"question": question}
        
        except sr.WaitTimeoutError:
            print("Listening timed out, please try again.")
            return {"error": "Listening timed out, please try again."}
        
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Please try again.")
            return {"error": "Sorry, I couldn't understand that."}
        
        except sr.RequestError:
            print("Could not request results, check your network connection.")
            return {"error": "Could not request results, check your network connection."}
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": f"An error occurred: {e}"}





